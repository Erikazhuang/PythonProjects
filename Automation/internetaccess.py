from urllib.request import urlopen
import textwrap
from bs4 import BeautifulSoup

def textFromHtmlId(url, htmlId, textWidth):
    """ download text of html id from web site, reformat text content and set width of line to textWidth
    >>> print(textFromWeb('https://www.quotev.com/story/13902911/%E9%B8%A3%E5%BB%8A/5','rescontent')[:3])
     阳光
    """
    stringresponse = getTextFromUrl(url) #https://www.gutenberg.org/files/1661/1661-0.txt
    #print(textwrap.fill(stringresponse,width=100))

    #get div id = 'rescontent' from html 
    soup = BeautifulSoup(stringresponse,features='html.parser')
    content =  soup.find(id=htmlId).getText()
    formatedcontent = textwrap.fill(content,width = textWidth)
    return(formatedcontent)


def getTextFromUrl(url):
    fullString =""
    with urlopen(url) as response:
        for line in response:
            try:
                line = line.decode("utf-8") #convert bityes to a str
                fullString += line.rstrip()
            except Exception as err:
                print('error: ' + str(err))
                continue

    return fullString