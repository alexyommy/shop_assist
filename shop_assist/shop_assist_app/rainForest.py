import json
import requests

# set up the request parameters
# params = {
#     'api_key': '2613DE212DD24509A46720C4C27202D9',
#     'type': 'bestsellers',
#     'url': 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b'
# }

# # make the http GET request to Rainforest API
# api_result = requests.get('https://api.rainforestapi.com/request', params)

# # print the JSON response from Rainforest API
# print(json.dumps(api_result.json()))


# set up the request parameters
params = {
    'api_key': '2613DE212DD24509A46720C4C27202D9',
    'type': 'bestsellers',
    'url': 'https://www.amazon.com/Best-Sellers-Musical-Instruments/zgbs/musical-instruments/ref=zg_bs_nav_0'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

data = json.dumps(api_result.json(), indent=4, sort_keys=True)

# print the JSON response from Rainforest API
print(data)


# print(data['bestsellers'])

# for item in data['type']:
#     print (item["current_category"])
