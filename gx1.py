from mat_fun import *
import math

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