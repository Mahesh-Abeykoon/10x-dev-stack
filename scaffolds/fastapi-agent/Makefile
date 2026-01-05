.PHONY: install dev test build run

install:
	pip install -r requirements.txt

dev:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest

build:
	docker build -t fastapi-agent .

run:
	docker run -p 8000:8000 --env-file .env fastapi-agent
