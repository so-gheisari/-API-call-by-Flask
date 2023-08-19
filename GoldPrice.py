from flask import Flask
import json, urllib
import os
from flask import jsonify
from flask import Response

appliction = Flask(__name__)
 
@appliction.route('/show/<object>')
def show_price(object):
    str1 = 'You have Entered' + ' ' + str(object)
    data = {}
    response = {}
    print(os.path.dirname(os.path.realpath(__file__)))
    with open(os.path.dirname(os.path.realpath(__file__)) + '/latest_data.txt', 'r') as f:
        data = json.loads(f.read())
    if object == 'gold':
        response['data'] = str(data['rates']['XAU'])
        response['success'] = True
    elif object == 'silver':
        response['data'] =  str(data['rates']['XAG'])
        response['success'] = True
    else:
        response['data'] = ''
        response['success'] = False
    
    return jsonify(response)

@appliction.route('/')
def wellcome():
    response = '<root><data>0.00053530324929072</data><success>True</success></root>' 
    return Response(response, mimetype='text/xml')

if __name__ == '__main__':
    appliction.run(host= '0.0.0.0', port=80)