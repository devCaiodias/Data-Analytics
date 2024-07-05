from httpx import get, post

url_base = 'http://127.0.0.1:5000/todos/api/tasks'

request = get(url_base)

assert request.status_code == 200, 'Codigo de resposta é diferente de 200'
assert request.json() == [], 'Algo de errado n está certo'

bad_task = {'tittle': 'Programar até cair'}
request = post(url_base, json=bad_task)
print(request)
assert request.status_code == 400, 'Codigo de resposta é diferente de 400'

god_task = {'tittle': 'Programar até cair','description': 'Pq é massa', 'done': True}

request = post(url_base, json=god_task)
assert request.status_code == 201, 'Codigo de resposta é diferente de 201'
