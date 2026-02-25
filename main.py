import requests
from send_email import send_email

topic = "tesla"
api_key = "6d8aab6ff7194c7095356de4d655b49e"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=6d8aab6ff7194c7095356de4d655b49e&" \
      "language=en"

# Make request
r= requests.get(url)
# Get a dictionary with data
content = r.json()
# print(content["articles"])

# Access the article titles and description
body = "Subject: Today's News"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + "\n" \
               + article["title"] + "\n" \
               + str(article["description"]) + "\n" \
               + article["url"] + \
               + 2*"\n"
    # print(article["title"])
    # print(article["description"])

body = body.encode("utf-8")
send_email(message=body)