all: lint

lint:
	python3 -m flake8 *.py

format:
	black *.py
