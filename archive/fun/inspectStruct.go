package main

import (
	"errors"
	"fmt"
	"reflect"
	"strings"
)

var errNotStruct = errors.New("anyStruct must be struct")

func dir(anyStruct interface{}) (map[string]map[string]string, error) {
	value := reflect.ValueOf(anyStruct)

	if value.Kind() != reflect.Struct {
		return nil, errNotStruct
	}

	res := map[string]map[string]string{}

	for i := 0; i < value.NumField(); i++ {
		mField := value.Field(i)
		mFieldType := value.Type().Field(i)

		res[mFieldType.Name] = map[string]string{}

		currentField := res[mFieldType.Name]
		currentField["category"] = "field"
		currentField["type"] = mField.Type().Name()
		if mField.CanInterface() {
			currentField["value"] = fmt.Sprintf("%v", mField.Interface())
		}
		if len(mFieldType.Tag) > 0 {
			currentField["tag"] = fmt.Sprintf("%v", mFieldType.Tag)
		}
	}

	for i := 0; i < value.NumMethod(); i++ {
		mMethod := value.Method(i).Type()
		mMethodType := value.Type().Method(i)

		res[mMethodType.Name] = map[string]string{}

		currentField := res[mMethodType.Name]
		currentField["category"] = "func"
		currentField["type"] = mMethodType.Type.String()

		ins := []string{}
		for j := 0; j < mMethod.NumIn(); j++ {
			ins = append(ins, mMethod.In(j).String())
		}
		currentField["input"] = strings.Join(ins, ", ")

		outs := []string{}
		for j := 0; j < mMethod.NumOut(); j++ {
			outs = append(outs, mMethod.Out(j).String())
		}
		currentField["output"] = strings.Join(outs, ", ")
	}

	return res, nil
}

type Person struct {
	Name   string `json:"name"`
	Nation string `json:"country" wow:"NOPE"`
	Zip    int
	wow    int
}

func (p Person) New(a int) Person                      { return Person{} }
func (p Person) GetAge(a, b int) (int, error)          { return 0, errors.New("TEST") }
func (p Person) IncreaseAge(by int, reason string) int { return 0 }
func (p Person) GetName(persons ...string) string      { return "WHATEVER" }

func main() {
	b := Person{
		Name:   "John",
		Nation: "German",
		Zip:    201,
		wow:    4,
	}

	info, _ := dir(b)

	for field, keys := range info {
		fmt.Printf("<%v>\n", field)
		for name, detail := range keys {
			fmt.Println("  ", name, "->", detail)
		}
	}
}
