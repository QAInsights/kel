#!/bin/bash

# IMPORTANT:
# Change the version in pyproject.toml and __version__.py
# before running this script

rm -rf ../dist
echo "Release script"
source ../*env/bin/activate
poetry build
twine upload ../dist/*
