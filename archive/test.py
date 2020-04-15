import pandas as pd
from iso3166 import countries
import json
#import numpy as np
iso = pd.read_csv('C:/Users/d9ld9/github/weatherin/app/static/iso3166_rus.csv',usecols=['Alpha-2','Alpha-3'], encoding = "utf-8")
iso.dropna(inplace=True)
labels = list(iso[(iso['Alpha-2'] == 'AN') | (iso['Alpha-2'] == 'CS') | (iso['Alpha-2'] == 'SU')].index.values) # they don't exist anymore
iso.drop(index=labels,inplace=True)
iso['Country_en'] = [countries.get(row).name for row in iso['Alpha-2']]
data = [{'Country_en':'Benin','Alpha-2':'BJ','Alpha-3':'BEN'},
        {'Country_en':'Bonaire','Alpha-2':'BQ','Alpha-3':'BES'},
        {'Country_en':'Sint Eustatius','Alpha-2':'BQ','Alpha-3':'BES'},
        {'Country_en':'Saba','Alpha-2':'BQ','Alpha-3':'BES'},
        {'Country_en':'Curaçao','Alpha-2':'CW','Alpha-3':'CUW'},
        {'Country_en':'Guernsey','Alpha-2':'GG','Alpha-3':'GGY'},
        {'Country_en':'Isle of Man','Alpha-2':'IM','Alpha-3':'IMN'},
        {'Country_en':'Jersey','Alpha-2':'JE','Alpha-3':'JEY'}]
iso.append(data,ignore_index=True,sort=False)
iso.sort_values(by='Country_en', inplace=True)
#choices = [", ".join(e for e in list) for list in iso[['Alpha-3','Country','Country_en']].values.tolist()]
iso_json = iso.to_json(orient='records')
with open('C:/Users/d9ld9/github/weatherin/app/static/countries.json', 'w', encoding='utf-8') as f:
    json.dump(iso_json, f, ensure_ascii=False, indent=4)
#print(iso_json)
#print(iso['Country_en'])
with open('C:/Users/d9ld9/github/weatherin/app/static/countries.json', 'r') as f:
    countries = json.loads(json.load(f))
#jsonData = json.loads(countries)
choices = [elem['Alpha-2']+', '+elem['Country_en'] for elem in countries]
print(choices)
