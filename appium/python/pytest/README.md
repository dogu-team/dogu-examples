# appium/python/pytest

## Requirements

* Python 3.9 or higher

## Activate virtual environment

```shell
python3 -m venv .venv

# on Windows powershell
.venv\Scripts\activate.ps1 

# on Windows cmd
.venv\Scripts\activate.bat 

# on Linux/MacOS
source .venv/bin/activate 
```

## Installation

```shell
pip3 install -r requirements.txt
```

## Usage

### Android web test

```shell
# "browserName" must exist in dogu.config.json
pytest android/test_web.py
```

### Android app test

```shell
# "appVersion" must exist in dogu.config.json
# "browserName" must NOT exist in dogu.config.json
pytest android/test_app.py
```
