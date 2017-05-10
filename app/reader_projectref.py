import requests
import json
import pandas as pd

#reading configurations
with open('config.json') as conf_file:    
    conf = json.load(conf_file)

headers ={
    'X-Dreamfactory-API-Key': conf['api-key-lts'],
}

resp = requests.get('https://api.lts.no/api/v2/db-odoo1-lts/_table/project_task/?fields=description,create_date', headers=headers)
if resp.status_code != 200:
    # This means something went wrong
    print('ERROR, status-code == ' + str(resp.status_code))

pd.set_option('display.max_colwidth', -1)    
df = pd.DataFrame(resp.json()['resource'])

#Add column for year
df['year'] = df['create_date'].str[:4]

#Sort by create_date
df = df.sort_values('create_date', ascending=False)

#No need for create_date anymore
df = df.drop('create_date', 1)

#Remove rows without description
df = df[df['description'].notnull()]

#Changing place
df = df[['year', 'description']]

#Changing column headers
df.columns = ['År', 'Beskrivelse']

#Save file
df.to_html('ref.htm',index=False, justify='right')
