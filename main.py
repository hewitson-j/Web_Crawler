import requests

url = input("Type in URL to crawl: ")

print("URL to run: ", url)

try:
    response = requests.get(url)
except:
    print("Invalid URL. Program terminating.")
    exit()

if response.status_code == 200:
    print(response.text)
