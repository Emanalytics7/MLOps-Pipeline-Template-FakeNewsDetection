import requests

url = 'http://127.0.0.1:5000/predict'
data = {'text': 'A new study reveals that eating chocolate every day can make you lose weight without exercise.'}
response = requests.post(url, json=data)
print(response.text)


