import csv
import math
import matplotlib.pyplot as plt 
import sys
from gx2 import *
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

	means12, covs12, meanCovs12, pw12 = info_for_all_classes([training_data[0], training_data[1]])
	means23, covs23, meanCovs23, pw23 = info_for_all_classes([training_data[1], training_data[2]])
	means31, covs31, meanCovs31, pw31 = info_for_all_classes([training_data[2], training_data[0]])
	means123, covs123, meanCovs123, pw123 = info_for_all_classes(training_data)

	w, w0 = pocs(means12, meanCovs12, pw12)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[0], test_data[1]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[0], training_data[1]], gx, sys.argv, ["class1", "class2"])
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[0], training_data[1]], Norm, sys.argv, ["class1", "class2"], means12, meanCovs12, 2)

	w, w0 = pocs(means23, meanCovs23, pw23)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[1], test_data[2]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[1], training_data[2]], gx, sys.argv, ["class2", "class3"])
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[1], training_data[2]], Norm, sys.argv, ["class2", "class3"], means23, meanCovs23, 2)
	

	w, w0 = pocs(means31, meanCovs31, pw31)
	confusion, accuracy, precision, recall, fmeasure = analysis([test_data[2], test_data[0]], w, w0, gx, None)
	decision_boundary(w, w0, [training_data[2], training_data[0]], gx, sys.argv, ["class3", "class1"])
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, [training_data[2], training_data[0]], Norm, sys.argv, ["class3", "class1"], means31, meanCovs31, 2)
	
	w, w0 = pocs(means123, meanCovs123, pw123)
	confusion, accuracy, precision, recall, fmeasure = analysis(test_data, w, w0, gx, None)
	decision_boundary(w, w0, training_data, gx, sys.argv, ["class1", "class2", "class3"])
	print(confusion,"\n", accuracy,"\n", precision,"\n", recall,"\n", fmeasure)
	contour(w, w0, training_data, Norm, sys.argv, ["class1", "class2", "class3"], means123, meanCovs123, 2)
	

