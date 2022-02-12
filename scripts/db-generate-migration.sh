#!/bin/sh

set -exu

exec docker-compose run --rm migrations scripts/docker/db-generate-migration.sh "${@}"