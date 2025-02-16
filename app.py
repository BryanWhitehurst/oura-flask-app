from flask import Flask, jsonify
from datetime import date
from datetime import timedelta
import requests 
import json

app = Flask(__name__)

@app.route('/')
def getSleepScore():
    sleep_url = 'https://api.ouraring.com/v2/usercollection/sleep' 
    sleep_score_url = 'https://api.ouraring.com/v2/usercollection/daily_sleep' 

    today = date.today()
    yesterday = today - timedelta(days = 1)
    tomorrow = today + timedelta(days = 1)
    
    #get sleep score from yesterday - today
    params = { 
        'start_date': yesterday.__str__(), 
        'end_date': tomorrow.__str__() 
    }

    headers = { 
        'Authorization': '<redacted>' 
    }

    sleep_response = requests.request('GET', sleep_url, headers=headers, params=params)
    sleep_score_response = requests.request('GET', sleep_score_url, headers=headers, params=params) 
    sleep_score = json.loads(sleep_score_response.content)['data'][-1]['score']
    sleep_duration = int(json.loads(sleep_response.content)['data'][-1]['total_sleep_duration'])

    sleep_hours = int(sleep_duration / 3600)
    sleep_mins = int(sleep_duration / 60) % 60

    data = {
        'sleep': sleep_score,
        'sleep_hrs': sleep_hours,
        'sleep_mins': sleep_mins
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)