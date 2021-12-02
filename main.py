from flask import Flask


app = Flask(__name__)

@app.route("/")
def page_index():
    return "Hello world4 and llalala"


if __name__ == "__main__":
    app.run()
