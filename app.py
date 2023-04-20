import codecs
from flask import Flask, redirect, url_for, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods = ['POST','GET'])
def hello():
    return open("index.html", 'r')

@app.route('/calculate', methods = ['POST','GET'])
def calculate():
    val1 = request.args.get('val1')
    val2 = request.args.get('val2')
    sum = int(val1) + int(val2)
    return str(sum)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)