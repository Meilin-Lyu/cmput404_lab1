import requests
import urllib.request
print(requests.__version__)

url = "http://google.com/"
r= requests.get(url)
print(r)

url1 = 'https://raw.githubusercontent.com/Meilin-Lyu/cmput404_lab1/main/lab1.py'
urllib.request.urlretrieve(url1,"lab1_m.py")
f=open("lab1_m.py") 
content = f.read()                 
print(content)                       
f.close()