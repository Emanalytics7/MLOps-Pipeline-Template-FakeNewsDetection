import requests

url = 'http://52.172.25.57:5000/predict' # Replace with your IP address or url of your deployed api
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