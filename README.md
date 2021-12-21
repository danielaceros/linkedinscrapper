# linkedinscrapper
A ScrapperBOT who scraps Linkedin works and details from work offers, and save it as .xlsx to C:/ path
# Getting Started
Download the repo, and install the modules:
* pip install bs4
* pip install xlsxwriter
* pip install time
* pip install csv
* pip install requests
* pip install pandas
* pip install tkinter
* pip install win32api
* pip install threading
* pip install typing
* pip install tqdm
# Running Code
On directory, with PowerShell or ComandPrompt, do:
* python main.py
* python3 main.py
# Main Menu
You will see two different options:
* 1-Menu with GUI, you should need the python module Tkinter
* 2-Menu with NOT-GUI
# Scrapping
Script has two options, or scrap one-time data, so you only have to put the URL, ej. 'https://www.linkedin.com/jobs/...'
Or ScrapLoop, that scrap data each interval of time you select
# Finishing
The script will make a directory on you C:/ called 'ScrapperLogs', where it wil put the queries on .xlsx
