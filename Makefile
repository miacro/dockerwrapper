SHELL=/bin/bash
MAKE=make --no-print-directory

install:
	python setup.py install --user

test:
	python -m unittest discover ./dockerwrapper/test

uninstall:
	pip uninstall dockerwrapper

.PHONY:
	install uninstall
