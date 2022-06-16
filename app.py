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
            'format': 'json'
            }
        
        try:
            response = requests.get(ENV['URL_ISS'], params=data)
        except Exception as e:
            raise e

        lat = response.json()['iss_position']['latitude']
        lon = response.json()['iss_position']['longitude']
        # results['timestamp'] = response.json()['timestamp']
        results['latitude'] = lat
        results['longitude'] = lon

        lat, lon

        return render_template("iss.html", **results)
    return render_template("iss.html")

@server.route('/get_coor', methods = ['GET', 'POST'])

def get_coor():
    if request.method == 'POST':

        results = {}
        results['address'] = request.form['address']

        data = {
        'key': ENV['PRIVATE_TOKEN'],
        'q': results['address'],
        'format': 'json'
        }
        try:
            response = requests.get(ENV['URL'], params=data)
        except Exception as e:
            raise e

        lat = response.json()[0]['lat']
        lon = response.json()[0]['lon']

        results['lat'] = lat
        results['lon'] = lon
        
        lat, lon
        # return lat, lon
        return render_template("get_coor.html", **results)
    return render_template("get_coor.html")


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