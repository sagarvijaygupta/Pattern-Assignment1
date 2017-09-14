import math

def analysis(test_data, w, w0, gx, W):
	right = 0

	classCount = 0
	total = 0
	confusion = [[0 for x in test_data] for y in test_data]

	for test in test_data:
		total += len(test)
		for data in test:
			min_gx = -1*math.inf
			min_idx = 0
			for x in range(len(test_data)):
				if W == None:
					if gx(w[x], w0[x], [data], W) > min_gx:
						min_idx = x
						min_gx = gx(w[x], w0[x], [data], W)
				else:
					if gx(w[x], w0[x], [data], W[x]) > min_gx:
						min_idx = x
						min_gx = gx(w[x], w0[x], [data], W[x])

			confusion[classCount][min_idx] += 1
		classCount += 1

	print(confusion)
	precision = []
	recall = []
	fmeasure = []

	for i in range(len(test_data)):
		right += confusion[i][i]
		precision.append(confusion[i][i]/sum(confusion[i]))
		recall.append(confusion[i][i]/(sum(x[i] for x in confusion)))

	for i in range(len(test_data)):
		fmeasure.append(2*precision[i]*recall[i]/(precision[i] + recall[i]))

	accuracy = right / total

	return confusion, accuracy, precision, recall, fmeasure
	