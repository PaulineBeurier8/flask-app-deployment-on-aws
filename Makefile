install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


lint:
	@black --check app.py

fmt:
	@black app.py

format: fmt
