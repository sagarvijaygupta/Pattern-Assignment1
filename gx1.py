from mat_fun import *
import math
import numpy as np

def gx(w, w0, x, W):
	return (multiply(x, w)[0][0] + w0)

def pocs(means, meanCovs, pw):
	w = []
	w0 = []
	val = 0
	for i in range(len(meanCovs)):
		val += meanCovs[i][i]
	val /= len(meanCovs)

	for i in range(len(meanCovs)):
		meanCovs[i][i] = val
	
	for mu, p in zip(means, pw):
		w.append(multiply(inv(meanCovs), transpose([mu])))
		w0.append(-0.5 * multiply(multiply([mu],inv(meanCovs)), transpose([mu]))[0][0] + math.log(p))
	return w, w0

def Norm(x, mu, cov, d):
	if np.linalg.det(cov) == 0.0:
		print("wrong")
		inv = np.linalg.pinv(cov)
	else:
		inv = np.linalg.inv(cov)
	# print(mu2)
	
	# print(mu)
	det = np.linalg.det(inv)
	exp = (-0.5) * (np.matmul(np.matmul((x - mu), inv), (x - mu).T))
	exp = np.exp(exp)
	ans = exp / (np.power(2 * np.pi, d / 2) * np.power(np.absolute(det), 0.5))
	# print(ans)
	# print(exp)
	return ans