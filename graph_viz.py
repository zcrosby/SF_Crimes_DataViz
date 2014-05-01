from collections import Counter
import csv

import matplotlib.pyplot as plt
import numpy.numarray as na


# Put the full path to your CSV/Excel file here
MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)
    
    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)#reader returns an iterators where we can access one element at a time

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    #for eac row in the csv, create a dictionary 
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    num_of_incidents = 0

    for i in parsed_data:
        num_of_incidents+=1

    #print counter
    return parsed_data

def visualize_by_day():
	'''visualize data by the day of the week'''

	#get the parsed data 
	data = parse(MY_FILE, ",")

	#count number of incidents that happened on each day of the week (variable counter)
	#Counter inherits pythondictionary structure. here it's iterating over each element in 
	#the list, which is a list of dictionaries, then grabs each Day of the week key
	counter = Counter(i["DayOfWeek"] for i in data)#called a list comprehension

	hand_counter = 0
	for i in data:
		key = "DayOfWeek"
		if key in i:
			hand_counter+=1
	print hand_counter

	print counter
	#separate the x-axis data (the days of the week) from the'counter' variable from the y-axis 
	#data (the number of incidents for each day)
	data_list = [
					counter["Monday"],
					counter["Tuesday"],
					counter["Wednesday"],
					counter["Thursday"],
					counter["Friday"],
					counter["Saturday"],
					counter["Sunday"]
				]

	day_labels_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	# with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)

	# create the amount of ticks needed for our x-axis, and assign the labels
    #xticks takes the num of ticks on x axis for the first arg, then takes a tuple of labels associated with those ticks
    #range returns an array of integers in this case range(len(day_labels_tuple)) = [0, 1, 2, 3, 4, 5, 6]
	plt.xticks(range(len(day_labels_tuple)), day_labels_tuple)

	#save the plot
	plt.savefig("Days.png")

	#close plot file
	plt.clf()

def visualize_by_category():
	"""Visualize data by category in a bar graph"""
	
	data = parse(MY_FILE, ",")

	#count number of times each category occurs ex. {'WARRANTS': 31, ...}
	counter = Counter(i["Category"] for i in data)
	#print(counter)

	hand_counter = 0
	for i in data:
		key = "Category"
		if key in i:
			hand_counter += 1
	#print(hand_counter + "incidents by category")

	#labels are the keys pulled from the Counter
	#order does not matter, so we can use counter.keys() which returns an array of category names ex. ['FRAUD', 'WEAPON LAWS', ...]
	category_labels = tuple(counter.keys()) #we have to put them in a tuple, for xticks()

	#with our labels, we'll use numpy.numarray to create a list of 
	#ticks, delimited by spaces (numarray does this for us), where 
	#we want to place our labels on the x-axis (ex. of list [  0.5   1.5   2.5 ...])
	#xlocations will be used to help place plt.xticks()
	xlocations = na.array(range(len(category_labels))) + 0.5

	#set the width of the bars in the graph
	w = 0.5
	plt.bar(xlocations, counter.values(), width=w)

	#place labels and tick location to xaxis
	plt.xticks(xlocations + w/2, category_labels, rotation=90)

	#this method will adjust to the inconsistency of labels in 
	plt.subplots_adjust(bottom=0.4)

	plt.rcParams['figure.figsize'] = 12, 8

	plt.savefig("Category.png")

	plt.clf()


def main():
    visualize_by_category()

if __name__ == "__main__":
    main()