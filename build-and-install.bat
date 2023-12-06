cd .\pycp\
call .\venv\Scripts\Activate.bat
call python setup.py pytest
call python setup.py bdist_wheel
call deactivate
cd ..
call .\venv\Scripts\Activate.bat
call pip uninstall pycp -y
call pip install .\pycp\dist\pycp-0.0.1-py3-none-any.whl
call deactivate