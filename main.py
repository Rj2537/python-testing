import requests as r
import json 
file_path ='url.json'
try:
    with open(file_path, "r") as file:
        data = json.load(file)
        url = data['default'][0]
    # print(url)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: The file '{file_path}' contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
post_url = url+"/meta/anilist/watch/spy-x-family-episode-1"
response = r.get(post_url)
data = response.json()
 
print(data)