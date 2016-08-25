
.PHONY: all build run dev

all: run

build:
	docker build -t skflask .

run:
	docker run -it --rm -p 5000:5000 skflask

dev:
	docker run -v $(PWD)/skflask:/app -it --rm -p 5000:5000 skflask
