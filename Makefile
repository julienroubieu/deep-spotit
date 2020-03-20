
#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Train model
train:
	python $(PROJECT_DIR)/src/train.py

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete