#!/bin/sh

set -exu


alembic revision --autogenerate -m "${@:-'New migration created'}"