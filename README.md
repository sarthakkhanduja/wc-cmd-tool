# Custom Word Count Tool (ccwc)

## Overview
This is Coding Challenge #1 by John Crickett.
The goal of this project is to create a Python-based command-line tool that replicates the functionality of the Unix `wc` (word count) command. This tool allows users to count the number of bytes, lines, words, and characters in a given file or from standard input. 

## Initial Approach

Initially, the script was written as mentioned in `main.py`

### Issues with the Initial Approach

1. **Lack of Standard Input Handling**: The initial script did not handle input from standard input (pipes).
2. **Hardcoded Argument Parsing**: The argument parsing was done manually, making the script less flexible and harder to maintain.
3. **Redundant File Openings**: Each function opened the file separately, which was inefficient.
4. **Error Handling**: The error handling was basic and could be improved for better user feedback.

## Improved Approach

The improved version of the script addresses these issues by using the `argparse` library for better argument parsing and support for standard input handling. 

### Improvements

1. **Standard Input Handling**: The script now supports reading from standard input using the `-` option.
2. **Efficient Argument Parsing**: The `argparse` library simplifies argument parsing and improves maintainability.
3. **File Handling**: The script uses context managers to handle file operations efficiently.
4. **Better Error Handling**: Improved error handling and user feedback.

## Installation and Usage

### Clone the Repository

```sh
git clone <repository-url>
cd <repository-directory>
```

### Make the Script Executable

Rename the script to `ccwc` and make it executable:

```sh
mv ccwc.py ccwc
chmod +x ccwc
```

### Add the Script to Your PATH
Move the script to a directory in your PATH:
```sh
sudo mv ccwc /usr/local/bin/
```

# Usage
## Count Bytes
```sh
ccwc -c <fileName>
```

## Count Lines
```sh
ccwc -l <fileName>
```

## Count Words
```sh
ccwc -w <fileName>
```
## Count Characters
```sh
ccwc -m <fileName>
```

## Example with Standard Input
```sh
echo "Hello, World!" | ccwc -w
```
