import flask
from flask import Flask
import json
import requests
import os

app = Flask(__name__)
@app.route('/',methods=['GET'])

def meteo() :
    url = "http://api.openweathermap.org/data/2.5/weather?"
    env = os.environ
    api_key = env['API_KEY']
    lat = flask.request.args.get("latitude")
    lon = flask.request.args.get("longitude")
    url = url + "latitude = " + lat + "& longitude = " + lon + "& appid = " + api_key
    res = requests.get(url)
    data = json.loads(res.text)
    return data

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 8081, debug = True)