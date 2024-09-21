install-deps:
ifeq ($(shell uname -s),Linux)
	pip install -r requirements.txt
endif

start:
ifeq ($(shell uname -s),Linux)
	python -m fastapi dev ./app/main.py
endif