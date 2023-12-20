pip-upgrade:
	pip install --upgrade pip

pip-dev:
	pip install -r requirements/requirements-dev.txt

pip-install:
	pip-compile requirements/requirements.in && pip install -r requirements/requirements.txt

graph:
	python3 manage.py graph_models

migration:
	python3 manage.py makemigrations && python3 manage.py migrate

create:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver localhost:8000

coverage:
	pytest --cov=babel --migrations -n 2 --dist loadfile

py_cov:
	coverage run -m pytest && coverage html

black:
	python3 -m black .
