import requests
class CoreApi:
    def execute_API(url, method='GET', payload={}, headers={}):
        error = {}
        if method == 'GET':
            response = requests.get(url)
            if response.ok:
                return response
            else:
                return None

        elif method == 'POST':
            response = requests.post(url, data=payload, headers=headers)
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'PUT':
            response = requests.put(url, data=payload, headers=headers)
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'PATCH':
            response = requests.patch(url, data=payload, headers=headers)
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}

        elif method == 'DELETE':
            response = requests.delete(url, data=payload,headers=headers)
            return {'response': response.status_code, 'json_response': response.json(), 'error': error}


