import requests

pixela_endpoint = 'https://pixe.la/v1/users'
user_name = 'jawadali7898'
TOKEN = 'rh389r3iur9j8'
user_params = {
    'token': TOKEN,
    'username': user_name,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_endpoint = f'{pixela_endpoint}/{user_name}/graphs'
graph_id = 'graph1'
graph_name = 'Cycling Graph'

graph_config = {
    'id': graph_id,
    'name': graph_name,
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

value_endpoint = f'{graph_endpoint}/{graph_id}'

value_update_endpoint = f'{value_endpoint}/20240720'
value_config = {
    'quantity': '15'
}

value_headers = {
    'X-USER-TOKEN': TOKEN
}

value_response = requests.put(url=value_update_endpoint, json=value_config, headers=value_headers)
print(value_response.text)

