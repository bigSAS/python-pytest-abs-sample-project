:: clean chromedriver processes
tasklist /fi "imagename qa chromedriver.exe" |find ":" > nul
if errorlevel 1 taskkill /f /im "chromedriver.exe"
