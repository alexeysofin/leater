#!/bin/sh

set -exu

exec pytest -vv -s "${@:-tests}"
