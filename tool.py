import unidecode
import json
accented_string = 'Thành phố hồ chí minh'
# accented_string is of type 'unicode'
unaccented_string = unidecode.unidecode(accented_string)
# unaccented_string contains 'Malaga'and is of type 'str'

with open('city.json','r',encoding='utf-8') as f:
    data = json.load(f)

for i in data:
    accented_string = i['name']
    # accented_string is of type 'unicode'
    i['name'] = unidecode.unidecode(accented_string)
    # unaccented_string contains 'Malaga'and is of type 'str'i['name']

with open('city2.json','w') as f:
    json.dump(data,f, indent=4)