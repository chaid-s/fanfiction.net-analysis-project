#Story ID finder

from bs4 import BeautifulSoup
from fanfiction import Scraper
import csv
import time
import requests
import copy

def getPageIds(url):

    r = requests.get(url)

    ids = [] #List of Story IDs

    soup = BeautifulSoup(r.content, 'html5lib') 

    table = soup.find_all("a", {"class":'stitle'})

    for table in table:
        start  ="/s/"
        end = "/1/"
        string=table.get('href')
        ids.append(string[string.find(start)+len(start):string.rfind(end)])

    return ids

def getSourceMaterialIds(section, sourceMaterial):

    pageNumber=1

    idList=[]

    while True:

        urlPreString = ("https://www.fanfiction.net/"+section+"/"+
        sourceMaterial+"/"+"?&srt=1&r=10&p="+str(pageNumber))

        idBuffer = getPageIds(urlPreString)

        pageNumber = pageNumber + 1

        if not idBuffer:

            break
        else:
            idList=idList+idBuffer

    return idList

def scrapeMetaData(ids):

    idList=ids

    metadata =[]

    scraper = Scraper()
    
    for i in idList:
        metadata.append(scraper.scrape_story_metadata(i))

    return metadata

table = getSourceMaterialIds("game","Gunz-The-Duel")

metadata = scrapeMetaData(table)

print(metadata)

with open('idCSV.txt', 'w') as myfile:
    wr = csv.DictWriter(myfile, fieldnames=['id', 'canon_type',
                'canon','author_id', 'title', 'updated', 'published',
                'lang','genres'],extrasaction='ignore')
    wr.writeheader()
    wr.writerows(metadata)


