import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return "Test"
    
@app.route('/test')
def test():
    value1 = Flask.request.args.get('val1')
    value2 = Flask.request.args.get('val2')
    return "Test Results:" + value1 + value2

    
'''
@app.route('/', methods=['GET', 'POST'])
def home():
   return Flask.render_template('index.html')

@app.route('/get_numbers')
def get_values():
   value1 = Flask.request.args.get('val1')
   value2 = Flask.request.args.get('val2')
   return Flask.jsonify({'data':f'<p>The result is: {value1+value2}</p>'})



'''
