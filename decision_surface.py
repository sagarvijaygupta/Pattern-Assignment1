import matplotlib.pyplot as plt
import math 

def decision_boundary(w, w0, dataset, gx, W = None):
	dataPlot = {}

	min_x = min_y = math.inf
	max_x = max_y = -1 * math.inf
	inc = 0
	for data in dataset:
		dataPlot[inc] = [[], []]
		for x in data:
			dataPlot[inc][0].append(x[0])
			dataPlot[inc][1].append(x[1])
			min_x = min(x[0], min_x)
			min_y = min(x[1], min_y)
			max_x = max(x[0], max_x)
			max_y = max(x[1], max_y)
		inc += 1
	len_x = max_x - min_x
	len_y = max_y - min_y
	min_x -= len_x*0.10
	min_y -= len_y*0.10
	max_x += len_x*0.10
	max_y += len_y*0.10

	epsilon =  (max_x - min_x)/300

	xValues = [[] for x in range(len(dataset))]
	yValues = [[] for x in range(len(dataset))]
	i = min_x
	j = min_y
	while i < max_x:
		j = min_y
		while j < max_y:
			min_gx = -1*math.inf
			min_idx = 0
			for x in range(len(dataset)):
				if W != None and gx(w[x], w0[x], [[i, j]], W[x]) > min_gx:
					min_idx = x
					min_gx = gx(w[x], w0[x], [[i, j]], W[x])

				if W==None and gx(w[x], w0[x], [[i, j]], W) > min_gx:
					min_idx = x
					min_gx = gx(w[x], w0[x], [[i, j]], W)
			xValues[min_idx].append(i)
			yValues[min_idx].append(j)
			j += epsilon
		i += epsilon
	colors_dot = ['#1A4F63', '#068587', '#6FB07F', '#FCB03C', '#FC5B3F']
	colors_triangle = ['#69ADFA', '#FFADA6', '#FF4A3A', '#CCED10', '#59660E']
	for x in range(len(dataset)):	
		plt.scatter(xValues[x], yValues[x], color = colors_dot[x], marker = 'o')	

	for x in range(len(dataset)):	
		plt.scatter(dataPlot[x][0], dataPlot[x][1], color = colors_triangle[x], marker = '.')
	plt.show()