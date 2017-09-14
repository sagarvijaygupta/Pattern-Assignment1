
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
	mat = []
	for i in range(len(matrix[0])):
		mat.append([x[i] for x in matrix])
	return mat

def inv(matrix):
	invMat = [[0, 0], [0, 0]]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	invMat[0][0] = matrix[1][1] / det
	invMat[1][1] = matrix[0][0] / det
	invMat[0][1] = -1*matrix[1][0] / det
	invMat[1][0] = -1*matrix[0][1] / det
	return invMat

def multiply(mat1, mat2):
	mat3 = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]

	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for ij in range(len(mat1[0])):
				mat3[i][j] += mat1[i][ij] * mat2[ij][j]
	return mat3