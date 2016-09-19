
NAME = davidgasquez/moser:latest

.PHONY: all build run dev

all: run

build:
	docker build -t $(NAME) .

run:
	docker run -it --rm -p 5000:5000 $(NAME)

dev:
	docker run -v $(PWD)/moser:/app -it --rm -p 5000:5000 $(NAME)
