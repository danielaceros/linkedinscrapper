#   _      _       _            _ _____ _   _  _____                                       
#  | |    (_)     | |          | |_   _| \ | |/ ____|                                      
#  | |     _ _ __ | | _____  __| | | | |  \| | (___   ___ _ __ __ _ _ __  _ __   ___ _ __  
#  | |    | | '_ \| |/ / _ \/ _` | | | | . ` |\___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__| 
#  | |____| | | | |   <  __/ (_| |_| |_| |\  |____) | (__| | | (_| | |_) | |_) |  __/ |    
#  |______|_|_| |_|_|\_\___|\__,_|_____|_| \_|_____/ \___|_|  \__,_| .__/| .__/ \___|_|    
#                                                                  | |   | |               
#                                                                  |_|   |_|               

import bs4
import time
import os, sys
import csv
import requests
import pandas as pd
import tkinter
import time
from os import path
from pathlib import Path
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Button
from tkinter import messagebox
from tkinter import scrolledtext
from bs4 import BeautifulSoup
from time import localtime, strftime
from time import sleep
from requests.sessions import dispatch_hook
from win32api import GetSystemMetrics, SetFileAttributes
from tkinter import Tk, mainloop, TOP
from bs4.element import ProcessingInstruction
from datetime import datetime
from threading import *
from time import sleep
from typing import Counter
from tqdm import tqdm

# mkdir
try:
    os.mkdir("C:/ScrapperLogs/")
except FileExistsError:
    pass

# scrap function
def scrap(url):
    a = True
    uri = requests.get(url).text # request get (url)
    while a ==  True:
        # arrays
        dicsoup = []
        dicsoup2 = []
        dicsoup3 = []
        dicsoup4 = []
        dicsoup5 = []

        # soups
        soup = BeautifulSoup(uri, "html.parser").find_all(class_="base-card__full-link", href=True)
        soup2 = BeautifulSoup(uri, "html.parser").find_all(class_="base-search-card__title")
        soup3 = BeautifulSoup(uri, "html.parser").find_all(class_="base-search-card__subtitle")
        soup4 = BeautifulSoup(uri, "html.parser").find_all(class_="job-search-card__location")
        soup5 = BeautifulSoup(uri, "html.parser").find_all(class_="job-search-card__listdate--new") + BeautifulSoup(url, "html.parser").find_all(class_="job-search-card__listdate")

        # iterate soups
        for soups in soup:
            soupt = soups["href"]
            dicsoup.append(soupt)

        for soups2 in soup2:
            soup2t = soups2.text
            soup2ts = soup2t.replace("\n", "")
            soup2tss = soup2ts.strip()
            dicsoup2.append(soup2tss)

        for soups3 in soup3:
            soup3t = soups3.text
            soup3ts = soup3t.replace("\n", "")
            soup3tss = soup3ts.strip()
            dicsoup3.append(soup3tss)
        
        for soups4 in soup4:
            soup4t = soups4.text
            soup4ts = soup4t.replace("\n", "")
            soup4tss = soup4ts.strip()
            dicsoup4.append(soup4tss)

        for soups5 in soup5:
            soup5t = soups5.text
            soup5ts = soup5t.replace("\n", "")
            soup5tss = soup5ts.strip()
            dicsoup5.append(soup5tss)  
        
        a = False

    # logtitle
    time = datetime.now()
    dt_string = time.strftime("%d-%m-%Y %H.%M.%S")

    # exporting to xlsx
    d = {'JobTitle': dicsoup2,'Description': dicsoup3, 'Location': dicsoup4, 'Uploaded': dicsoup5, 'Link': dicsoup}
    df = pd.DataFrame.from_dict(d, orient='index')
    path = 'C:/ScrapperLogs/ScrapperLog ' + dt_string + '.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    dx = df.transpose()
    dx.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
    writer.close()
    size = Path(path).stat().st_size
    if size <= 6000:
        os.remove(path)
    else:
        pass

# function gui
def gui():
    # reescaling windows
    window = Tk() 
    window.title("Scrapper") 
    window.geometry(str(GetSystemMetrics(0)-400) + "x" + str(GetSystemMetrics(1)-200))

    def run(): # run one time
        url = txt.get()
        tims = datetime.now()
        stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Getting URL...')
        c = time.time()
        scrap(url)
        d = time.time()
        tims = datetime.now()
        stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Scrapping...')
        bar['value'] = 100
        messagebox.showinfo('Completed', 'Your data has been saved to C:/ScrapperLogs')
        tims = datetime.now()
        elapsed = d - c
        stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Scrapped to XLSX in {round(elapsed, 2)} sg')

    def loop(): # run more times
        a = True
        url = txt.get()
        sg = combo.get()
        bar['value'] = 100

        # str to int (dic)
        sgdic = {'1min':60, '5min':300, '15min':900, '30min':1800, 
        '1hr':3600, '2hr':7200, '4hr':14400, '8hr':28800, '16hr':57600, 
        '24hr':86400}

        sgs = sgdic[f'{sg}'] # read dic
        messagebox.showinfo('Running', 'Your data is being saved to C:/ScrapperLogs, the program will run on background...')
        tims = datetime.now()
        stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Starting ScrapLoop for {sgs}')
        window.after(0, window.iconify) # minimize window (run in background)
        print(f"[{datetime.now()}] Scrapping on background each {sgs} sg...")
        while a == True:
            tims = datetime.now()
            stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Scrapping...')
            scrap(url)
            msgs = sgs * 1000
            window.after(msgs) # such as time.sleep()
            tims = datetime.now()
            stxt.insert(INSERT,f'\n{tims.strftime("[%X]")} Scrapped')
    
    # threadings
    def threadings():
        ts1=Thread(target=run) # function run
        ts1.start()
    
    def threadings2():
        ts2=Thread(target=loop) # fuction loop
        ts2.start()
    
    # scrolltext
    stxt = scrolledtext.ScrolledText(window,width=35,height=10, font=("Consolas", 9))
    tims = datetime.now()
    stxt.insert(INSERT,f'{tims.strftime("[%X]")} Ready for Scrapping')
    stxt.grid(column=1,row=3)      

    # labels
    lbl = Label(window, text="Scrapper", font=("Verdana", 38))
    lbl.grid(column=0, row=0)
    lbl = Label(window, text="LoopScrap (sg)", font=("Verdana", 10))
    lbl.grid(column=0, row=2)
    lbl = Label(window, text="Link: ", font=("Verdana", 18))
    lbl.grid(column=0, row=1)
    lbl = Label(window, text="", font=("Verdana", 18))
    lbl.grid(column=0, row=0)
    lbl = Label(window, text="", font=("Verdana", 18))
    lbl.grid(column=1, row=0)
    lbl = Label(window, text=" ", font=("Verdana", 18))
    lbl.grid(column=3, row=1)

    # entries
    txt = Entry(window,width=30)
    txt.focus()
    txt.grid(column=1, row=1)

    # progressbar
    bar = Progressbar(window, length=200)
    bar['value'] = 0
    bar.grid(column=4, row=1)

    # combo
    combo = Combobox(window)
    combo['values']= ("1min", "5min", "15min", "30min", "1hr", "2hr", "4hr", "8hr", "16hr", "24hr" )
    combo.current(0)
    combo.grid(column=1, row=2) 

    # butons
    btn = Button(window, text="Run", command=threadings)
    btn.grid(column=2, row=1)
    btn = Button(window, text="RunLoop", command=threadings2)
    btn.grid(column=2, row=2)

    window.mainloop() # close stuff

# threading of main function
def threading(tg1):
    t1=Thread(target=tg1) # function gui
    t1.start()

# mainmenu
def menu():
    mainmenu = int(input("""

  _      _       _            _ _____ _   _  _____                                       
 | |    (_)     | |          | |_   _| \ | |/ ____|                                      
 | |     _ _ __ | | _____  __| | | | |  \| | (___   ___ _ __ __ _ _ __  _ __   ___ _ __  
 | |    | | '_ \| |/ / _ \/ _` | | | | . ` |\___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__| 
 | |____| | | | |   <  __/ (_| |_| |_| |\  |____) | (__| | | (_| | |_) | |_) |  __/ |    
 |______|_|_| |_|_|\_\___|\__,_|_____|_| \_|_____/ \___|_|  \__,_| .__/| .__/ \___|_|    
                                                                 | |   | |               
                                                                 |_|   |_|               

(1).- GUI
(2).- NO GUI
> """))
    if mainmenu == 1: # GUI
        threading(gui)
    else: # NO GUI
        times = int(input("""
(1).- Scrap
(2).- LoopScrap
> """))
        if times == 1: # ONE TIME SCRAP
            url = input("""
Enter URL to Scrap:
> """)
            print(f"[{datetime.now()}] Starting scrapping...")
            for i in tqdm(range(0, 100)): # progressbar
                sleep(0.001)
            print(f"[{datetime.now()}] Scrapping...")
            a = time.time()
            scrap(url.strip())
            b = time.time()
            finaltime = b - a # elapsed time of scrapping
            print(f"[{datetime.now()}] Scrapped to XLSX in {round(finaltime, 4)} sg")
        else: # LOOP SCRAP
            bool = True
            url = input("""
Enter URL to Scrap:
> """)  
            delay = float(input("""
Enter (sg) of ScrapLoop
> """))
            while bool == True:
                print(f"[{datetime.now()}] Starting scrapping...")
                for i in tqdm(range(0, 100)):
                    sleep(0.001)
                print(f"[{datetime.now()}] Scrapping...")
                a = time.time()
                scrap(url.strip())
                b = time.time()
                finaltime = b - a # elapsed time of scrapping
                print(f"[{datetime.now()}] Scrapped to XLSX in {round(finaltime, 4)} sg")
                print(f"[{datetime.now()}] Waiting {delay} seconds...")
                time.sleep(delay)
               

# starting stuff
if __name__ == "__main__":
    menu()





