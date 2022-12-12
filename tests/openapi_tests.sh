#!/usr/bin/env bash

set -e
here="$( cd "$( dirname "$0" )" && pwd )"

function dotest {
  echo "---------------------------------"
  echo "Testing: $1"
  echo "---------------------------------"
  ./run_dirs.py "$1" test 2>/dev/null
}

function main {
  cd "$here"; cd ..; cd examples

  dotest dynu
  dotest hetzner
  dotest petstore2
  dotest petstore3
  dotest schemathesis

}

main
