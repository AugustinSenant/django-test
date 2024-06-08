run: ## Run the test server.
	python3 manage.py runserver_plus

install: ## Install the python requirements.
	pip3 install -r requirements.txt

migrate: ## Apply database migrations.
	python3 manage.py migrate