
.PHONY: all build run dev

all: run

build:
	docker build -t moser .

run:
	docker run -it --rm -p 5000:5000 moser

dev:
	docker run -v $(PWD)/moser:/app -it --rm -p 5000:5000 moser
