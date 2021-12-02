from flask import Flask


app = Flask(__name__)

@app.route("/")
def page_index():
    return "Привет Анютка"


if __name__ == "__main__":
    app.run()
