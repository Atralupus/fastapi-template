# Rest API

## Setup
Use Python 3.8~ (recommend 3.9.10)

Dependency Manger is [Poetry](https://python-poetry.org)
```
# Dependency import
$ poetry install

# or

$ poetry install -E pytest
... etc
```

# Test
Use pytest
```
$ pytest tests/
```

# Rule
Lint: flake8, mypy
optional formatter: black

# Desc
Use RestAPI Framework [FastAPI](https://fastapi.tiangolo.com)

# Run
```
$ python app.py gen-spec execute
```