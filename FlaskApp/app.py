#main application to run the soundboard
#run and point browser to localhost:5000

from flask import Flask, render_template

app = Flask(__name__)
app_title = "Dingies Club"
author = "Tones"

#only one page, all on index
@app.route("/")
def main():
	#passing to index
	return render_template("index.html", author=author)

#about page
@app.route("/about")
def about():
	return render_template("about.html", app_title="About", author=author)

if __name__ == "__main__":
	app.run(debug=True)