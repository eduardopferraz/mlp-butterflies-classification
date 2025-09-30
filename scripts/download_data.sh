#!/bin/bash
mkdir -p /workspaces/mlp-crocodile-classification/data/raw
kaggle datasets download zadafiyabhrami/global-crocodile-species-dataset -p /workspaces/mlp-crocodile-classification/data/raw --unzip

unzip data/raw/global-crocodile-species-dataset.zip -d data/raw