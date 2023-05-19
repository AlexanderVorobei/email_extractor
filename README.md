# Email extractor Script

This script is designed to extract email addresses from an image.

## Installation

1. Ensure that you have Python 3 installed.
2. Clone the repository containing the script's code.

## Dependencies

The script requires the following dependencies:

- Python 3
- Virtual environment (virtualenv)
- Libraries listed in the `requirements.txt` file

## Setup

1. Create a virtual environment:

```shell
python3 -m venv .venv
```

2. Activate the virtual environment:

```shell
source .venv/bin/activate
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```


## Usage

Run the script by providing the path to the input image and the path to the output text file:

```shell
python main.py --input /path/to/image.jpg --output /path/to/file.txt
```


## Makefile

The repository also includes a Makefile, which provides convenient commands for running and setting up the script. The main commands are:

- `make setup`: Install the required dependencies.
- `make run`: Run the script using the `INPUT` and `OUTPUT` environment variables.

Before running the `make run` command, make sure to set the `INPUT` and `OUTPUT` environment variables with the appropriate file paths:


```shell
export INPUT=/path/to/image.jpg
export OUTPUT=/path/to/file.txt
make run
```