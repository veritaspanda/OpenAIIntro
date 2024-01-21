from flask import Flask
#import random, threading, webbrowser
#import startFlaskApp

app = Flask(__name__)



@app.route('/')
def scrape_and_reformat(html = "<html><body> ... generated html string ... </body></html>"):
    # call your scraping code here
    #return '<html><body> ... generated html string ... </body></html>'

    return html

#if __name__ == '__main__':
#    app.run()

if __name__ == 'basicFlaskHtmlPage':
    app.run(port=8090,host="localhost",debug=False)
     #appUpdated = startFlaskApp.startFlaskApp(app)
elif __name__ == 'main':
    app.run(port=8090,host="localhost",debug=True)
    #startFlaskApp.startFlaskApp(app)
elif __name__ == '__main__':
    app.run(port=8090,host="localhost",debug=False)
    #startFlaskApp.startFlaskApp(app)