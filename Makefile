.PHONY: all setup lint run test

VENV := .venv/bin/activate

all: setup lint run

$(VENV):
	python3 -m venv .venv

setup: $(VENV)
	. $(VENV); pip install -r requirements.txt

run: $(VENV)
	. $(VENV); python3 main.py
