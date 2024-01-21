from flask import Flask
import random, threading, webbrowser

#app = Flask(__name__)


def startFlaskApp(app):
    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)
    print("Port: " + str(port) + " url: " + url)
    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run(port=port, debug=False)
    return

def sendStaticFile(app):
    startFlaskApp(app)
    app.send_static_file("index.html")
    return