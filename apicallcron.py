from flask import Flask
import urllib.request, json
import ssl
import os

def get_price():
    str1 = 'You have Entered' + ' ' + str(object)
    req = urllib.request.Request(
        'https://metals-api.com/api/latest?access_key=xj4bhpuu9lgv5ba2dmflzsg6j1unblapb5sqzqrg139tnb6n9085juf3w526',
        data=None,
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0'
            }
    )
    gcontext = ssl.SSLContext()
    response = urllib.request.urlopen(req, context= gcontext)
    data = json.loads(response.read())
    return data

my_data = get_price()
#print(my_data)

with open(os.path.dirname(os.path.realpath(__file__)) + '/latest_data.txt', 'w') as f:
    f.write(json.dumps(my_data))