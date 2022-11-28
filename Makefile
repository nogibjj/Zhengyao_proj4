install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py dblib/*py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib

build:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 536529811433.dkr.ecr.us-east-1.amazonaws.com
	docker build -t proj4 .
	docker tag proj4:latest 536529811433.dkr.ecr.us-east-1.amazonaws.com/proj4:latest
	docker push 536529811433.dkr.ecr.us-east-1.amazonaws.com/proj4:latest

all: install lint test