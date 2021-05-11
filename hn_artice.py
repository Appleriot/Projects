import requests
import json

# MAke a API call, and store the respone.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the strututre of the data.
repsone_dict = r.json
readble_file = 'data/readable_hn_data.json'
with open(readble_file, 'w') as f:
    json.dump(repsone_dict, f, indent=4)
