import time
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cssselect import GenericTranslator, SelectorError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#Set Up
browser = webdriver.Firefox()
browser.get("https://www.google.com/search?q=site:blogsity.com&oq=site:&aqs=chrome.0.69i59j69i57j69i58j69i65.1577j0j7&sourceid=chrome&ie=UTF-8&pws=0&bav=on.2,or.r_cp.&bvm=bv.108538919,d.eWE&biw=1280&bih=705")
f = open('subHeading.txt', 'w', 0)


for i in range(0, 198):
    #Get List of indexed Sites Titles
    listOfTitles = browser.find_elements_by_xpath(".//*[@id='rso']/div/div/div/div/div/span")

    #Send them to file
    for i in range(0, len(listOfTitles)):
        print listOfTitles[i]
        f.write(listOfTitles[i].text)
        f.write('\n')
    
    #go to new page
    nextButton = browser.find_element_by_xpath(".//*[@id='pnnext']/span[2]")
    nextButton.click()
    time.sleep(3)

    


'''
def check_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
        

f1 = open('CommonFirstNames.txt', 'r+')
names = []
j = 0

while True:
    line = f1.readline()
    if not line: break
    line = line.rstrip('\n')
    names.append(line)

for i in range(len(names)):
    print j
    print names[i]
    print str(names[i])
    j = j+1


f = open('emails.txt', 'w', 0)

for number in range(0, len(names)):

    browser.get('http://directory.unm.edu/index.php')

    select = browser.find_element_by_xpath("/html/body/div[@id='page']/div[@id='container']/div[@id='content']/div[@class='content']/div[@id='after_default_1']/div[@class='dir-search-box-wrapper']/div[@class='search-form']/form[@id='dirsearch']/fieldset/div/label[3]")
    select.click()

    select2 = browser.find_element_by_xpath("/html/body/div[@id='page']/div[@id='container']/div[@id='content']/div[@class='content']/div[@id='after_default_1']/div[@class='dir-search-box-wrapper']/div[@class='search-form']/form[@id='dirsearch']/p[1]/input[@id='name']")
    select2.send_keys(names[number] + '\n')

    linksElements = browser.find_elements_by_tag_name('a')

    for i in range(0, len(linksElements)):
        print linksElements[i].text
        if ( '@' in linksElements[i].text ):
            f.write(linksElements[i].text + '\n')

number += 1

'''



'''
-----------------

while (level[j] != "X"):

    i = 2
    letter = 0
    select = Select(browser.find_element_by_id('id_tamuEduPersonClassification'))
    select.select_by_value(level[j])

    while (letter <= len(names)):

        element = browser.find_element_by_xpath('.//*[@id="id_givenName"]')
            element.send_keys(names[letter])
        select = Select(browser.find_element_by_id('id_tamuEduPersonClassification'))

            select.select_by_value(level[j])

            element = browser.find_element_by_xpath('.//*[@id="contentBox"]/form/button')
        element.click()
        letter += 1

        while (i <= 51):

            if (check_xpath(".//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[1]/a") == True):

                element = browser.find_element_by_xpath(".//*[@id='resultsTable']/tbody/tr["+str(i)+"]/td[1]/a")
                element.click()

                if (check_xpath("//*[@id='contentBox']//a[contains(@href, 'mailto')]") == True):
                    element = browser.find_element_by_xpath("//*[@id='contentBox']//a[contains(@href, 'mailto')]")
                                print element.text
                    f.write(element.text)
                    f.write('\n')

                browser.back()

                i += 1
            else:
                i = 52
        browser.back()
        i = 2
    j += 1
    letter = 0


    
f.close()
'''
