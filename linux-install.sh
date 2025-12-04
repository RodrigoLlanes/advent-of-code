#!/bin/bash

cd ./pycp
source ./.venv/bin/activate
python3 setup.py pytest
python3 setup.py bdist_wheel
deactivate
cd ..
source ./.venv/bin/activate
pip uninstall pycp -y
pip install ./pycp/dist/pycp-0.0.1-py3-none-any.whl
deactivate
