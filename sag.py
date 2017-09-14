import csv
import math
import matplotlib.pyplot as plot 

def read_file(file):
	dataset = list(csv.reader(open(file, 'r'), delimiter = ' '))
	dataset = [[float(x) for x in row] for row in dataset]
	return dataset

def split_dataset(dataset, ratio):
	divider = int(ratio * len(dataset))
	training_data = dataset[: divider]
	test_data = dataset[divider : ]
	return training_data, test_data

def mean(training_data):
	mu = []
	for i in range(len(training_data[0])):
		mu.append(sum(x[i] for x in training_data) / len(training_data))
	return mu

def covariance_matrix(training_data, mu):
	cov = [[0, 0], [0, 0]]
	for i in training_data:
		cov[0][0] += ((i[0] - mu[0]) ** 2)
		cov[1][1] += ((i[1] - mu[1]) ** 2)
		cov[0][1] += (i[0] - mu[0]) * (i[1] - mu[1])
	cov[0][0] /= len(training_data)
	cov[0][1] /= len(training_data)
	cov[1][1] /= len(training_data)
	cov[1][0] = cov[0][1]
	return cov

def mod(cov):
	return ((cov[0][0] * cov[1][1]) - (cov[0][1] ** 2))

def transpose(matrix):
	mat = [[]]
	for i in range(len(matrix[0])):
		mat.append([x[i] for x in matrix])
	return mat

def inv(matrix):
	invMat = [[0, 0], [0, 0]]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	invMat[0][0] = matrix[1][1]/det
	invMat[1][1] = matrix[0][0]/det
	invMat[0][1] = -1*matrix[1][0]/det
	invMat[1][0] = -1*matrix[0][1]/det
	return invMat

def multiply(mat1, mat2):
	mat3 = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]

	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for ij in range(len(mat1[0])):
				mat3[i][j] += mat1[i][ij] * mat2[ij][j]
	return mat3

def poc(mu1, mu2, var, pw1, pw2):
	w1 = multiply(inv(var), mu1)
	w10 = -0.5*multiply(transpose(mu1), mu1) + math.log(pw1)
	w2 = multiply(inv(var), mu2)
	w20 = -0.5*multiply(transpose(mu2), mu2) + math.log(pw2)
	g1 = multiply(transpose(w1), )

if __name__ == '__main__':
	dataset1 = read_file('Class1.txt')
	training_data1, test_data1 = split_dataset(dataset1, 0.75)
	dataset2 = read_file('Class2.txt')
	training_data2, test_data2 = split_dataset(dataset2, 0.75)
	# print(covariance_matrix(training_data, mean(training_data)))
	mu1 = mean(training_data1)
	mu2 = mean(training_data2)
	x0 = [(mu1[0] + mu2[0]) / 2, (mu1[1] + mu2[1]) / 2]
	slope = (mu1[1] - mu2[1]) / (mu1[0] - mu2[0])
	m = -1 / slope
	print(m, x0)
