import trafilatura

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

downloaded = trafilatura.fetch_url(url)

text = trafilatura.extract(downloaded)

print(text[:1000])