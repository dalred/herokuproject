from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def image():
    return render_template('test.html')


if __name__ == "__main__":
    app.run()
