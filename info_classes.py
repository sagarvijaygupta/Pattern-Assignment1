from mat_fun import *

def info_for_all_classes(dataset):
	means = []
	
	for data in dataset:
		means.append(mean(data))
	covs = []

	for i in range(len(means)):
		covs.append(covariance_matrix(dataset[i], means[i]))
	meanCovs = [[0 for x in range(len(covs[0]))] for y in range(len(covs[0]))]

	for cov in covs:
		for i in range(len(cov)):
			for j in range(len(cov[0])):
				meanCovs[i][j] += cov[i][j]

	for i in range(len(meanCovs)):
		for j in range(len(meanCovs)):
			meanCovs[i][j] /= len(covs)

	pw = []
	all_data = 0
	for data in dataset:
		all_data += len(data)
	for data in dataset:
		pw.append(len(data) / all_data)
	return means, covs, meanCovs, pw