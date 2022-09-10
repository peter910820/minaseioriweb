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

@app.route("/about", methods=['GET'])
def about_page():
    return render_template("/about.html")

@app.route('/article/<title>')
def article(title):
    return render_template(f"/article/{title}.html")

if __name__ == "__main__":
    app.run()