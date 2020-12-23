from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/about")
def aboutSection():
    return render_template("about.html")


# app.run(port=9000, debug=True)
