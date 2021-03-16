from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('./index.html')

app.run()
