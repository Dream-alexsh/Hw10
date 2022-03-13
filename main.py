from flask import Flask
import json

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates = json.load(file)
    candidate_list_id = {}
    for i in candidates:
        candidate_list_id[i['id']] = i
    candidate_list = []
    for candidate in candidates:
        b = candidate['name'] + ' - ' + '\n' + candidate['position'] + '\n' + candidate['skills'] + '\n'
        candidate_list.append(b)


app = Flask(__name__)


@app.route('/')
def page_index():
    return '<pre>' + '\n'.join(candidate_list) + '</pre>'


@app.route('/candidate/<int:id>')
def page_candidate(id):
    candidate = candidates[id - 1]
    return '<img src="' + candidate['picture'] + '">' + '<pre>' + candidate['name'] + ' - ' + '\n' + candidate['position'] + '\n' + candidate['skills'] + '\n' + '</pre>'


@app.route('/skills/<skill>')
def page_skill(skill):
    candidate_str = ''
    for candidate in candidate_list_id.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            candidate_str += '<pre>' + candidate['name'] + ' - ' + '\n' + candidate['position'] + '\n' + candidate['skills'] + '\n' + '</pre>'
    return candidate_str

app.run()
