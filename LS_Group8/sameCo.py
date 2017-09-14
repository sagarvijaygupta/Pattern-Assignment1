Class1 = []
Class2 = []
Class3 = []

def read():
	global Class1, Class2, Class3 	
	with open('Class1.txt') as f:
		Class1 = f.readlines()
	Class1 = [x.split() for x in Class1]

	Class1 = [[float(x) for x in row] for row in Class1]
	Class1 = Class1[:int(0.75 * len(Class1))]

	with open('Class2.txt') as f:
		Class2 = f.readlines()
	Class2 = [x.split() for x in Class2]

	Class2 = [[float(x) for x in row] for row in Class2]

	with open('Class3.txt') as f:
		Class3 = f.readlines()
	Class3 = [x.split() for x in Class3]

	Class3 = [[float(x) for x in row] for row in Class3]


# print zip(*matrix)
def covarienceMatrix(matrix):
	mu = []
	for i in range(len(matrix[0])):
		mu.append(sum(x[i] for x in matrix)/len(matrix))
	transMatrix = [[x[0] for x in matrix], [x[1] for x in matrix]]			
	matrix = zip(*matrix)
 	return [[sum((a-mu[0])*(b-mu[1]) for a, b in zip(row_trans_mat, col_matrix)) for col_matrix in matrix] for row_trans_mat in transMatrix]

def meanCovMatrix():
	m1 = covarienceMatrix(Class1)
	m2 = covarienceMatrix(Class2)
	m3 = covarienceMatrix(Class3)

	return [[(m1[i][j] + m2[i][j] + m3[i][j])/3 for j in range(len(m1[0]))] for i in range(len(m1))]

read()
# print Class1	
print covarienceMatrix(Class1)
# print meanCovMatrix()
# print line