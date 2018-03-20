#!/bin/bash

# Intended for the deployment of a python 3 package
usage="$(basename "$0") [-h] [-u s] -- to tar and upload python package

where:
    -h  show this help text
    -u  set the pypi username"

USER="sylhare"
while getopts ':hs:' option; do
  case "$option" in
    h | --help) echo "$usage"
       exit
       ;;
    u) seed="$OPTARG"
       ;;
    *) printf "missing argument for -%s\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))

# Check if twine is installed, if not install it
pip show twine 1>/dev/null
if [ $? != 0 ]; then
   pip install --upgrade twine
else
   echo "Installed" #Replace with your actions
fi

# Create the package tarball from the setup.py
python ../setup.py sdist

# Deploy the package in the dist folder
# twine upload -u $USER -p $PASSWORD --repository-url $URL dist/*
python -m twine upload -u $USER dist/*

exit 0;