<h1 align="center">
  <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
  </a>
</h1>
<p align="center">
    <em>A minimalistic wrapper to AWS DynamoDB</em>
</p>

<p align="center">
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/markdown-autodocs.yml/badge.svg" alt="Deployment">
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
    - [Create a new table](#1-create-a-new-table)
    - [Get all table names](#2-get-all-table-names)
    - [Create a New Item](#3-create-a-new-item)
    - [Read an Item](#4-read-an-item)
    - [Increase an existing attribute value](#5-increase-an-existing-attribute-value)
    - [Update existing attribute in an item](#6-update-existing-attribute-in-an-item)
    - [Add a new attribute in an item](#7-add-a-new-attribute-in-an-item)
    - [Add an attribute to the list](#8-add-an-attribute-to-the-list)
    - [Add an attribute to the string set](#9-add-an-attribute-to-the-string-set)
    - [Delete an attribute from the string set](#10-delete-an-attribute-from-the-string-set)
    - [Delete an attribute from an item](#11-delete-an-attribute-from-an-item)
    - [Read items by filter](#12-read-items-by-filter)
    - [Delete a table](#13-delete-a-table)
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

### 1. Create a new table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/1-create-a-new-table.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 2. Get all table names
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/2-get-all-table-names.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 3. Create a New Item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/3-create-a-new-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 4. Read an Item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/4-read-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 5. Increase an existing attribute value
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/5-increase-an-existing-attribute-value.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 6. Update existing attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/6-update-existing-attribute-in-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 7. Add a new attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/7-add-a-new-attribute-in-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 8. Add an attribute to the list
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/8-add-an-attribute-to-the-list.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 9. Add an attribute to the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/9-add-an-attribute-to-the-string-set.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 10. Delete an attribute from the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/10-delete-an-attribute-from-the-string-set.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 11. Delete an attribute from an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/11-delete-an-attribute-from-an-item.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 12. Read items by filter
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/12-read-items-by-filter.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

### 13. Delete a table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/13-delete-a-table.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## Running Tests

To run tests, run the following command

```bash
pytest -s
```

## Github Workflow Artifacts

<!-- MARKDOWN-AUTO-DOCS:START (WORKFLOW_ARTIFACT_TABLE) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## License

[MIT](https://choosealicense.com/licenses/mit/) © [dineshsonachalam](https://www.github.com/dineshsonachalam)