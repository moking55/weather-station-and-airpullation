
from flask import Flask, render_template, request 
import sys,time
from datetime import datetime
# import json to load JSON data to a python dictionary 
import json 
  
# urllib.request to make a request to api 
import urllib.request 
  
  
app = Flask(__name__) 
  
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city']
    else: 
        # for default name mathura 
        city = 'lamphun'
     # your API key will come here 
    api = '11c0d3dc6093f7442898ee49d2430d20'
     # source contain json data from api 
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api + '&units=metric').read()
     # converting JSON data to a dictionary 
    list_of_data = json.loads(source) 
     # data for variable list_of_data 
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "temp_min": str(list_of_data["main"]["temp_min"]),
        "temp_max": str(list_of_data["main"]["temp_max"]),
        "temp": str(list_of_data['main']['temp']), 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']),
        "sunrise": str(datetime.fromtimestamp(list_of_data["sys"]["sunrise"]).strftime('%H:%M:%S')),
        "sunset": str(datetime.fromtimestamp(list_of_data["sys"]["sunset"]).strftime('%H:%M:%S'))
    } 
    print(data) 
    return render_template('index.html', data = data) 
  
  
if __name__ == '__main__': 
    app.run(debug = True) 
