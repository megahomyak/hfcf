.PHONY: all

all: invoke.o invoke

invoke:
	mkfifo invoke

invoke.o: invoke.c
	gcc -o invoke.o invoke.c
