import numpy as np #valuable to replace list with numpy array

def process_data():
	import_train_data = []

	with open('income_data.txt') as inputfile:
		for line in inputfile:
			import_train_data.append(line.strip().split(', '))

	inputfile.close()

	features_train = []
	labels_train = []

	for i in range(len(import_train_data)):
		features_train.append(import_train_data[i][:-1])
		labels_train.append(import_train_data[i][-1])


	import_test_data = []

	with open('income_test.txt') as inputfile2:
		for line in inputfile2:
			import_test_data.append(line.strip().split(', '))

	inputfile2.close()

	features_test = []
	labels_test = []

	for i in range(len(import_test_data)):
		features_test.append(import_test_data[i][:-1])
		labels_test.append(import_test_data[i][-1])

	return features_train, labels_train, features_test, labels_test

features_train, labels_train, features_test, labels_test = process_data()

print(features_test[0])