#!/bin/bash
set -exu

wait=()
timeout=60

show_help()
{
    echo "usage: ./wait-for-multiple.sh -s localhost:9092 -s db:5432 -t 15 echo 1"
}

# parse -s arguments
while getopts "t:s:h:" opt; do
    case $opt in
        s) wait+=("$OPTARG");;
        t) timeout=${OPTARG};;
        h) show_help
           exit 0
        #...
    esac
done
shift $((OPTIND -1))
[ "${1:-}" = "--" ] && shift

# wait for all services
for i in "${wait[@]}"; do
    $(dirname "$0")/wait-for-it.sh $i -t $timeout
done

# exec the rest of the command
exec "$@"
