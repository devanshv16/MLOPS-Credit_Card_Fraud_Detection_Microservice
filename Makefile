install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C .

format:
	black .

format-check:
	black --check .

test:
	#python -m pytest -vv -cov=src tests/*.py
	PYTHONPATH=. pytest

all: install lint format test