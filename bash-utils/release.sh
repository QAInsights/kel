#!/bin/bash

# IMPORTANT:
# Change the version in pyproject.toml and __version__.py
# before running this script

# get input from user
# shellcheck disable=SC2162

read -p "Did you change the version in pyproject.toml and __version__.py " message

if [ "$message" != "y" ]; then
    echo "Please change the version in pyproject.toml and __version__.py"
    exit 1
else
    echo "Continuing with the release"
    rm -rf ../dist
    echo "Release script"
    source ../*env/bin/activate
    poetry build
    twine upload ../dist/*

fi
