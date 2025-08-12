.PHONY: build run

build:
	docker build -t ml-deployment:latest .

run:
	docker run -p 8000:80 ml-deployment:latest
