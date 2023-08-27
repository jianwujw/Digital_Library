import requests
import json
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *

def createJSON(root,dir,modifyDir):
    url = 'https://openlibrary.org/search'

    driver = webdriver.Chrome()
    driver.get(url)
    findInput = driver.find_element('name','q')
    findInput.send_keys(str(modifyDir))
    findInput.send_keys(Keys.ENTER)

    books = None
    work_title = None
    pages = None
    publish_date = None
    subject_list = None
    authors = None

    try:
        books = driver.find_element(By.CLASS_NAME,'results')
        if books:
            ActionChains(driver)\
                .click(books)\
                .perform()
    except ElementNotInteractableException as e:
        print(e)
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchWindowException as e2:
        print(e2)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)

    currentURL = driver.current_url   
    html = requests.get(currentURL)
    soup = BeautifulSoup(html.content, 'html.parser')

    try:
        work_title = soup.find(attrs={'class':'work-title'})
        if work_title != None:
            work_title = work_title.text
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)


    try:
        publisher = soup.find(attrs={'itemprop':'publisher'})
        if publisher != None:
            publisher = publisher.text
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)

    try:
        pages = soup.find(attrs={'itemprop':'numberOfPages'})
        if pages != None:
            pages = pages.text
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)

    try:
        publish_date = soup.find(attrs={'itemprop':'datePublished'})
        if publish_date != None:
            publish_date = publish_date.text    
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)

    try:
        subjects = soup.findAll(attrs={'data-ol-link-track':'BookOverview|SubjectClick'})
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5)

    try:
        authors = soup.findAll(attrs = {'data-ol-link-track':'BookOverview|SubjectPeopleClick'})
    except InvalidArgumentException as e1:
        print(e1)
    except NoSuchAttributeException as e3:
        print(e3)
    except NoSuchElementException as e4:
        print(e4)
    except AttributeError as e5:
        print(e5) 


    subject_list =[]
    for subject in subjects:
        if subject != None:
            subject_list.append(subject.text)       
    author_list =[]
    for author in authors:
        if author != None:
            author_list.append(author.text)

    url_dict = {
        'work_title':work_title,
        'publisher': publisher,
        'pages': pages,
        'publish_date': publish_date,
        'subjects' : subject_list,
        'authors': author_list
    }
    filename = 'content.json'
    output_file = open(os.path.join(root,dir,filename),'w')
    json.dump(url_dict,output_file)





path = 'static/BOOK/onlineBooks/convertJPG'
bookDict = {}
num = 0
for root, dirs, files in os.walk(path):  

    for dir in dirs:
        print(dir)
        modifyDir = dir.replace('[',"").replace(']',"").replace('_', " ").replace('-'," ")
        imagesArray = []
        infoDict = {}
        file_json = "content.json"
        for files in os.listdir(os.path.join(root,dir)): 
            if os.path.isfile(os.path.join(root,dir,file_json)):
                continue
            else:               
                createJSON(root,dir, modifyDir) 










# url = 'https://openlibrary.org/search'

# driver = webdriver.Chrome()
# driver.get(url)
# findInput = driver.find_element('name','q')
# findInput.send_keys('huckleberry')
# findInput.send_keys(Keys.ENTER)

# books = None
# work_title = None
# pages = None
# publish_date = None
# subject_list = None
# authors = None

# try:
#     books = driver.find_element(By.CLASS_NAME,'results')
#     if books:
#         ActionChains(driver)\
#             .click(books)\
#             .perform()
# except ElementNotInteractableException as e:
#     print(e)
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchWindowException as e2:
#     print(e2)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)

# currentURL = driver.current_url   
# html = requests.get(currentURL)
# soup = BeautifulSoup(html.content, 'html.parser')

# try:
#     work_title = soup.find(attrs={'class':'work-title'})
#     if work_title != None:
#         work_title = work_title.text
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)


# try:
#     publisher = soup.find(attrs={'itemprop':'publisher'})
#     if publisher != None:
#         publisher = publisher.text
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)

# try:
#     pages = soup.find(attrs={'itemprop':'numberOfPages'})
#     if pages != None:
#         pages = pages.text
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)

# try:
#     publish_date = soup.find(attrs={'itemprop':'datePublished'})
#     if publish_date != None:
#         publish_date = publish_date.text    
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)

# try:
#     subjects = soup.findAll(attrs={'data-ol-link-track':'BookOverview|SubjectClick'})
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5)

# try:
#     authors = soup.findAll(attrs = {'data-ol-link-track':'BookOverview|SubjectPeopleClick'})
# except InvalidArgumentException as e1:
#     print(e1)
# except NoSuchAttributeException as e3:
#     print(e3)
# except NoSuchElementException as e4:
#     print(e4)
# except AttributeError as e5:
#     print(e5) 


# subject_list =[]
# for subject in subjects:
#     if subject != None:
#         subject_list.append(subject.text)       
# author_list =[]
# for author in authors:
#     if author != None:
#         author_list.append(author.text)

# url_dict = {
#     'work_title':work_title,
#     'publisher': publisher,
#     'pages': pages,
#     'publish_date': publish_date,
#     'subjects' : subject_list,
#     'authors': author_list
# }
# output_file = open('content.json','w')
# json.dump(url_dict,output_file)