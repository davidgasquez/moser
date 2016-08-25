#! /bin/bash

if [ "$1" == "dev" ]; then
    docker run -v $PWD/skflask:/app -it --rm -p 5000:5000 skflask
else
    docker run -it --rm -p 5000:5000 skflask
fi
