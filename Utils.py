import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

class Utils(object):
	# Generate random dataset and plot it 
	def initData(self):
		np.random.seed(0)
		X, y = datasets.make_moons(200, noise=0.20)
		plt.scatter(X[:,0], X[:,1], s=40, cmap=plt.cm.Spectral)
		plt.show()
		return X, y

	def normalizeData(self,X):
		min = np.min(X, axis=0)
		max = np.max(X, axis=0)
		normX = 1 - ((max - X) / (max-min))
		return normX


