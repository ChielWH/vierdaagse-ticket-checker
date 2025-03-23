#!/bin/bash

SCRIPT_DIR="/Users/cheldoorn/personal-projects/ticket-checker"
VENV_DIR="$SCRIPT_DIR/.venv"
PYTHON_SCRIPT="$SCRIPT_DIR/main.py"

source "$VENV_DIR/bin/activate"
python "$PYTHON_SCRIPT"

exit $? # Exit with the same code as the Python script