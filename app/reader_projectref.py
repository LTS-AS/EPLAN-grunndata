import requests
import json
import sys

#reading configurations
with open('config.json') as conf_file:    
    conf = json.load(conf_file)
    

resp = requests.get('https://api.lts.no/api/v2/db/_table', headers={'X-Dreamfactory-API-Key': conf['api-key-lts']})
if resp.status_code != 200:
    # This means something went wrong.
    print('ERROR, status-code != 200')
    #sys.exit(1)
    

for todo_item in resp.json()['resource']:
    print('{} {}'.format(todo_item['name'], ''))
