from flask import Flask, jsonify, request
import startFlaskApp

app = Flask(__name__, static_folder='app', static_url_path="/app")

def setHtml(html="<html><body> ... setting html string ... </body></html>"):
    return html

indexHtml = setHtml()

@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})

@app.route("/index")
def index():
    return jsonify({"status": "healthy"})


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
    if app is None:
        print(str(path))
        return jsonify({"status": "Nothing Here"})
    else:
        print(str(app.route))
        print(str(path))
        #startFlaskApp.startFlaskApp(app)
        # app.send_static_file("index.html")
        return indexHtml

if __name__ == '__main__':
    app.run(port=8090,host="localhost",debug=False)
elif __name__ == 'singlePageFlask':
    app.run(port=8090,host="localhost",debug=False)