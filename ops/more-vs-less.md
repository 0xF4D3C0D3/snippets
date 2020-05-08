# more vs less

## Overview
### Name
```
more - file perusal filter for crt viewing
less - opposite of more
```

### Description
#### more
`more` is a filter for paging through text one screenful at a time.
This version is especially primitive. **Users should realize that
less(1) provides more(1) emulation plus extensive enhancements.**

#### less
`less` is a program similar to `more` (1), **but which allows backward
movement in the file as well as forward movement.**  **Also, less does
not have to read the entire input file before starting, so with large
input files it starts up faster than text editors like vi** (1). `less`
uses termcap (or terminfo on some systems), so it can run on a
variety of terminals.  There is even limited support for hardcopy
terminals.  (On a hardcopy terminal, lines which should be printed at
the top of the screen are prefixed with a caret.)

**Commands are based on both more and vi.**  Commands may be preceded by
a decimal number, called N in the descriptions below.  The number is
used by some commands, as indicated.

## Common
1. They are pager that helps the computer prints ouput one page at a time.

## Difference
1. `more` passes raw escape sequences that tell your terminal which colors to display by default.
2. `less` allows backward movement, but `more` can't.
3. `less` has about 27000 lines long, meanwhile `more` has about 2000 lines long.

## Note
1. Some systems hardlink `more` to `less`.

## Reference
- http://man7.org/linux/man-pages/man1/more.1.html
- http://man7.org/linux/man-pages/man1/less.1.html
- https://unix.stackexchange.com/a/81131

## Quotation
`less` is more, but more `more` than `more` is, so `more` is less `less`, so use more `less` if you want less `more`. (...) If `less` is more than `more`, `most` is more than `less`.” —Slackware Linux Essentials
