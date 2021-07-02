from selenium import webdriver  # selenium webdriver
import os
from pathlib import Path
import requests
from selenium.webdriver.support.ui import Select
import time

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


def getseq(NCBI_ID):
    reqUrl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="+NCBI_ID+"&rettype=fasta&retmode=text"
    response = requests.request("GET", reqUrl)
    return "".join(response.text.split("\n")[1:])


def getGcount(driver,NCBI_ID):
    
    driver.get("https://bioinformatics.ramapo.edu/QGRS/analyze.php")
    Select(driver.find_element_by_name("QGRSmax")).select_by_visible_text("45")
    driver.find_element_by_name("sequence").send_keys(getseq(NCBI_ID))
    driver.find_element_by_xpath("//input[@value='Analyze']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//img[@src='data.gif']").click()

    # switch tab
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # count how many 2G,3G and 4G sequences present
    gees = [0,0,0]
    i = 2
    while True:
        try:
            entry = driver.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[3]/b/u").text
            gees[len(entry)-2]+=1
            # print(entry)
            i+=1
        except:
            break
    
    print("Result for",NCBI_ID)
    for i in range(len(gees)):
        print("No. of "+str(i+2)+"G PQS :",gees[i])

    return gees


def getGcountMultiple(driver, IDs):
    
    driver.get("https://bioinformatics.ramapo.edu/QGRS/analyze.php")
    Select(driver.find_element_by_name("QGRSmax")).select_by_visible_text("45")
    
    for id in IDs:
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath("//a[@href='analyze.php']").click()
        time.sleep(2)

        driver.find_element_by_name("sequence").clear()
        driver.find_element_by_name("sequence").send_keys(getseq(id))
        driver.find_element_by_xpath("//input[@value='Analyze']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//img[@src='data.gif']").click()
        
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)

        gees = [0,0,0]
        i = 2
        while True:
            try:
                entry = driver.find_element_by_xpath("//table/tbody/tr["+str(i)+"]/td[3]/b/u").text
                gees[len(entry)-2]+=1
                # print(entry)
                i+=1
            except:
                break
        
        print("Result for",id)
        for i in range(len(gees)):
            print("No. of "+str(i+2)+"G PQS :",gees[i])

        driver.close()
    
    return IDs