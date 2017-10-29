from mat_fun import *
import math
import numpy as np

def gx(w, w0, x, W):
	return multiply(multiply(x, W), transpose(x))[0][0] + multiply(transpose(w), transpose(x))[0][0] + w0

def pocs(means, covs, pw):
	w = []
	w0 = []
	W = []
	mat = [[-0.5, 0], [0, -0.5]]
	for mu, p, cov in zip(means, pw, covs):
		W.append(multiply(mat, inv(cov)))
		w.append(multiply(inv(cov), transpose([mu])))
		w0.append(-0.5 * (multiply(multiply([mu], inv(cov)), transpose([mu])))[0][0] - 0.5 * math.log(abs(mod(inv(cov)))) + math.log(p))
	return w, w0, W

def Norm(x, mu, sigma, d):
	if np.linalg.det(sigma) == 0.0:
		print("wrong")
		inv = np.linalg.pinv(sigma)
	else:
		inv = np.linalg.inv(sigma)
	det = np.linalg.det(inv)
	exp = (-0.5) * (np.matmul(np.matmul((x - mu), inv), (x - mu).T))
	exp = np.exp(exp)
	ans = exp / (np.power(2 * np.pi, d / 2) * np.power(np.absolute(det), 0.5))
	return ans