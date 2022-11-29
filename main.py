from utils import *
from flask import Flask


app = Flask(__name__)
candidates = load_candidates()


@app.route('/')
def page_index():
    return get_all(candidates)


@app.route('/candidates/<int:pk>')
def page_candidates(pk):
    candidate = get_by_pk(pk, candidates)
    if candidate:
        return candidate
    else:
        return 'Кандидат с указанным номером не найден'


@app.route('/skills/<skill>')
def page_skills(skill):
    candidate = get_by_skill(skill, candidates)
    if candidate:
        return candidate
    else:
        return 'Кандидат с указанными навыками отсутствует'


app.run()
