. PHONY: all compile run test clean

all:
	make clean
	make test
	make run
	make compile

compile:
	cp outputs/output.rst ../dockstore-documentation/docs/output.rst
	cd ../dockstore-documentation/docs/; \
	make html; \
	python -mwebbrowser file:///$$(pwd)/_build/html/output.html

run:
	python3 main.py

test:
	mypy Gloss.py
	mypy main.py
	flake8 --ignore W191,E501,E231,E128 Gloss.py

clean:
	rm -f outputs/output.rst
	rm -f outputs/toc.rst