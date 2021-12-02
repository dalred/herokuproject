from flask import Flask, render_template, url_for
import dropbox

dbx = dropbox.Dropbox('sl.A9dta5WjJhb9MrvaQIxJ4Jm8ZUjUb72j_SdWnul9_9lJXtwd598Fki7r5xnxD47Mw7y1vwTl6Zn6B_1gfQ7U9fQdDpgC0h7iujnMrKklirgSp7lWilp7BzhNwCDtQFOF0CkOoUzozEb1')

app = Flask(__name__)
link = dbx.files_get_temporary_link('/myfile.jpg').link
@app.route("/")
def image():
    return render_template('test.html', link=link)


if __name__ == "__main__":
    app.run()
