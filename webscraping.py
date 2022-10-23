from bs4 import BeautifulSoup as bs
import requests 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("What is the ticker")
ticker = input()

link = "https://www.cnbc.com/quotes/" + ticker + "?tab=news"

print(link)

response = requests.get(link) #gets link
html = response.content #gets html content of link
soup = bs(html, 'lxml') #creates soup object

links = []

for a in soup.findAll('a', class_= "LatestNews-headline"):
    links.append(a['href'])

print(links)

keywords = ["continue","recession","severe","jump"]
keywordCounter = 0

for articleLink in links:
    responseLink = requests.get(articleLink)
    htmlNew = responseLink.content
    soupNew = bs(htmlNew, 'lxml')
    #redo process above for scraping for each article link
    for p in soupNew.findAll('p'):
        paragraph = str(p)
        for keyword in keywords:
            if keyword in paragraph:
                keywordCounter += 1

if (len(links) < 3):
    print("Not enough sources for this stock to make a reasonable judgement, sorry!")
else: 
    print(keywordCounter) #should be 4


