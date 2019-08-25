# importing Modules
import requests
import jsonpath
import json


def test_allapi():
    # get rest API End point
    url = 'https://reqres.in/api/users?page=1'
    print(url)
    # Execute the rest GET API
    v_response = requests.get(url)
    # response code of the request
    v_responsecode = v_response.status_code
    # convert the data into JSON
    json_data = json.loads(v_response.text)
    # get the per_page value
    v_per_page = jsonpath.jsonpath(json_data, 'per_page')
    # get the number of students value
    v_student_records = jsonpath.jsonpath(json_data, 'data')
    v_count_records = len(v_student_records[0])
    # assert condition
    assert v_responsecode == 200
    assert v_per_page[0] == 6
    assert v_count_records == v_per_page[0]
    # store the Dynamic data
    v_id = jsonpath.jsonpath(json_data, 'data[1].id')
    v_email = jsonpath.jsonpath(json_data, 'data[1].email')
    v_first_name = jsonpath.jsonpath(json_data, 'data[1].first_name')
    v_last_name = jsonpath.jsonpath(json_data, 'data[1].last_name')

    # Get the single user details
    url = 'http://reqres.in/api/users/' + str(v_id[0])
    print(url)
    # Execute the rest GET API
    v_response = requests.get(url)
    # response code of the request
    v_responsecode = v_response.status_code
    json_data = json.loads(v_response.text)
    v_id_1 = jsonpath.jsonpath(json_data, 'data.id')
    v_email_1 = jsonpath.jsonpath(json_data, 'data.email')
    v_first_name_1 = jsonpath.jsonpath(json_data, 'data.first_name')
    v_last_name_2 = jsonpath.jsonpath(json_data, 'data.last_name')
    # assert condition
    assert v_responsecode == 200
    assert v_id_1 == v_id
    assert v_email_1 == v_email
    assert v_first_name_1 == v_first_name
    assert v_last_name_2 == v_last_name

    # Delete the ID
    url = 'http://reqres.in/api/users/' + str(v_id[0])
    print(url)
    # Execute the rest GET API
    v_response = requests.delete(url)
    # response code of the request
    v_responsecode = v_response.status_code
    # assert condition
    assert v_responsecode == 204
    assert len(v_response.text) == 0