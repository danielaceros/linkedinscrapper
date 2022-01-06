<html>
<div align="center">
<img src="https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ-hqOabjK8ieuevGe6wlTD15QzOqw" alt="alt text" width="150" height="150"></img>
</div>
<h1 align="center">@danielaceros
<div align="center">
<a href=https://github.com/danielaceros><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=@danielaceros&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<img src="https://img.shields.io/github/followers/danielaceros?style=social" alt="Star Badge"/>
<a><img src="https://img.shields.io/github/last-commit/danielaceros/instaloaderbot" alt="Join Community Badge"/></a>
<a><img src="https://img.shields.io/github/repo-size/danielaceros/instaloaderbot" />
</div>
</html>

# linkedinscrapper
A ScrapperBOT who scraps Linkedin works and details from work offers, and save it as .xlsx to C:/ path
# Getting Started
Download the repo, and install the modules:
```bash
pip install bs4
pip install xlsxwriter
pip install time
pip install csv
pip install requests
pip install pandas
pip install tkinter
pip install win32api
pip install threading
pip install typing
pip install tqdm
```
# Running Code
On directory, with PowerShell or ComandPrompt, do:
```bash
python main.py
python3 main.py
```
# Main Menu
You will see two different options:
* 1-Menu with GUI, you should need the python module Tkinter
* 2-Menu with NOT-GUI
# Scrapping
Script has two options, or scrap one-time data, so you only have to put the URL, ej. 'https://www.linkedin.com/jobs/...'
Or ScrapLoop, that scrap data each interval of time you select, so once you put the link, it will be scraping on loop
# Finishing
The script will make a directory on you C:/ called 'ScrapperLogs', where it wil put the queries on .xlsx
