SHELL := /bin/bash

fetch-data-from-gdrive:
	python ./scripts/data_acquisition/downloadFromGDrive.py
run-preprocessing-pipeline:
	python ./scripts/preprocessing/main.py

run-training-pipeline:
	python ./scripts/training/main.py

