import csv
import math
import matplotlib.pyplot as plt 
from gx1 import *
from mat_fun import *
from decision_surface import *
from info_classes import *
from read_data import *

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

	means12, covs12, var12, pw12 = info_for_all_classes([training_data[0], training_data[1]])
	means23, covs23, var23, pw23 = info_for_all_classes([training_data[1], training_data[2]])
	means31, covs31, var31, pw31 = info_for_all_classes([training_data[2], training_data[0]])
	means123, covs123, var123, pw123 = info_for_all_classes(training_data)

	w, w0 = pocs(means12, var12, pw12)
	decision_boundary(w, w0, [training_data[0], training_data[1]], gx)
	w, w0 = pocs(means23, var23, pw23)
	decision_boundary(w, w0, [training_data[1], training_data[2]], gx)
	w, w0 = pocs(means31, var31, pw31)
	decision_boundary(w, w0, [training_data[2], training_data[0]], gx)
	w, w0 = pocs(means123, var123, pw123)
	decision_boundary(w, w0, training_data, gx)

