pip-upgrade:
	pip install --upgrade pip

pip-dev:
	pip install -r requirements/requirements-dev.txt && pip-compile requirements/requirements.in && pip install -r requirements/requirements.txt

