import requests


def load_candidates():
    response = requests.get('https://www.jsonkeeper.com/b/MWLL').json()
    return response
