import os
from urllib import response
from dotenv import dotenv_values
import requests
from flask import Flask, render_template, request


server = Flask(__name__)

ENV = dotenv_values()

@server.route('/iss', methods = ['GET', 'POST'])

def iss():
    if request.method == 'GET':
        
        results = {}


        data = {
            'message': 'success',
            }
        
        try:
            response = requests.get(ENV['URL_ISS'], params=data)
        except Exception as e:
            raise e

        results['latitude'] = response.json()['iss_position']['latitude']
        results['longitude'] = response.json()['iss_position']['longitude']
        results['timestamp'] = response.json()['timestamp']

        return render_template("iss.html", **results)
    return render_template("iss.html")

@server.route('/', methods = ['GET', 'POST'])

def index():

    if request.method == 'POST':

        results = {}
        results['lat'] = request.form["lat"]
        results['lon'] = request.form["lon"]

        data = {
        'key': ENV['PRIVATE_TOKEN'],
        'lat': results['lat'],
        'lon': results['lon'],
        'format': 'json'
        }
        try:
            response = requests.get(ENV['URL_REVERSE'], params=data)
        except Exception as e:
            raise e

        results['address'] = response.json()['address']

        # return render_template("results.html", **results)
        return render_template("index.html", **results)
    return render_template("index.html")

if __name__ == '__main__':
    server.run(host=ENV['HOST'], port=ENV['PORT'], debug = True) 