from setuptools import find_packages, setup

with open('requirements.txt', 'rt') as requirements:
    requires = requirements.readlines()
    setup(
            name="LucidDynamodb",
            version="1.0.1",
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