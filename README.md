# Siyavuala Practice API
The Siyavula Practice API provides an easy way to integrate Siyavula's Practice into any application via a RESTful API.

## Siyavuala Practice API Demo
This repo serves as a demo application written in Python Pyramid to integrate with Siyavula's Practice API.  To authenticate with the API you will need API credentials.  If you do not yet have credentials, please contact sales@siyavula.com.

Please note that this is a only a demo application, the code was written to be as easy to understand as possible and as such might lack features you would expect in production level code.

## Requirements
* Python 3.7
* Pip
* Venv
* Linux

## Installation
#### Clone the repo:
    git clone git@github.com:Siyavula/practice-api-python-pyramid.git
#### Go to the `practice-api-python-pyramid` directory
    cd practice-api-python-pyramid
#### Install the virtual environment and app
    ./install.sh
#### Run the app
    ./start.sh
#### To demo the responsive version, in your browser go to:
    http://localhost:6543/emas
#### To demo the mobile (phones without JavaScript support) version, in your browser go to:
    http://localhost:6543/mobile
