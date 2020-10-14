# python-pytest-abs-sample-project

Sample test project using python + pytest + selenium + abs-web-testing 😎

## Prepare environment

Using venv module  

```sh
python -m venv env
env\Scripts\activate
(env) > pip install -r requirements.txt
```

## ABS configuration

ABS docs: [https://abs-web-testing.readthedocs.io/en/latest/](https://abs-web-testing.readthedocs.io/en/latest/)  
Place config in **config.yaml** file.
Path to config can be changed in conftest.py or environment variable **ABS_CONFIG_PATH**.  
Example  

```yaml
#config.yaml
wd_path: path/to/chromedriver/executable
find_element_timeout: 5
wait_for_condition_timeout: 10
wait_between: 0.5
```

## (Windows powershell) Run all tests using .bat file

Example

```ps1
.\run-execute-all-tests.bat
```

## (Windows powershell) Run tests by markers using .bat file

Example

```ps1
.\run-execute-tests-by-markers.bat "google or unit"
```

## (Windows powershell) Move reports into report folder

```ps1
.\run-move-reports.bat
```

## TODO: linux sh scripts
