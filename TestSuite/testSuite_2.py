import requests
import json
import jsonpath

def test_PostRequestAPI():
    # get rest API End point
    url = "https://reqres.in/api/users"

    # read the data from the file
    f_pointer = open("C:\\Python API\\Sample_Post_input.json", mode='r')
    v_input_data = f_pointer.read()

    # convert the data into json/dict
    v_input_data_json = json.loads(v_input_data)

    # print input data
    print(v_input_data_json)

    # Execute the rest POST API
    v_response = requests.post(url, v_input_data_json)
    print(v_response.text)

    # response code of the request
    v_responsecode = v_response.status_code
    print(v_responsecode)

    # convert the data into json
    json_data = json.loads(v_response.text)
    print(json_data)

    # get the id of the response of students value
    v_id = jsonpath.jsonpath(json_data, "id")
    print(v_id[0])

    # assert condition
    assert v_responsecode == 201

def test_PutRequestAPI():
    # get rest API End point
    url = "https://reqres.in/api/users/2"

    # read the data from the file
    f_pointer = open("C:\\Python API\\Sample_Put_input.json", mode='r')
    v_input_data = f_pointer.read()

    # convert the data into json/dict
    v_input_data_json = json.loads(v_input_data)

    # print input data
    print(v_input_data_json)

    # Execute the rest PUT API
    v_response = requests.put(url, v_input_data_json)
    print(v_response.text)

    # response code of the request
    v_responsecode = v_response.status_code
    print(v_responsecode)

    # convert the data into json
    json_data = json.loads(v_response.text)
    print(json_data)

    v_name_input = v_input_data_json['name']
    v_job_input = v_input_data_json['job']

    print(v_name_input)
    print(v_job_input)

    # get the data from the response file
    v_name = jsonpath.jsonpath(json_data, 'name')
    v_job = jsonpath.jsonpath(json_data, 'job')
    v_updatedAt = jsonpath.jsonpath(json_data, 'updatedAt')
    print(v_name[0])
    print(v_job[0])
    print(v_updatedAt[0])

    # assert condition
    assert v_responsecode == 200
    assert v_job[0] == v_job_input
    assert v_name[0] == v_name_input
    assert v_updatedAt[0] is not None