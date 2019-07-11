#main application to run the soundboard
#run and point browser to localhost:5000

from flask import Flask, render_template, request, redirect, g
import sqlite3
import os, sys

app = Flask(__name__)
app_title = "Dingies Club"
author = "Booty Gang"

#only one page, all on index
@app.route("/")
def main():
	#passing to index
	return render_template("index.html", app_title=app_title, author=author)


if __name__ == "__main__":
	app.run(debug=False)