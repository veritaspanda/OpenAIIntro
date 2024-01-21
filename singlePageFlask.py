from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})

@app.route("/")
def index():
    return app.render_template('index.html')


if __name__ == '__main__':
    app.run(port=8090,host="localhost",debug=False)
elif __name__ == 'singlePageFlask':
    app.run(port=8090,host="localhost",debug=False)