#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters, please specify the path for the source file"
else
	/usr/bin/python3 q.py $1
fi
