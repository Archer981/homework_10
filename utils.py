import requests


def load_candidates():
    response = requests.get('https://www.jsonkeeper.com/b/MWLL').json()
    return response


def get_all(candidates):
    result = ''
    for candidate in candidates:
        result += f'Имя кандидата - {candidate["name"]}<br>'
        result += f'{candidate["position"]}<br>'
        result += f'{candidate["skills"]}<br><br>'
    return result


def get_by_pk(pk, candidates):
    for candidate in candidates:
        if candidate['pk'] == pk:
            return (f'Имя кандидата - {candidate["name"]}<br>'
                    f'{candidate["position"]}<br>'
                    f'{candidate["skills"]}<br>')
    return


def get_by_skill(skill, candidates):
    result = ''
    for candidate in candidates:
        if skill.lower() in candidate['skills'].lower().split(', '):
            result += (f'Имя кандидата - {candidate["name"]}<br>'
                       f'{candidate["position"]}<br>'
                       f'{candidate["skills"]}<br><br>')
    return result
