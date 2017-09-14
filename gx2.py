from mat_fun import *
import math

def gx(w, w0, x, W):
	return (multiply(x, w)[0][0] + w0)

def pocs(means, cov, pw):
	w = []
	w0 = []
	for mu, p in zip(means, pw):
		w.append(multiply(inv(cov), transpose([mu])))
		w0.append(-0.5 * multiply(multiply([mu], inv(cov)), transpose([mu]))[0][0] + math.log(p))
	return w, w0