import os
from flask import Flask
import socket
import logging

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    app.logger.info('Main page')
    return "Hello, world!"