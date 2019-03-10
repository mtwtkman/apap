#!/bin/sh -eu

cmd=$1
shift

case $cmd in
  test) python -m unittest tests$@;;
  mypy) mypy apap;;
  format) black apap/*.py tests/**/*.py tests/*.py;;
  *) $cmd $@;;
esac
