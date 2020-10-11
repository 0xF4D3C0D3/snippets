#!/bin/bash

echo '$@'
i=0
for arg in $@; do
    echo $i: $arg; ((i++))
done 
echo

echo '"$@"'
i=0
for arg in "$@"; do
    echo $i: $arg; ((i++))
done 
echo

echo '$*'
i=0
for arg in $*; do
    echo $i: $arg; ((i++))
done 
echo

echo '"$*"'
i=0
for arg in "$*"; do
    echo $i: $arg; ((i++))
done 
echo
