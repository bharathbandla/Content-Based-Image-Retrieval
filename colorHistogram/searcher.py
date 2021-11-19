# import the necessary packages
import numpy as np
import csv

# this is the path for feature database which we stored for all training data
feature_data_path = r'C:\files\sem5\Machine Learning\project\code\colorHistogram\featuresData.csv'

eps=1e-10

# this will search for a given image to all the images features in the csv file
def Searcher(queryFeatures, limit = 4):
	# this is our dictionary of results to be store
	results = {}
	# open the index file for reading
	with open(feature_data_path) as f:
		# initialize the CSV reader
		reader = csv.reader(f)
		# loop over the rows in the index
		for row in reader:
			# parse out the image ID and features, then compute the
			# chi-squared distance between the features in our index
			# and our query features
			# get the features of the row, except 1st column, because that is image name
			# convert each feature into float
			features = [float(x) for x in row[1:]]

			# this is to get the chi-square distance calculation to get the distance b/t query image Feature and this row features
			d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(features, queryFeatures)])

			# insert into the dictionary
			# key is the current image ID in the index and the value is the distance we just computed,
			results[row[0]] = d

		# close the reader
		f.close()

	# sort our results, so that the smaller distances are more closer to the given query image
	results = sorted([(v, k) for (k, v) in results.items()])
	# return our (limited) results
	return results[:limit]
