set MARKERS=%1%
set ROOT=%2%

env\Scripts\activate & ^
pytest -vvv ^
--html=report.html --self-contained-html ^
--json-report --json-report-file=report.json ^
--log-file=run.log ^
-m %MARKERS% %ROOT% & ^
python move_reports.py
