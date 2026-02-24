import requests

api_key = "6d8aab6ff7194c7095356de4d655b49e"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2026-01-24&sortBy=publishedAt&apiKey=" \
      "6d8aab6ff7194c7095356de4d655b49e"

# Make request
r= requests.get(url)
# Get a dictionary with data
content = r.json()
print(content["articles"])

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])