import requests

url = "http://127.0.0.1:5000/tasks"

payload = {
    "title": "Benyamin",
    "priority": 7
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

response2 = requests.get(url)
print(response2.status_code)
print(response2.json())

url2 = "http://127.0.0.1:5000/tasks/1"

response3 = requests.put(url2)
print(response3.status_code)
print(response3.json())

response4 = requests.delete(url2)
print(response4.status_code)
print(response4.json())