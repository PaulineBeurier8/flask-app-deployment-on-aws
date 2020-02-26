install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt


lint:
	pylint -E app.py

fmt:
	pylint -E app.py

format: fmt
