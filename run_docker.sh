#!/usr/bin/env bash

# Docker Build:
docker build --tag pauline08/flask-app-deployment-on-aws:latest .

# List images:
docker image ls

# Run locally:
docker run -p 8000:80 pauline08/flask-app-deployment-on-aws:latest

# Ping local website
#http://localhost:8000
