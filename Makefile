MAIN_FILE=main.py

all:
	@echo "cmd:"
	@echo "  install    creates a virtual pyenv and"
	@echo "             installs all necessary dependencies."
	@echo "  run        starts the app in a pyenv"
	@echo "  mrproper   remove pyenv"

install:
	virtualenv venv;
	. ${PWD}/venv/bin/activate
	pip install -r requirements.txt

run:
	. ${MAIN_FILE}/venv/bin/activate
	python3 main.py

mrproper:
	rm -rf ./venv/
