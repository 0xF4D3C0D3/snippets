### 1. ps is the command that diplays information about the active processes
`ps` is the one of tricky commands due to its myriad flags and backward-compatibilities.
so I try to organize it and make a thorough explanation for it.

let's start from `man ps`. it says _ps is used for reporting a snapshot of the current processes_.


### 2. `ps -ef` is UNIX-style and `ps aux` is BSD-style
ok. now we know what the ps is and what it is for. then how can we use it? _man_ says there are three kinds of options
can be used; UNIX, BSD, GNU. UNIX options are preceded by a dash, BSD options are **not** preceded by a dash, and
GNU options are preceded by **two** dashes. 


### 3. There are some compatibilities between UNIX and BSD styles though, don't rely upon them
be careful for using dash, for example, `ps -aux` and `ps aux` are totally different. In POSIX and UNIX, `ps -aux` means
print all processes owned by a user named "x", as well as printing all processes that would be seleced by `-a` option.
If the user named "x" does not exist, this may be the same as `ps aux` as follows:
```
jungdongho@jung-dong-ho-desktop:~$ A=$(ps aux | head) B=$(ps -aux | head) bash -c 'diff <(echo "$A") <(echo "$B")'
jungdongho@jung-dong-ho-desktop:~$ sudo useradd x
jungdongho@jung-dong-ho-desktop:~$ sudo -u x sleep 9999 &
[1] 12701
jungdongho@jung-dong-ho-desktop:~$ A=$(ps aux | head) B=$(ps -aux | head) bash -c 'diff <(echo "$A") <(echo "$B")'
1,10c1,10
< USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
< root           1  0.0  0.0 167908 12032 ?        Ss   15:44   0:03 /sbin/init splash
< root           2  0.0  0.0      0     0 ?        S    15:44   0:00 [kthreadd]
< root           3  0.0  0.0      0     0 ?        I<   15:44   0:00 [rcu_gp]
< root           4  0.0  0.0      0     0 ?        I<   15:44   0:00 [rcu_par_gp]
< root           6  0.0  0.0      0     0 ?        I<   15:44   0:00 [kworker/0:0H-kblockd]
< root           9  0.0  0.0      0     0 ?        I<   15:44   0:00 [mm_percpu_wq]
< root          10  0.0  0.0      0     0 ?        S    15:44   0:00 [ksoftirqd/0]
< root          11  0.0  0.0      0     0 ?        I    15:44   0:02 [rcu_sched]
< root          12  0.0  0.0      0     0 ?        S    15:44   0:00 [migration/0]
---
>     PID TTY          TIME CMD
>    1000 tty1     00:00:01 Xorg
>    1154 tty1     00:00:00 gnome-session-b
>    1806 tty2     00:05:55 Xorg
>    1817 tty2     00:00:00 gnome-session-b
>    1890 tty2     00:00:01 uim-xim
>    1891 tty2     00:00:01 uim-toolbar
>    1894 tty2     00:00:00 uim-helper-serv
>   12701 pts/0    00:00:00 sudo
>   12702 pts/0    00:00:00 sleep
```
However, it's more or less just for backward compatiblity so don't rely on it.


### 4. The outputs may different between UNIX and BSD styles
with UNIX-style, ps selects all processes with the same effective user ID(euid=EUID) as the current user and associated
with the same terminal as the invoker. It displays the process ID(pid=PID),
the terminal associated with the process(tname=TTY), the cumulated CPU time in [DD-]hh:mm:ss format(time=TIME), the
executable name(ucmd=CMD), and the output is unsorted.

BSD-style will add the several columns to ouput such as process state(stat=STAT), command args(args=COMMAND) instead of
the executable name and also change the process selection to include processes on other terminals(TTYs) that are owned
by you. 


### 5. UNIX style is the default and standard
the default output format is UNIX style


### 6. Process selection is additive
Except as described below, process selection options are additive. The default selection is discarded, and then the
selected processes are added to the set of processes to be displayed. A process will thus be shown if it meets any of the
given selection criteria.

```
jungdongho@jung-dong-ho-desktop:~$ ps -u whoopsie
    PID TTY          TIME CMD
   1389 ?        00:00:00 whoopsie
```
the default selection is discarded

```
jungdongho@jung-dong-ho-desktop:~$ ps -u whoopsie -u avahi
    PID TTY          TIME CMD
    774 ?        00:00:00 avahi-daemon
    824 ?        00:00:00 avahi-daemon
   1389 ?        00:00:00 whoopsie
```
two filters are additive, in other words, they are ORed.


### 6. 
