INFO=

all:
	@echo "cmd:"
	@echo "  install    creates a virtual pyenv and"
	@echo "             installs all necessary dependencies."
	@echo "  run        starts the app in a pyenv"
	@echo "  mrproper   remove pyenv"

install:
	( \
	virtualenv venv -p python3; \
	. ${PWD}/venv/bin/activate; \
	pip install -r requirements.txt; \
	)

run:
	( \
	. ${PWD}/venv/bin/activate; \
	python main.py; \
	)

mrproper:
	rm -rf ./venv/

