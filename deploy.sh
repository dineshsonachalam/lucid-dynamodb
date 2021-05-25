#!/bin/bash
cleanup() {
    rm -rf build dist *.egg-info
}

Main() {
    cleanup
    # Compliling your package
    python3 setup.py sdist bdist_wheel
    # Upload projects to pypi
    twine upload --skip-existing dist/*
    cleanup
}

Main