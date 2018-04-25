# coding=utf-8
from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
import requests
import json
AU_ENDPOINT = 'http://0.0.0.0:2000'
AT_ENDPOINT = 'http://0.0.0.0:3000'
RE_ENDPOINT = 'http://0.0.0.0:4000'

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        
        url = RE_ENDPOINT # define end-point

        params = {'test' : 'test'}
        data = requests.get(url, params = params)
        data = data.json()
        if data['status'] == 'approved':
            return jsonify({'status': 'approved', 'test': data['test']})
        else:
            return jsonify({'status': 'failed'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)