
#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Train model
prepare:
	python $(PROJECT_DIR)/src/01_prepare.py

## Train model
train:
	python $(PROJECT_DIR)/src/02_train.py

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete