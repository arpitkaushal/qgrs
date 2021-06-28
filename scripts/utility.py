from selenium import webdriver  # selenium webdriver
import os
from pathlib import Path


def newdriver(browser,dir_path):
    # launch webdriver
    browserdriver = str(Path(dir_path).parents[0]) + '\\webdrivers\\' + browser + 'driver.exe'
    print(browserdriver)
    if(browser=="chrome"):
        return webdriver.Chrome(browserdriver)
    if(browser=="msedge"):
        return webdriver.Edge(browserdriver)
    if(browser=="gecko"):
        return webdriver.Firefox()
        """ if firefox.exe not found in default location 
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.binary_location = r'C:\\Users\\IITGN\AppData\\Local\\Mozilla Firefox\\firefox.exe'
        return webdriver.Firefox(options=options)
        """
    if(browser=="safari"):
        return webdriver.Safari()
