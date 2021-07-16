import os
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

UP_API_KEY = config.get('API','ACCESS_TOKEN')
UP_ENDPOINT = "https://api.up.com.au/api/v1/"

class APIKeyMissingError(Exception):
    pass

if UP_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developer.up.com.au/#getting-started "
        "for how to retrieve your Personal Access Token from "
        "Up"
    )
else:
    headers = {'Authorization': f'Bearer {UP_API_KEY}'}
    session = requests.Session()
    session.headers.update(headers)