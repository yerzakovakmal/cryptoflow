#!/bin/bash

cd /Users/akmalyerzakov/projects/github/cryptoflow

./venv/bin/python ingestion/pipeline.py >> ingestion.log 2>&1