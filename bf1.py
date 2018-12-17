from statistics import mean
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
import random
style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6] , dtype=np.float64)

ys = np.array([5,4,6,4,5,7] , dtype=np.float64)

def create_dataset(hm, variance, step = 2, correlation = False):
	val = 1
	ys=[]
	for i in range(hm):
		y = val+ random.randrange(-variance , variance)
		ys.append(y)
		if correlation and correlation  == 'pos':
			val+= step
		elif correlation and correlation == 'neg':
			val-= step
		xs = [i for i in range(len(ys))]

	return np.array(xs, dtype = np.float64) , np.array(ys, dtype = np.float64)
def best_fit_slope_i(xs,ys):
	m = ((mean(xs)*mean(ys)) - mean(xs*ys))/(mean(xs)*mean(xs) - mean(xs*xs))
	b = mean(ys) - m*mean(xs)
	return m ,b

def r_squared(ys_orig, ys_line):
	return sum((ys_line - ys_orig) * (ys_line - ys_orig))

def coefficient(ys_orig, ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	error_regression = r_squared(ys_orig, ys_line)
	error_mean  = r_squared(ys_orig, y_mean_line)
	return 1 - error_regression / error_mean

xs, ys = create_dataset(40,20,2,'pos')
m ,b  = best_fit_slope_i(xs,ys)
print(m)
print(b)
regression_line = [(m*x) + b for x in xs]
error_coefficient = coefficient(ys, regression_line) 
print(error_coefficient)
plt.scatter(xs,ys)
plt.plot(xs, regression_line)

plt.show()