# -*- coding: utf-8 -*-
import os
from flask import Flask

# flask
app = Flask(__name__, static_folder='static')


@app.route('/')
def hello():
    name = "Hello World"
    return name

# main
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), port=os.getenv("APP_PORT", 3000))
