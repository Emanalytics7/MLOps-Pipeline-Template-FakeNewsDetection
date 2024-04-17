import requests

url = 'http://20.195.118.156:5500/predict' # Adjust this
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