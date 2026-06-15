import trafilatura

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

downloaded = trafilatura.fetch_url(url)

text = trafilatura.extract(downloaded, output_format='txt')

print(text[:1000])