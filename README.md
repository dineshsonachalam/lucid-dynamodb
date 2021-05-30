<p align="center">
  <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
</p>
<p align="center">
    <em>A minimalistic wrapper to AWS DynamoDB</em>
</p>
<p align="center">
  
<a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
    <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
</a>
  
<a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://img.shields.io/pypi/v/LucidDynamodb?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

## Installation

<div class="termy">

```console
$ pip install LucidDynamodb
```
  
</div>

**Prerequisite:**  
1. Set Python3 as a default python version on your MacOS/Linux.

```
# Step 1: Install Python3 using homebrew
$ brew install python

# Step 2: Look for the path where the latest python3 is available
dineshsonachalam@macbook ~ % ls -l /usr/local/bin/python*
lrwxr-xr-x  1 dineshsonachalam  admin  24 May 30 11:31 /usr/local/bin/python -> /usr/local/bin/python3.9

# Step 3: Change the default symbolic link to version of python you want to use
$ ln -s -f /usr/local/bin/python3.9 /usr/local/bin/python

# Step 4: Close the current terminal session or keep it that way and instead open a new terminal window (not tab). Check for the python version.
dineshsonachalam@macbook ~ % python --version
Python 3.9.2
```
2. Set pip3 as a default pip version on MacOS/Linux.
```
# Step 1: Add alias to your ~/.bashrc
dineshsonachalam@macbook ~ % cat ~/.zshrc | grep -i "alias"
alias pip=pip3
```
