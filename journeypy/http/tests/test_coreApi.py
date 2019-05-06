from journeypy.http import CoreApi
import requests
def test_get(mocker):
    mocker.patch.object(requests, 'get')
    requests.get.return_value.status_code = 200
    response = CoreApi.execute_API("http://localhost", method="GET")
    requests.get.assert_called_with("http://localhost")

def test_post(mocker):
    mocker.patch.object(requests, 'post')
    requests.post.return_value.status_code = 200
    requests.post.return_value.ok = True
    response = CoreApi.execute_API("http://localhost", method="POST",payload={"a":"A"})
    requests.post.assert_called_with("http://localhost",data={"a":"A"},headers={})

def test_patch(mocker):
    mocker.patch.object(requests, 'patch')
    requests.patch.return_value.status_code = 200
    requests.patch.return_value.ok = True
    response = CoreApi.execute_API("http://localhost", method="PATCH",payload={"a":"A"})
    requests.patch.assert_called_with("http://localhost",data={"a":"A"},headers={})

def test_put(mocker):
    mocker.patch.object(requests, 'put')
    requests.put.return_value.status_code = 200
    requests.put.return_value.ok = True
    response = CoreApi.execute_API("http://localhost", method="PUT",payload={"a":"A"})
    requests.put.assert_called_with("http://localhost",data={"a":"A"},headers={})

def test_delete(mocker):
    mocker.patch.object(requests, 'delete')
    requests.delete.return_value.status_code = 200
    requests.delete.return_value.ok = True
    response = CoreApi.execute_API("http://localhost", method="DELETE",payload={"a":"A"})
    requests.delete.assert_called_with("http://localhost",data={"a":"A"},headers={})