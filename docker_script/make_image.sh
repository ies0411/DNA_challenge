#!/bin/bash

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DOCKER_DIR=${SOURCE_DIR}/docker
IMAGE_NAME=dna
DOCKER_BUILDKIT=1 docker build --build-arg CACHEBUST=$(date +%s) -t ${IMAGE_NAME} ${DOCKER_DIR}
