all: lint

lint:
	python3 -m flake8 --max-line-length 99 *.py

format:
	black *.py
