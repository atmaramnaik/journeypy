import requests

url = 'http://jsonplaceholder.typicode.com/todos'



class coreApi:
    def execute_API(url, method='GET', payload={1: "a"}, headers={}):
        error = {}
        if method == 'GET':
            response = requests.get(url)
            if response.ok:
                return response
            else:
                return None

        elif method == 'POST':
            response = requests.post(url, json=payload, headers=headers)
            assert response.ok is True
            assert response.request.url == url
            assert response.request.body == payload
            assert response.request.headers == headers
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'PUT':
            response = requests.put(url, data=payload, headers=headers)
            assert response.ok is True
            assert response.request.url == url
            assert response.request.body == payload
            assert response.request.headers == headers
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'PATCH':
            response = requests.patch(url, data=payload, headers=headers)
            assert response.ok is True
            assert response.request.url == url
            assert response.request.body == payload
            assert response.request.headers == headers
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'DELETE':
            response = requests.delete(url, data='1')
            assert response.request.url == url
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}


