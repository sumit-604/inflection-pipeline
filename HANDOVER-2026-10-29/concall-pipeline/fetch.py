import requests

print("Sending request to Screener...")
response = requests.get("https://www.screener.in")
print("Status code:", response.status_code)
print("Page size:", len(response.text), "characters")
print("Done!")