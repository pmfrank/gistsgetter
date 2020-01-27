import requests
from requests.auth import HTTPBasicAuth
import json

def search(url, username, password):

    gist_info = str()
    
    response = requests.get(url, auth=(username,password))
    if response.status_code != 200:
        return 'Failed to authenticate'
    for filename, content in response.json()['files'].items():
        gist_info = gist_info + f"{filename}\n{content['content']}\n"

    return gist_info