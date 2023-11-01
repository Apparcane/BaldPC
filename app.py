from flask import Flask, render_template, url_for
import requests

SID = "oe2jhn59pl8gnu6sk2fj6o6o76"


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)