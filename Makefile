install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt


lint:
	pylint app.py
