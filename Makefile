# create env
build:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	@echo
	@echo 'Run with "./run.sh <text>"'
