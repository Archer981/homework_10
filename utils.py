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


def get_by_pk(pk, candidates):
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill_name, candidates):
    result = []
    for candidate in candidates:
        if skill_name.lower() in candidate.lower().split(', '):
            result.append(candidate)
    return result
