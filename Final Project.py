import json
import csv

raw = []
with open('yelp_academic_dataset_business.json') as f:
    for line in f:
        raw.append(json.loads(line))
		
  
	
#CategoriesIWant = ['Restaurants', 'Food']
#any(x in r['categories'] for x in CategoriesIWant)

filtered_list = [r for r in raw if r['city'] == 'Phoenix' and 'Restaurants' in r['categories']]

print str(filtered_list[1]['categories'])
a = []

for i in filtered_list:
	a.append((i['name'], str(i['categories']), i['latitude'], i['longitude']))
	

	
def write_csv(file_name, data=[], columns=()):
    with open(file_name, 'wb') as f:
        writer = csv.writer(f)
        data_to_write = []
        for i in data:
            tup = []
            for j in i:
                tup.append(unicode(j).encode('utf-8'))
            data_to_write.append(tuple(tup))
        writer.writerows(data_to_write)
		
write_csv("name_latitude_longitude.csv", data = a)