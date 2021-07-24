<h1 align="center">
  <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
  </a>
</h1>
<p align="center">
    <em>A minimalistic wrapper to AWS DynamoDB</em>
</p>
<p align="center">
    <a href="https://sonarcloud.io/dashboard?id=lucid-dynamodb">
        <img src="https://sonarcloud.io/api/project_badges/quality_gate?project=lucid-dynamodb"/>
    </a>
</p>

<p align="center">
    <a href="https://www.codacy.com/gh/dineshsonachalam/lucid-dynamodb/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dineshsonachalam/lucid-dynamodb&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/3607dfd408bb4b7394cb0631b717a76e"/>
    </a>
    <a href="https://snyk.io/test/github/dineshsonachalam/lucid-dynamodb">
        <img src="https://snyk.io/test/github/dineshsonachalam/lucid-dynamodb/badge.svg"/>
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
    </a>
    <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
        <img src="https://img.shields.io/pypi/v/LucidDynamodb?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/blob/master/LICENSE" target="_blank">
        <img src="https://badgen.net/github/license/dineshsonachalam/Lucid-Dynamodb" alt="MIT License" height="20">
    </a>
</p>

## Table of contents
- [Installation](#installation)
- [Example](#example)
    - [Connect to DynamodDB](#connect-to-dynamodb)
    - [Create a new table](#create-a-new-table)
    - [Get all table names](#get-all-table-names)
    - [Create a New Item](#create-a-new-item)
    - [Read an Item](#read-an-item)
    - [Read items by filter](#read-items-by-filter)
    - [Update existing attribute in an item](#update-existing-attribute-in-an-item)
    - [Add a new attribute in an item](#add-a-new-attribute-in-an-item)
    - [Add an attribute to the list](#add-an-attribute-to-the-list)
    - [Add an attribute to the string set](#add-an-attribute-to-the-string-set)
    - [Increase an existing attribute value](#increase-an-existing-attribute-value)
    - [Delete an attribute from an item](#delete-an-attribute-from-an-item)
    - [Delete an attribute from the string set](#delete-an-attribute-from-the-string-set)
    - [Delete an item](#delete-an-item)
    - [Delete a table](#delete-a-table)
- [Running tests](#running-tests)
- [Github Workflow Artifacts](#github-workflow-artifacts)
- [License](#license)

## Installation
<div class="termy">

```console
pip install LucidDynamodb
```
  
</div>

**Note:**  <a href="https://gist.github.com/dineshsonachalam/88f55b28c1f0c1ce93421f5a8f33e84a"> Prerequisite for Python3 development </a>

## Example

#### Connect to DynamoDB
You can connect to DynamoDB by following any of these two ways.

1. Using AWS config
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/using-aws-config-to-connect-to-dynamodb.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

2. Using AWS secret key
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/using-aws-secret-to-connect-to-dynamodb.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Create a new table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/1-create-a-new-table.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Get all table names
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/2-get-all-table-names.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Create a new item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/3-create-a-new-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Read an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/4-read-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Read items by filter
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/5-read-items-by-filter.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Update existing attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/6-update-existing-attribute-in-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Add a new attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/7-add-a-new-attribute-in-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Add an attribute to the list
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/8-add-an-attribute-to-the-list.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Add an attribute to the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/9-add-an-attribute-to-the-string-set.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Increase an existing attribute value
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/10-increase-an-existing-attribute-value.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete an attribute from an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/11-delete-an-attribute-from-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete an attribute from the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/12-delete-an-attribute-from-the-string-set.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/13-delete-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete a table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/14-delete-a-table.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## Running Tests

To run tests, run the following command

```bash
pytest -s
```

## License

[MIT](https://choosealicense.com/licenses/mit/) © [dineshsonachalam](https://www.github.com/dineshsonachalam)
