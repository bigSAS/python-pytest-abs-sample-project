# python-pytest-abs-sample-project

Sample test project

## Prepare environment

Using venv  

```sh
python -m venv env
env\Scripts\activate
(env) > pip install -r requirements.txt
```

## Run tests by markers using .bat file

Command: `run-tests.bat "{markers}" "{root-tests-folder}"`  

```sh
> run-tests.bat "unit" "tests/"
> run-tests.bat "unit and math" "tests/"
> run-tests.bat "unit or blog" "tests/"
```

## Run tests

all tests

```sh
env\Scripts\activate
(env) > pytest -vvv --html=report.html --json-report --json-report-file=report.json
```

marked tests

```sh
> env\Scripts\activate
(env) > pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit"
(env) > pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit and blog"
(env) > pytest -vvv --html=report.html --json-report --json-report-file=report.json -m "unit or blog"
```

