import requests


def load_candidates():
    response = requests.get('https://www.jsonkeeper.com/b/MWLL').json()
    return response


def get_all(candidates):
    for candidate in candidates:
        print(candidate['name'])
        print(candidate['position'])
        print(candidate['skills'])
        print()
