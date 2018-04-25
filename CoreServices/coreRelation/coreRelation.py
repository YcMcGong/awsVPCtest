# coding=utf-8
from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
import requests
AU_ENDPOINT = 'http://0.0.0.0:2000'
AT_ENDPOINT = 'http://0.0.0.0:3000'
RE_ENDPOINT = 'http://0.0.0.0:4000'

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        
        return jsonify({'status': 'approved', 'test': 'Michael'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 4000)