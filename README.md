# ccwc tool

## Table of contents
- [System Requirements](#system-requirements)
- [Project Structure](#project-structure)
- [Use of the Tool](#use-of-the-tool)
- [Tool Testing](#tool-testing)


### System Requirements

The ccwc tool has been build in Python, version 3.10.12.

There are two external libraries used, sys (system) and unittest.

### Project Structure

```
.
├── ccwc.py                  - the file contains methods used to measure input content.
├── main.py                  - the tool main entry.
├── process.py               - methods used to process command arguments.
├── test_ccwc.py             - tests applied in ccwc tool assessment.
└── test.txt                 - the file used in ccwc tool assessment.

```

### Use of the Tool

The tool takes a file or a pipe as an input and outputs file measurements according the chosen option.

The tool tries to follow wc syntax, thus its application is as follows:

```
python3 main.py ccwc [option] filename
```

There are five options supported:

- generic: without an option, outputs the number of lines, words and bytes in a file.
- ```-c```: outputs the number of bytes in a file.
- ```-l```: outputs the number of lines in a file.
- ```-w```: outputs the number of words in a file.
- ```-m```: outputs the number of chars in a file.

The tool also supports a combination of std_out input, where the ccwc options are as given above, in the form:

```
cat filename | python3 main.py ccwc [option]
```

### Tool Testing

The test file can be run from the command line:

```
python3 -m unittest test.py
```