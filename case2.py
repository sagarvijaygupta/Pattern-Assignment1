import csv
import math
import matplotlib.pyplot as plt 
from gx2 import *
from mat_fun import *
from decision_surface import *
from info_classes import *
from read_data import *
from analysis import *

if __name__ == '__main__':
	classes = ['Class1.txt', 'Class2.txt', 'Class3.txt']
	dataset = []
	for i in classes:
		dataset.append(read_file(i))
	training_data, test_data = [], []
	for data in dataset:
		training, test = split_dataset(data, 0.75)
		training_data.append(training)
		test_data.append(test)

	means12, covs12, meanCovs12, pw12 = info_for_all_classes([training_data[0], training_data[1]])
	means23, covs23, meanCovs23, pw23 = info_for_all_classes([training_data[1], training_data[2]])
	means31, covs31, meanCovs31, pw31 = info_for_all_classes([training_data[2], training_data[0]])
	means123, covs123, meanCovs123, pw123 = info_for_all_classes(training_data)

	w, w0 = pocs(means12, meanCovs12, pw12)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[0], test_data[1]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[0], training_data[1]], gx)

	w, w0 = pocs(means23, meanCovs23, pw23)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[1], test_data[2]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[1], training_data[2]], gx)
	

	w, w0 = pocs(means31, meanCovs31, pw31)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[2], test_data[0]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[2], training_data[0]], gx)
	
	w, w0 = pocs(means123, meanCovs123, pw123)
	confusion, accuracy, precision, recall, fmeasure = analysis(test_data, w, w0, gx, None)
	decision_boundary(w, w0, training_data, gx)
	

