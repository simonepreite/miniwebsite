from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/_consegne_vaccini')
def consenge_vaccini():
    fd = open("../covid19-opendata-vaccini/dati/consegne-vaccini-latest.json")
    dati = json.load(fd)
    fd.close()
    print (dati["data"][0])
    return jsonify(dati["data"][0])


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('./index.html')

app.run()
