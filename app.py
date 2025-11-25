from flask import Flask, request, render_template, redirect
# import requests
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()
webhook = os.getenv('webhook_url')

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/camp')
def camp():
    # return render_template('camp.html')
    return redirect('https://camp.tayari.live')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)