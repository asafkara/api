import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response)
# print(dir(response))
data = response.json()
print(data)

print(len(data))

for x in range(len(data)):
    print(data[x]['title'])

for x in data:
    print(x['title'])


names = ['ben', 'ahmed', 'tony', 'alice']
ages = [29, 31, 21, 34]

for n, a in zip(names, ages):
    print(n, a)

tickers = ["AAPL", "GOOGLE", "ETH"]
prices = [23.99, 199.34, 158.53]

for ticker, cost in zip(tickers, prices):
    if cost < 50:
        print(f"I just bought {ticker} for ${cost}")
    else:
        print(f"{ticker} is out of budget")

#post data to api

payload = {"title": "mocking jay", "userId": 49458}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)
print(response)
print(response.json())

payload = {"title": "mocking jay mocking ", "userId": 1, "body": "body bbodfobdo body bbodfobdo"}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)
print(response)
print(response.json())


#delete request

response = requests.delete("https://jsonplaceholder.typicode.com/posts/101")
print(response.json())