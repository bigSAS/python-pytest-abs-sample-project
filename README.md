# python-pytest-abs-sample-project

Sample test project

## Prepare environment

Using venv  

```sh
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Run tests (todo log-cli-level)

all tests

```sh
env\Scripts\activate
pytest -vvv --html=report.html --json-report --json-report-file=report.json
```

marked tests

```sh
env\Scripts\activate
pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit"
pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit and blog"
pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit or blog"
```
