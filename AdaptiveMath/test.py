from urllib import request
from bs4 import BeautifulSoup
import csv 

htmlpage = request.urlopen("file:///C:/Users/44792/Downloads/IXL%20-%20Year%206%20maths%20practice.html").read()
soup = BeautifulSoup(htmlpage,features="html.parser")

catCounter=0
skillCounter= 0

with open('skill.csv','w',newline='') as myfile:
    wr = csv.writer(myfile)
    for div in soup.find_all("div",class_='skill-tree-category'):
        header = div.find("h2",class_='skill-tree-skills-header')
        catCounter +=1
        for line in div.find_all("a",class_="skill-tree-skill-link"):
            skillCounter +=1
            row = (line.text.strip(),catCounter,header.text.strip())
            wr.writerow(row)


    