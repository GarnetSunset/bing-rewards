from bs4 import BeautifulSoup
import lxml.etree as ET
import os
import requests

def redditScrape():

    rssRedditURL = "https://www.reddit.com/r/MicrosoftRewards/search.rss?sort=new&restrict_sr=on&q=flair%3AMail%2BPoints"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    xmlData = requests.get(rssRedditURL, headers=headers).text.encode('utf-8')

    tree = ET.fromstring(xmlData)

    linkList = []

    for content in tree.findall('{http://www.w3.org/2005/Atom}entry/{http://www.w3.org/2005/Atom}content'):
        soup = BeautifulSoup(content.text, "lxml")
        for link in soup.findAll('a'):
            if "aka.ms" in link.get('href') or "e.microsoft" in link.get('href'):
                linkList.append(link.get('href'))

    with open("email_links.txt", 'w') as filehandle:
        for listitem in linkList:
            filehandle.write('%s\n' % listitem)
