# coding=utf-8
from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
import json
import requests
AU_ENDPOINT = 'http://0.0.0.0:2000'
AT_ENDPOINT = 'http://0.0.0.0:3000'
RE_ENDPOINT = 'http://0.0.0.0:4000'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (default)"

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        
        url = AU_ENDPOINT # define end-point

        params = {'test' : 'test'}
        data = requests.get(url, params = params)
        data = data.json()
        
        if data['status'] == 'approved':
            url = AT_ENDPOINT # define end-point
            params = {'test' : 'test'}
            data = requests.get(url, params = params)
            data = data.json()
            return data['test']
        else:
            return '', 404

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
