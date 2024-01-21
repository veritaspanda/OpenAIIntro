import os
import webbrowser

#html = '<html> ...  generated html string ...</html>'
path = os.path.abspath('temp.html')
url = 'file://' + path

def openHtml(html):
    try:
        with open(path, 'w') as f:
            f.write(html)
            f.close()
            webbrowser.open(path)
    except:
        print("An error occured opening browser or displaying the html")