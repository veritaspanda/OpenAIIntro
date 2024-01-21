import os
import webbrowser
#import basicFlaskHtmlPage

newTab = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
#url = "http://docs.python.org/library/webbrowser.html"
#webbrowser.open(url,new=newTab)

# open an HTML file on my own (Windows) computer
#urlFileHardCode = "file:///C:/Users/Chris/GIT/OpenAIIntro/index.html"
#webbrowser.open(url,new=newTab)

#html = '<html> ...  generated html string ...</html>'
path = os.path.abspath('index.html') #file:///C:/Users/Chris/GIT/OpenAIIntro/index.html
#path1 = os.getcwd()
#path = os.path.realpath('index.html')
url = 'file:///' + path
#url1 = 'file:///' + path1 + '/' + 'index.html'

def updateHtml(html):
    try:
        with open(path, 'w') as f:
            f.write(html)
            f.close()
            #webbrowser.open(path)
            #urlToUse = 'file:///' + os.getcwd() + '\\' + 'index.html'
            #urlToUse = 'file:///' + os.path.abspath('index.html')
            webbrowser.open_new_tab(path)
            #webbrowser.open(urlFileHardCode,new=newTab)
            #basicFlaskHtmlPage.scrape_and_reformat(html=html)
    except:
        print("An error occured opening browser or displaying the html")