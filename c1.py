def gx(w, w0, x):
	return (multiply(x, w)[0][0] + w0)

def pocs(means, var, pw):
	cov = [[var, 0],[0, var]]
	w = []
	w0 = []
	for mu, p in zip(means, pw):
		w.append(multiply(inv(cov), transpose([mu])))
		w0.append(-0.5 * multiply([mu], transpose([mu]))[0][0] / var + math.log(p))
	return w, w0