env\Scripts\activate & ^
pytest -vvv ^
--html=report.html --self-contained-html ^
--json-report --json-report-file=report.json ^
--log-file=run.log ^
tests/
