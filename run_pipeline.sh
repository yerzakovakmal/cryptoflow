#!/bin/bash

cd "$(dirname "$0")" || exit

./venv/bin/python3 -m ingestion.pipeline >> ingestion.log 2>&1