from flask import Flask
from flask import render_template
# from decouple import config

# API_USERNAME = config('USER')
# API_KEY = config('KEY')
print(API_KEY)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/about")
def aboutSection():
    return render_template("about.html")
# @app.route("/trial")
# def trial():
#     return (f"{API_KEY}")


# app.run(port=9000, debug=True)
