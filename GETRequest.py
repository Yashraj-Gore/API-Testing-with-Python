import requests
import jsonpath
import json

# get REST API end point
url = "https://reqres.in/api/users?page=2"

# Execute the rest GET API
v_response = requests.get(url)

v_content = v_response.text
# prints the response
print(v_content)

# prints the response code
v_statuscode = v_response.status_code
print(v_statuscode)

# prints the jsondata
v_json_data = json.loads(v_content)
print(v_json_data)

# prints the value of per page value
v_per_page = jsonpath.jsonpath(v_json_data, 'per_page')
print(v_per_page)

# prints the length(total) data elements
v_data_elements = jsonpath.jsonpath(v_json_data, "data")
print(len(v_data_elements[0]))

# assert condition
assert v_statuscode == 200
assert v_per_page[0] == 6
assert v_per_page[0] == len(v_data_elements[0])
