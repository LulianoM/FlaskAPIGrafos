install-requirements:
	pip3 install -r requirements/requirements.txt

infrastructure/raise:
	docker-compose up -d --build

infrastructure/destroy:
	docker-compose down

local-venv:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate"
	pip3 install -r requirements/requirements.txt

prettify: local-venv
	black .

run-locally: local-venv
	clear
	python3 manage.py run -h 0.0.0.0

run-locally-docker: infrastructure/raise

test-application: local-venv
	pytest -svv --cov=application

test-api:
	pytest -svv --cov=domain tests/test_api.py