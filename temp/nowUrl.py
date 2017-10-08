import requests

def readUrl(url):
	webContent = requests.get(url,verify=True).text
	return webContent

url = 'https://secure.orbitremit.com/api/rates/AUD:INR.json'
data = readUrl(url)

print(data)