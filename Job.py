import time
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cssselect import GenericTranslator, SelectorError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains
from random import *
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf-8')


global browser


def launchBrowser():
    print "Start: launchBrowser"
    global browser
    browser = webdriver.Firefox()
    browser.implicitly_wait(1)
    browser.get('https://google.com/search?num=100&espv=2&q=houston+lawyers')
    print "End: launch Browser"



def recordLinksToFile():
    print "Start: recordLinksToFile"
    f = open('subHeading.txt', 'w', 0)
    listOfTitles = browser.find_elements_by_xpath("/html/body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@class='mw'][2]/div[@id='rcnt']/div[@class='col'][1]/div[@id='center_col']/div[@id='res']/div[@id='search']/div/div[@id='ires']/div[@id='rso']/div[@class='_NId']/div[@class='srg']/div[@class='g']/div[@class='rc']/h3[@class='r']/a")
    for i in range(0, len(listOfTitles)):
        print listOfTitles[i]
        f.write(listOfTitles[i].text)
        f.write('\n')
    print "End: recordLinksToFile"




def begin():
    launchBrowser()
    recordLinksToFile()        

#-----START PROGRAM -----

begin()
    
































