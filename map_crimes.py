import geojson as g
import parse as p 

def create_map(data_file):
	"""creates a geojson file to map the locations of crime incidents"""

	#define type of geojsonwe want to create.
	#we're defining the type of geojson as a 'FeatureCollection' collection of features (features can be points, multi-points, linestring, etc. )
	geo_map = {"type": "FeatureCollection"}

	#define an empty list to collect each point to graph
	#this list will collect our coordinates, for each iteration
	item_list = []

	#iterate over the dataset to create a geojson doc
	#enumerate() allows us to get the row and the row_num (row_num is the line number) for each row
	for row_num, row in enumerate(data_file):
		#skip any zero coordinates (this will throw off the map)
		if row['X'] == '0' or row['Y'] == '0':
			continue
		#setup a new dictionary for each iteration	
		data = {}

		#assign row specs to appropiate geojson fields
		data['type'] = 'Feature'
		data['id'] = row_num
		data['properties'] = {
								'title': row['Category'],
								'description': row['Descript'],
								'date': row['Date']
							 }
		data['geometry'] = {
							'type': 'Point',
							'coordinates': (row['X'], row['Y'])
						   }

		#add data dict to the item list
		item_list.append(data)

	#for each point in the item list, add the point to our geo_map dict. 
	#setdefault creates a default key to be added to the dict
	for point in item_list:
		geo_map.setdefault('features', []).append(point)

	#after the data is parsed in geojson, write the new parsed data to a file
	with open('sf_crimes.geojson', 'w') as f:
		f.write(g.dumps(geo_map)) 

def main():
	d = p.parse(p.MY_FILE, ",")
	return create_map(d)

if __name__ == "__main__":
    main()