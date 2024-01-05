# Backend initialization (WIP)

## Local with virtual environmennt

### Make sure you have Python (3.10) and pip installed

```
python3 --version
pip --version
```

### Clone repository

```
git clone https://github.com/mrMikoma/SmartRelay.git
```

### Setup and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### Install required modules

```
pip install -r requirements.txt
```

### Create .env file in following format

```
CITY=<city>
COORDINATES=<latitude>,<longitude>
```

### If successful, run program

```
python3 ./main.py
```

### Deactivate venv (when not used)

```
deactivate
```

## Docker

### Make sure you have Docker configured properly

### Build container image

```
docker build -t backend .
```

### Run container

```
docker run backend
```