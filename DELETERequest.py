import requests
import json
import jsonpath

# get REST API end point
url = "https://reqres.in/api/users/2"

# Execute the rest DELETE API
response = requests.delete(url)

# prints the response code
v_status_code = response.status_code
print(v_status_code)

# prints the response text
v_data = response.text
print(v_data)

# assert conditions
assert v_status_code == 204
assert len(v_data) == 0