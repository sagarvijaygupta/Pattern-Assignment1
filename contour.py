import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math 
import numpy as np

def contour(w, w0, dataset, Norm, args, classes, mu, sigma, d, W = None):
	dataPlot = {}
	
	case = args[0][:-3]
	dataSource = args[1][:-1]
	
	plt.xlabel('X')
	plt.ylabel('Y')
	title = dataSource + '\n'
	for i in range(len(classes)):
		title = title + ' ' + classes[i]
		if i != len(classes) - 1:
			title = title + ' vs '
	plt.title(title)

	legends = []

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

	xValues = []
	yValues = []
	zValues = [[] for x in range(1+int((max_y-min_y)/epsilon))]
	print(len(zValues))
	i = min_x
	j = min_y
	count = 0
	while j < max_y:
		yValues.append(j)
		i = min_x
		while i < max_x:
			max_Norm = -1*math.inf
			min_idx = 0
			for x in range(len(dataset)):
				if W != None and Norm(np.array([[i, j]]), mu[x], sigma, d)[0][0] > max_Norm:
					min_idx = x
					max_Norm = Norm(np.array([[i, j]]), mu[x], sigma, d)[0][0]

				if W==None and Norm(np.array([[i, j]]), mu[x], sigma, d)[0][0] > max_Norm:
					min_idx = x
					max_Norm = Norm(np.array([[i, j]]), mu[x], sigma, d)[0][0]

			if j == min_y:
				xValues.append(i)
			zValues[count].append(max_Norm)
			i += epsilon
		j += epsilon
		count += 1

	colors_dot = ['#1A4F63', '#068587', '#6FB07F', '#FCB03C', '#FC5B3F']
	colors_triangle = ['#69ADFA', '#FFADA6', '#FF4A3A', '#CCED10', '#59660E']
	# print(zValues)
	cp = plt.contour(xValues, yValues, zValues, colors = 'k')
	plt.clabel(cp, inline=True, 
	          fontsize=10)

	for x in range(len(dataset)):	
		plt.scatter(dataPlot[x][0], dataPlot[x][1], color = colors_triangle[x], marker = '.')
		legends.append(mpatches.Patch(color = colors_triangle[x], label = classes[x] + ' data'))
	plt.legend(handles = legends).get_frame().set_alpha(0.5)
	str = ""
	for i in range(len(classes)):
		str += classes[i][-1]
	plt.savefig("Plots/" + case + "/" + dataSource + "/" + case + dataSource + "Contour" + str)
	plt.show()