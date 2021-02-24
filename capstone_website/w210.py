from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd
import os
import numpy as np
import sys
from flask import request

# Embed for Typeform
#import * as typeformEmbed from '@typeform/embed'

APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/product")
def summary():
    return render_template("product.html")


@app.route("/process")
def segment():
    return render_template("process.html")


@app.route("/people")
def score():
    return render_template("people.html")   

# Main
if __name__ == "__main__":
  port = 80
  if len(sys.argv[1:]) > 0:
    port = sys.argv[1]

  app.run(host="0.0.0.0", port=port)


