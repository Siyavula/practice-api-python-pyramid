#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Create the virtual environment
if [ -d "venv" ]; then
    echo "${green}Virtual environment exists${reset}"
else
    echo "${yellow}Creating Virtual environment${reset}"
    virtualenv --python=python3.7 venv
    echo "${green}Virtual environment created${reset}"
fi

# Install app
#venv/bin/pip install -e practice-api-python-pyramid
#echo "${yellow}Installing practice-api-python-pyramid${reset}"
#echo "  ${green}practice-api-python-pyramid complete${reset}"