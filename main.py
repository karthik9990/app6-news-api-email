import requests

api_key = "8f91250ce8d24c01bb1c45a963713eb4"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-02-29&sortBy=publishedAt&apiKey"
       "=8f91250ce8d24c01bb1c45a963713eb4")

# make a request
request = requests.get(url)

# get the dictionary with data
content = request.json()

# access teh article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
