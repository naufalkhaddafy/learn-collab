from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Namaku Nuril dan gondrong aku ganteng asli dan original tapi boong. Gue Gondrong sayang Ditha lho</p>"

