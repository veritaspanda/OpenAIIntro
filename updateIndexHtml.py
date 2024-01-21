import os
import webbrowser

newTab = 2 # open in a new tab, if possible


#html = '<html> ...  generated html string ...</html>'
path = os.path.abspath('index.html')
url = 'file:///' + path

def updateHtml(html):
    try:
        with open(path, 'w') as f:
            f.write(html)
            f.close()
            webbrowser.open_new_tab(path)
    except:
        print("An error occured opening browser or displaying the html")