package main

import (
        "github.com/fsnotify/fsnotify"
        "gopkg.in/yaml.v2"
        "io/ioutil"
        "log"
        "reflect"
        "time"
)

type Library struct {
        Current int
}

func (l *Library) Increase(by int) {
        l.Current += by
}

func (l *Library) Decrease(by int) {
        l.Current -= by
}

func (l *Library) ReturnCall(name string, params ...interface{}) func() {
        v := reflect.ValueOf(l)
        m := v.MethodByName(name)

        reflectedParams := []reflect.Value{}
        for _, p := range params {
                reflectedParams = append(reflectedParams, reflect.ValueOf(p))
        }

        if m.IsValid() {
                return func() { m.Call(reflectedParams) }
        } else {
                log.Fatalln("There are no such", name, "method!")
        }
        return nil
}

type Spec struct {
        Adjust struct {
                Type string
                By   int
        }
}

func readConfig(fileName string) Spec {
        spec := Spec{}
        b, err := ioutil.ReadFile(fileName)
        if err != nil {
                log.Fatal(err)
        }

        err = yaml.Unmarshal(b, &spec)
        if err != nil {
                log.Fatal(err)
        }

        return spec
}

func NewWatcher(fileName string, newContent chan<- Spec, done <-chan bool) {
        watcher, err := fsnotify.NewWatcher()
        if err != nil {
                log.Fatal(err)
        }
        defer watcher.Close()

        go func() {
                for {
                        select {
                        case event, ok := <-watcher.Events:
                                if !ok {
                                        log.Fatal(event, ok)
                                }

                                if event.Op == fsnotify.Write {
                                        newContent <- readConfig(fileName)
                                }
                        }
                }
        }()
        watcher.Add(fileName)

        <-done
}

func main() {
        newContent := make(chan Spec)
        done := make(chan bool)

        go NewWatcher("/tmp/foo", newContent, done)

        lib := &Library{}

        updateInterval := time.Second
        nextUpdate := time.After(0)
        var updateLib func()

        go func() {
                for {
                        select {
                        case content, ok := <-newContent:
                                if !ok {
                                        log.Fatal(content, ok)
                                }
                                log.Printf("new config detected... %#v\n", content)
                                updateLib = lib.ReturnCall(content.Adjust.Type, content.Adjust.By)
                        case <-nextUpdate:
                                log.Println(lib.Current)
                                if updateLib != nil {
                                        updateLib()
                                }
                                nextUpdate = time.After(updateInterval)
                        }
                }
        }()

        newContent <- readConfig("/tmp/foo")

        <-done
}
