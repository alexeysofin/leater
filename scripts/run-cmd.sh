#!/bin/sh

set -exu

exec docker-compose run --rm --entrypoint bash api scripts/docker/run-cmd.sh "${@}"