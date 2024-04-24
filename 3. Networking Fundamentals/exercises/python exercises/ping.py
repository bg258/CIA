import requests

url = "https://www.cisco.com"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is reachable.")
    else:
        print(f"{url} is not reachable. Status code: {response.status_code}")
except requests.ConnectionError:
    print(f"{url} is not reachable.")
