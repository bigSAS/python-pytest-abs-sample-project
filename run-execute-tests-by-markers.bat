set MARKERS=%1%

env\Scripts\activate & ^
pytest -vvv ^
--html=report.html --self-contained-html ^
--json-report --json-report-file=report.json ^
--log-file=run.log ^
-m %MARKERS% tests/
