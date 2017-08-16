#!/home/ranjan/anaconda2/bin/python

# monte carlo method to evaluate value of pi
# using Markov Chain Monte Carlo method 

from random import uniform
import math

def get_num_hits(samples):
	""" generates samples from mcmc and return number of hits withing circular area of 1"""
	hits = 0
	x = 1
	y = 1
	for i in range(samples):
		delta_x = uniform(-0.1,0.1)
		delta_y = uniform(-0.1,0.1)

		if abs(x + delta_x) < 1 and abs(y + delta_y) < 1 :
			x = x + delta_x
			y = y + delta_y
			

		if x*x + y*y < 1:
			hits = hits + 1

	print(hits)
	return hits;


if __name__ == '__main__':
	samples = 10000
	print(get_num_hits(samples)*4/float(samples))



