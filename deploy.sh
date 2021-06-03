#!/bin/bash
cleanup() {
    rm -rf build dist *.egg-info
}

Main() {
    cleanup
    # Compliling the package
    python3 setup.py sdist bdist_wheel
    # Upload projects to pypi
    twine upload --username $PYPI_USERNAME --password $PYPI_PASSWORD --skip-existing dist/*
    cleanup
}

Main
