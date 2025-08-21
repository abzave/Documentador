# Python Documentation Generator

This project generates code documentation for Python code. The goal of the project is to reduce the time spent writting code documentation.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [How to Compile and Run](#how-to-run)
5. [Usage](#usage)

## Project Overview

This documentation generator takes a Python file and looks for functions or methods lacking documentation. 

## Features

- **Generate Docstring**: Takes care of adding docstrings to the functions and methods present in a Python file.
- **List Python Files**: Lists all the files with extension `.py` in the current folder.
- **Search File in Path**: Allows the user to enter a path and look for Python files there.
- **Skip Functions and Methods**: Skips all constructors, getters, setters, and already documented functions and methods by default, as well as allowing the user to skip specific methods and functions.

## Requirements

- **Run everywhere with Python**: The project can run on any platform as long as it has a Python interpreter installed.
- **Read available files**: The project lists all the Python files that are avaible to document.

## How to Run

### Step 1: Clone the repository

``` bash
git clone https://github.com/abzave/Documentador.git
cd Documentador
```

### Step 2: Run the program

``` bash
python3 documentador.py
```

## Usage

1. Select a file from the listed available files.
    - If the file is located in a different path, enter the path where the file is located.
2. The user will be asked to confirm that the current function or method needs to be document. This is repeated for every eligible fuction and method present in the file.
    - If the function does not require documentation enter `-1`.
3. For every parameter present except for `self`, the user will be prompted to specify the data type.
4. Enter the output of the function or method if any.
5. Provide a description of the function or method functionality.
