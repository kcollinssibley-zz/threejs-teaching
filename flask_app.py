import argparse
import os
import socket
import sys

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/cubemap')
def cubemap():
    return render_template('cubemap.html')

@app.route('/stage')
def stage():
    return render_template('stage.html')

app.run()
