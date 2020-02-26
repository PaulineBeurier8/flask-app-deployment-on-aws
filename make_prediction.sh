#!/usr/bin/env bash

PORT=8000
echo "Port: $PORT"

# POST method predict
curl -d '{"X": [1, 2]}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
