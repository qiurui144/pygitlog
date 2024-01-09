#/bin/bash
python setup.py bdist_egg
python setup.py install --user
python main.py