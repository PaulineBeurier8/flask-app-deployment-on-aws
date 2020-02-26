install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt


lint:
	@black --check app.py

fmt:
	@black app.py

format: fmt
