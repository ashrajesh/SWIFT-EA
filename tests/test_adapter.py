# to execute pytest: pipenv run pytest -rP

import pytest
import adapter

job_run_id = '1'

def adapter_setup(test_data):
    a = adapter.Adapter(test_data)
    return a.result


@pytest.mark.parametrize('test_data', [
    {'id': job_run_id, 'data': {'UETR': 'd2ecb184-b622-11e9-a2a3-2a2ae2dbcce4', 'status': 'transactions', 'oauth_token': 'xxxxxxx'}},
    {'id': job_run_id, 'data': {'transaction': 'd2ecb184-b622-11e9-a2a3-2a2ae2dbcce4', 'status': 'cancellation', 'oauth': 'xxxxxxx'}},
    {'id': job_run_id, 'data': {'ID': 'changed', 'status': 'transactions', 'token': 'xxxxxxx'}},
    {'id': job_run_id, 'data': {'ID': 'd2ecb184-b622-11e9-a2a3-2a2ae2dbcce4', 'status': 'status', 'token': 'xxxxxxx'}},
])
def test_create_request_success(test_data):
    result = adapter_setup(test_data)
    print(result)
    assert result['statusCode'] == 200
    assert result['jobRunID'] == job_run_id
    assert result['data'] is not None
    assert type(result['result']) is str
    assert type(result['data']['result']) is str

@pytest.mark.parametrize('test_data', [
    {'id': job_run_id, 'data': {'UETR': 'd2ecb184-b622-11e9-a2a3-2a2ae2dbcce4', 'status': 'transactions', 'oauth_token': 'xxxxxxx'}},
    {'id': job_run_id, 'data': {'transaction': 'N/A', 'status': '', 'oauth': ''}},
    {},
])
def test_create_request_error(test_data):
    result = adapter_setup(test_data)
    print(result)
    assert result['statusCode'] == 500
    assert result['jobRunID'] == job_run_id
    assert result['status'] == 'errored'
    assert result['error'] is not None