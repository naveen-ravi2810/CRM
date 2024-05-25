install_dep:
	# Install the dependency of the application
	poetry install

format:
	# Makes the format
	poetry run ruff format .

run:
	# starts the server makes the new migration code in migrate file
	poetry run python manage.py runserver

makemigration:
	# makes the new migration code in migrate file
	poetry run python manage.py makemigrations

migrate:
	# makes the new migration code in migrate to the database
	poetry run python manage.py migrate

newadmin:
	# create new super user
	poetry run python manage.py createsuperuser

start:
	# starts the server by doing dependency installation, Migration, create new admin user
	poetry install
	poetry run python manage.py migrate
	# Create a SuperUser
	poetry run python manage.py createsuperuser
	poetry run python manage.py runserver


RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[0;33m
BLUE=\033[0;34m
MAGENTA=\033[0;35m
CYAN=\033[0;36m
NC=\033[0m

help:
	# HELP COMMANDS
	@echo "     ${CYAN}     start              ${NC}basic command to start the application with every process 😁"
	@echo "     ${GREEN}     newadmin           ${NC}add new admin user to the application"
	@echo "     ${YELLOW}     install_dep        ${NC}to install application dependency"
	@echo "     ${BLUE}     format             ${NC}format the python files using ultrafast ruff"
	@echo "     ${MAGENTA}     run                ${NC}run the application in the debug mode"
	@echo "     ${RED}     makemigration      ${NC}make the new changes in the migrations"
	@echo "     ${CYAN}     migrate            ${NC}changes in DB if any new migrations in model happens"