#!/bin/sh

set -exu

exec docker-compose run --rm migrations "${@}"