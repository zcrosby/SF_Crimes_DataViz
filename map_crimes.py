import geojson as g
import parse as p 

def create_map(data_file):
	"""creates a geojson file to map the locations of crime incidents"""

	#define type of geojsonwe want to create

	#define an empty list to collect each point to graph

	#iterate over the dataset to create a geojson doc

	#skip any zero coordinates (this will throw off the map)

	#setup a new dictionary for each iteration

	#assign line items to appropiate geojson fields

	#add data dict to the item list

	#for each point in the item list, add the point to our dict.

	#after the data is parsed in geojson, write the new parsec data to a file 

def main():

	d = p.parse(p.MY_FILE, ",")
	
    create_map(d)

if __name__ == "__main__":
    main()