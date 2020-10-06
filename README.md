# python-pytest-abs-sample-project

Sample test project

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
