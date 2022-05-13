. PHONY: all html reqs run test clean

all:
	make clean
	make test
	make run
	make html

clean:
	rm -f outputs/output.rst
	rm -f outputs/toc.rst

html:
	cp outputs/output.rst ../dockstore-documentation/docs/output.rst
	cd ../dockstore-documentation/docs/; \
	make html; \
	python -mwebbrowser file:///$$(pwd)/_build/html/output.html

reqs:
	# install requirements for dockstore-documentation - it's best to do this inside a venv
	# until dockstore-documentation merges 12.1 to devolp, we have to manually add attrs==21.4.0
	curl https://raw.githubusercontent.com/dockstore/dockstore-documentation/develop/requirements.txt >> requirements-dev.txt
	echo "attrs==21.4.0\n" >> requirements-dev.txt
	pip install -r requirements-dev.txt

run:
	python3 main.py

test:
	mypy Gloss.py
	mypy main.py
	flake8 --ignore W191,E501,E231,E128 Gloss.py