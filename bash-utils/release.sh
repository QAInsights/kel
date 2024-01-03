#!/bin/bash

echo "Release script"
source ../*env/bin/activate
poetry build
twine upload ../dist/*
