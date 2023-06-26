#!/bin/bash
docker container rm -f web
docker build -t python-app . --no-cache
docker run --name web -d -p 8000:8000 python-app