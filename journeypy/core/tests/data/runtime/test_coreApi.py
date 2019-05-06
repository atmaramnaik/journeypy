from journeypy.core.data.runtime.coreApi import coreApi
from mock import patch
import mocker
import requests


def test_request_response():
    mocker.patch.object(requests, 'get')
    requests.return_value.status_code = 200
    response = coreApi.execute_API()
    print(response)
#
# def test_request_response(self):
#     # print(coreApi.execute_API())
#     with patch(coreApi.execute_API,'re') as mock_get:
#         mock_get.return_value.status_code = 200
#         response = coreApi.execute_API()
#         self.assertEqual(response.status_code, 200)


