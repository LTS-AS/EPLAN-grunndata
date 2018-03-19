from pandas import DataFrame
import json

with open('data\\standard_archive.json') as f:
    data = json.load(f)

df = DataFrame(data)

print(df)