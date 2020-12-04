.ONESHELL:
SHELL := /bin/bash

ACTIVATE_VENV	= source scripts/activate.sh
REQUIREMENTS	= source scripts/requirements.sh
RUN_APP			= source scripts/run_app.sh
TEST_APP		= source scripts/test_app.sh

all:
	$(ACTIVATE_VENV) && $(RUN_APP)

test:
	@$(ACTIVATE_VENV) && $(TEST_APP)

cover:
	@$(ACTIVATE_VENV) && $(TEST_APP) "--cov=api"

