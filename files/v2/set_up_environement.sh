#!/bin/bash

ENV_NAME=venv
python -m venv --upgrade --upgrade-deps $ENV_NAME && chmod +x ./$ENV_NAME/bin/activate* && source ./$ENV_NAME/bin/activate && deactivate && source ./$ENV_NAME/bin/activate && pip3 install -r requirements.txt && deactivate || virtualenv --clear $ENV_NAME && chmod +x ./$ENV_NAME/bin/activate* && source ./$ENV_NAME/bin/activate && deactivate && source ./$ENV_NAME/bin/activate && pip3 install -r requirements.txt && deactivate
