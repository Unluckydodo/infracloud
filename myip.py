import datetime
import sys

import requests

print(datetime.datetime.now())

r = requests.get("https://api.ipify.org?format=json", timeout=10)
print("Status Code:", r.status_code)
if r.status_code != 200:
    print("Error:", r.status_code, r.text, file=sys.stderr)
    sys.exit(1)

data = r.json()
print(data)

ip = data.get("ip")
if ip is None:
    print("Unexpected response:", data, file=sys.stderr)
    sys.exit(1)
print("IP Address:", ip)
