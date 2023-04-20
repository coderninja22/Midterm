import pytest
import requests
from app import *
url = 'http://127.0.0.1:5000/calculate?val1=1000&val2=4000'
response = requests.get(url)
sum = int(response.text)
assert sum == 5000

