import requests

url = 'http://127.0.0.1:5000/predict' # local host you can adjust yours here!
data = {'text': 'A new study reveals that eating chocolate every day can make you lose weight without exercise.'}
response = requests.post(url, json=data)
print(response.text)


#output 
"""
    {
  "prediction": "Fake News",
  "probability": [
    0.9602542836386087,
    0.03974571636139135
  ]
}

"""