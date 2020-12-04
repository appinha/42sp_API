#!/bin/bash
## Script for running inside .venv

# Check requirements
check=$(pip3 freeze)
requirements='requirements.txt'
while read line; do
	[[ $check != *"$line"* ]] && pip3 install $line
done < $requirements
