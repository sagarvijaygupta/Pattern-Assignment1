import csv
import math
import matplotlib.pyplot as plt 
import sys
from gx3 import *
from mat_fun import *
from decision_surface import *
from info_classes import *
from read_data import *
from analysis import *
from contour import *

if __name__ == '__main__':
	classes = [sys.argv[1]+'Class1.txt', sys.argv[1]+'Class2.txt', sys.argv[1]+'Class3.txt']
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

	w, w0, W = pocs(means12, [covs[0], covs[1]], pw12)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[0], test_data[1]], w, w0, gx, W)
	decision_boundary(w, w0, [training_data[0], training_data[1]], gx, sys.argv, ["class1", "class2"], W)
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[0], training_data[1]], gx, sys.argv, ["class1", "class2"], W)

	w, w0, W = pocs(means23, [covs[1], covs[2]], pw23)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[1], test_data[2]], w, w0, gx, W)
	decision_boundary(w, w0, [training_data[1], training_data[2]], gx, sys.argv, ["class2", "class3"], W)
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[1], training_data[2]], gx, sys.argv, ["class2", "class3"], W)
	
	w, w0, W = pocs(means31, [covs[0], covs[2]], pw31)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[2], test_data[0]], w, w0, gx, W)
	decision_boundary(w, w0, [training_data[2], training_data[0]], gx, sys.argv, ["class3", "class1"], W)
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[2], training_data[0]], gx, sys.argv, ["class3", "class1"], W)

	w, w0, W = pocs(means123, covs, pw123)
	confusion, accuracy, precision, recall, fmeasure = analysis(test_data, w, w0, gx, W)
	decision_boundary(w, w0, training_data, gx, sys.argv, ["class1", "class2", "class3"], W)
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, training_data, gx, sys.argv, ["class1", "class2", "class3"], W)

