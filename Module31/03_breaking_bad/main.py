from pprint import pprint
import requests
import json


my_req = requests.get('https://www.breakingbadapi.com/api/deaths/')


death_dict = json.loads(my_req.text)
result = sorted(death_dict, key=lambda count: int(count['number_of_deaths']), reverse=True)


with open('max_death.json', 'w') as file:
    json.dump(result[0], file, indent=4)

pprint(result[0])
