from setuptools import find_packages, setup
import requests
import semantic_version

def get_LucidDynamodb_version():
    url = "https://pypi.org/pypi/LucidDynamodb/json"
    response = requests.request("GET", url, headers={}, data={})
    result = response.json()
    LucidDynamodb_version = str(result.get("info").get("version"))
    current_version = semantic_version.Version(LucidDynamodb_version)
    next_version = current_version.next_patch()
    return next_version

with open('requirements.txt', 'rt') as requirements:
    requires = requirements.readlines()
    setup(
            name="LucidDynamodb",
            version=str(get_LucidDynamodb_version()),
            author="Dinesh Sonachalam",
            author_email="dineshsonachalam@gmail.com",
            description="A simple Python wrapper to AWS Dynamodb",
            url="https://github.com/dineshsonachalam/Lucid-Dynamodb",
            install_reqires=requires,
            include_package_data=True,
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            python_requires='>=3.6',
    )