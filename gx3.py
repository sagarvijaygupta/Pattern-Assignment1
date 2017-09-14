from mat_fun import *
import math

def gx(w, w0, x, W):
	return multiply(multiply(x, W), transpose(x))[0][0] + multiply(transpose(w), transpose(x))[0][0] + w0

def pocs(means, covs, pw):
	w = []
	w0 = []
	W = []
	mat = [[-0.5, 0], [0, -0.5]]
	for mu, p, cov in zip(means, pw, covs):
		print(cov)
		W.append(multiply(mat, inv(cov)))
		w.append(multiply(inv(cov), transpose([mu])))
		w0.append(-0.5 * (multiply(multiply([mu], inv(cov)), transpose([mu])))[0][0] - 0.5 * math.log(abs(mod(inv(cov)))) + math.log(p))
	return w, w0, W