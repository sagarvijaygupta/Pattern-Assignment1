import csv
import math
import matplotlib.pyplot as plt 
from gx3 import *
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

	means12, covs, meanCovs12, pw12 = info_for_all_classes([training_data[0], training_data[1]])
	means23, covs, meanCovs23, pw23 = info_for_all_classes([training_data[1], training_data[2]])
	means31, covs, meanCovs31, pw31 = info_for_all_classes([training_data[2], training_data[0]])
	means123, covs, meanCovs123, pw123 = info_for_all_classes(training_data)
	covs[0][0][1] = 0
	covs[0][1][0] = 0
	covs[1][0][1] = 0
	covs[1][1][0] = 0
	covs[2][0][1] = 0
	covs[2][1][0] = 0
	w, w0, W = pocs(means12, [covs[0], covs[1]], pw12)
	decision_boundary(w, w0, [training_data[0], training_data[1]], gx, W)
	w, w0, W = pocs(means23, [covs[1], covs[2]], pw23)
	decision_boundary(w, w0, [training_data[1], training_data[2]], gx, W)
	w, w0, W = pocs(means31, [covs[0], covs[2]], pw31)
	decision_boundary(w, w0, [training_data[2], training_data[0]], gx, W)
	w, w0, W = pocs(means123, covs, pw123)
	decision_boundary(w, w0, training_data, gx, W)

	