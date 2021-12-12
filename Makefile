SHELL := /bin/bash

fetch-data-from-gdrive:
	python3 ./scripts/data_acquisition/downloadFromGDrive.py
run-preprocessin-pipeline:
	python ./scripts/preprocessing/main.py
