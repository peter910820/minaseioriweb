from flask import Flask
from flask import render_template

import os

app = Flask(__name__)

# 網頁端 #
@app.route("/", methods=['GET'])
def home_page():
    return render_template("index.html")

@app.route("/note", methods=['GET'])
def note_page():
    return render_template("note.html")

@app.route("/article", methods=['GET'])
def article_page():
    return render_template("article.html")

@app.route("/article/0810_PJSK", methods=['GET'])
def article_0810_PJSK():
    return render_template("/article/0810_PJSK.html")

@app.route("/article/0817_TenkafuMA", methods=['GET'])
def article_0817_TenkafuMA():
    return render_template("/article/0817_TenkafuMA.html")

if __name__ == "__main__":
    app.run()