@ECHO OFF 
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\Users\abhis\anaconda3\Scripts\activate.bat" base

:: Section 2: Execute python script.
ECHO ============================
ECHO
cd "C:\Users\abhis\OneDrive\Documents\shoping\shoping"
ECHO ============================
scrapy crawl shoping_spider

ECHO ============================
ECHO End
ECHO ============================

rem End of script

