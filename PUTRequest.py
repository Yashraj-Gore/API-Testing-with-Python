import requests
import json
import jsonpath

# get rest API End point
url = "https://reqres.in/api/users/2"

# read the data from the file
f_pointer = open("C:\\Python API\\Sample_Put_input.json",mode='r')
v_input_data = f_pointer.read()

# convert the data into json/dict
v_input_data_json = json.loads(v_input_data)

# print input data
print("---------Input Data---------")
print(v_input_data_json)

# Execute the rest PUT API
v_response = requests.put(url,v_input_data_json)
print("---------API Response---------")
print(v_response.text)

# response code of the request
v_responsecode = v_response.status_code
print("---------Response Code---------")
print(v_responsecode)

# convert the data into json
json_data = json.loads(v_response.text)
print("---------JSON DATA---------")
print(json_data)

v_name_input = v_input_data_json['name']
v_job_input = v_input_data_json['job']

print("---------Name in the input file is---------")
print(v_name_input)
print("---------Job in the input file is---------")
print(v_job_input)

# get the data from the response file
v_name = jsonpath.jsonpath(json_data,'name')
v_job = jsonpath.jsonpath(json_data,'job')
v_updatedAt = jsonpath.jsonpath(json_data,'updatedAt')
print("---------Name in the response is---------")
print(v_name[0])
print("---------job in the response is---------")
print(v_job[0])
print("---------updatedDate in the response is---------")
print(v_updatedAt[0])

# assert condition
assert v_responsecode == 200
assert v_job[0] == v_job_input
assert  v_name[0] == v_name_input
assert v_updatedAt[0] is not None