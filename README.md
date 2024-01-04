# Project info

This project is part of my bachelor thesis and the case study within it.

The purpose of this project is to optimize house heating with relay.


# Project initialization (not tested)

## Make sure you have Python (3.10) and pip installed

```
python3 --version
pip --version
```

## Clone repository

```
git clone https://github.com/mrMikoma/SmartRelay.git
```

## Setup and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

## Install required modules

```
pip install -r requirements.txt
```

## Create .env file in following format

```
CITY=<city>
COORDINATES=<latitude>,<longitude>
```

## If successful, run program

```
python3 ./main.py
```

## Deactivate venv

```
deactivate
```