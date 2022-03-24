#main application to run the soundboard
#run and point browser to localhost:5000

from flask import Flask, render_template, url_for

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

app = Flask(__name__)
app_title = "Dingies Club"
author = "Tones"

#only one page, all on index
@app.route("/")
def main():
	#passing to index
	return render_template("index.html", author=author, posts=posts)

#about page
@app.route("/about")
def about():
	return render_template("about.html", app_title="About", author=author)

if __name__ == "__main__":
    # the host part is so that I can run access it from phone on same network
	app.run(debug=True, host="0.0.0.0")