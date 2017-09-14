import csv
def read_file(file):
	dataset = list(csv.reader(open(file, 'r')))
	for i in range(len(dataset)):
		dataset[i][0] = dataset[i][0].rstrip(' ')
		dataset[i] = dataset[i][0].split()
	dataset = [[float(x) for x in row] for row in dataset]
	return dataset
	
def split_dataset(dataset, ratio):
	divider = int(ratio * len(dataset))
	training_data = dataset[: divider]
	test_data = dataset[divider : ]
	return training_data, test_data