#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters, please specify the path for the data file"
else
    /usr/bin/python3 gen.py $1
fi
