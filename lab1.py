import requests
import urllib.request
print(requests.__version__)

url = "http://google.com/"
r= requests.get(url)
print(r)