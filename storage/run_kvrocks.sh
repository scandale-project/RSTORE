#!/bin/bash

set -e
set -x

if [[ -z "${KVROCK_BIN}" ]]; then
  ${KVROCK_BIN} -c kvrocks.conf
else
  ../../kvrocks/build/kvrocks -c kvrocks.conf
fi
