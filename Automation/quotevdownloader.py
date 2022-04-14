
import internetaccess as net
import codecs



#download all chapters
def downloadall(url,htmlId,startpage, endpage):
    for i in range(startpage,endpage):
        try:
            articletext = net.textFromHtmlId(f'{url}/{i}',htmlId,100)
            #write download text to file
            filename = f'{i}.txt'
            with codecs.open(filename,'w','utf-8') as f:
                f.write(articletext)
                f.close()
            
        except Exception as err:
            continue
            


#combine all text files into one
def combinefiles(startpage, endpage):
    onefile =''
    for i in range(startpage,endpage):
        filename = f'{i}.txt'
        with open(filename,encoding="utf-8") as f:
            data = f.read()
            onefile += data

    with codecs.open('all.txt','w','utf-8') as fone:
        fone.write(onefile)
        fone.close()

if __name__=='__main__':
    booklink = 'https://www.quotev.com/story/14770488/%E4%B8%9A%E7%81%AB'
    htmlid = 'rescontent'
    startpage = 1
    endpage = 60 #last page + 1
    downloadall(booklink,htmlid,startpage,endpage)
    combinefiles(startpage, endpage)


def test():
    articletext = textFromWeb('https://www.quotev.com/story/13482881/%E5%B9%BA%E5%84%BF/6','rescontent',100)[:100]
    filename = f'1.txt'
    with codecs.open(filename,'w+','utf-8') as f:
        f.write(articletext)
        f.close()