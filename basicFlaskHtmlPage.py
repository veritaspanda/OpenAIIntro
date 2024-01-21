from flask import Flask

app = Flask(__name__)



@app.route('/')
def scrape_and_reformat(html = "<html><body> ... generated html string ... </body></html>"):
    # call your scraping code here
    #return '<html><body> ... generated html string ... </body></html>'

    return html

if __name__ == '__main__':
   app.run(port=8090,host="localhost",debug=False)
