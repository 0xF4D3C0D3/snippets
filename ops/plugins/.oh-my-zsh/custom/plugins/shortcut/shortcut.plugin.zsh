R() {(
    set -xe
    code="$1"

    if [[ ! -f "$code" ]]; then
        echo "$code doesn't exist"
        return
    fi

    exe="${code%.*}"
    shift
    gcc "$code" -Wall -o "$exe" -lm; ./"$exe" "$@"; rm ./"$exe"
)}

R0() {(
    set -xe
    code="$1"

    if [[ ! -f "$code" ]]; then
        echo "$code doesn't exist"
        return
    fi

    exe="${code%.*}"
    shift
    gcc "$code" -Wall -O0 -o "$exe" -lm; ./"$exe" "$@"; rm ./"$exe"
)}

D() {(
    set -xe
    file="$1"

    if [[ ! -f "$file" ]]; then
        echo "$file doesn't exist"
        return
    fi

    if [[ "$file" == *.c ]]; then
        code="$file"
        exe="${code%.*}"
        shift
        gcc "$code" -Wall -g -o "$exe" $@
    else
        exe="$file"
    fi

    gdb "$exe"
    rm "$exe"
)}

C() {(
    set -xe
    code="$1"

    if [[ ! -f "$code" ]]; then
        echo "$code doesn't exist"
        return
    fi

    exe="${code%.*}"
    shift
    gcc "$code" -Wall -O0 -o "$exe" -lm;
)}

zstyle ':completion:*:*:R:*:*' file-patterns '*.c'
zstyle ':completion:*:*:R0:*:*' file-patterns '*.c'
zstyle ':completion:*:*:D:*:*' file-patterns '*'
zstyle ':completion:*:*:C:*:*' file-patterns '*'

alias m='mark'
alias j='jump'
alias open='xdg-open'
