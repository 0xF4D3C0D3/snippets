echo 'pass as $@'
./print_args.sh $@
echo
echo

echo 'pass as "$@"'
./print_args.sh "$@"
echo
echo

echo 'pass as $*'
./print_args.sh $*
echo
echo

echo 'pass as "$*"'
./print_args.sh "$*"
echo
echo

