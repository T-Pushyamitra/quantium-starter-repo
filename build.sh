#!/bin/bash

python -m venv venv
source venv/bin/activate
echo "Virtual Environment Activated"

pip install --upgrade pip
pip install -r requirements.txt

echo "Started Testing Application"
pytest

TEST_STATUS=$?

if [ $TEST_STATUS -eq 0 ]; then
    echo "Tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi
