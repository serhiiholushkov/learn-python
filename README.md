# learn-python

# To install the exact package versions specified in a requirements.txt

pip install -r requirements.txt

# To generate/re-generate requirements file use

pip freeze > requirements.txt

# To add a single line to requirements

pip install <package> && pip freeze | grep <package> >> requirements.txt
