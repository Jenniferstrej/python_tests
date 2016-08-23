# python_tests

A set of python tests examples

The instructions below are for Mac OS and may need to be adapted for other platforms

#Create and use a virtual environment

create the environment (once):

(in project folder)

virtualenv venv
to activate the virtual environment at any point:

source venv/bin/activate
to deactivate:

deactivate

#Install Python pre-requisites

(in project folder) (with active virtual environment as above)

pip install -r requirements.txt

#Running Unit tests

python -m unittest discover
