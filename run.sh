pip install -r requirements-dev.txt
bumpversion --allow-dirty --current-version 1.0.0 minor setup.py telegramdb/constants.py run.bat run.sh
python setup.py sdist bdist_wheel
twine upload dist/*
del /Q dist