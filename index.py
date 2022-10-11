from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Namaku Nuril dan aku ganteng asli bangget dan original</p>"
