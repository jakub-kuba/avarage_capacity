import pickle
import json

with open ("countries.dat", "rb") as f:
    mydict = pickle.load(f)

print(mydict)

for my in mydict:
    mydict[my] = mydict[my][-3:]

with open('countries_dict.json', 'w') as cd:
    json.dump(mydict, cd)

with open('countries_dict.json', 'r') as countries:
    ctr_json = json.load(countries)

print(ctr_json)

