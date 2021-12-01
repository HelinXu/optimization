# simulated annealing search of a one-dimensional objective function
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot as plt
from math import *
import numpy as np
from time import time

# objective function
def objective(x):
	return -np.exp(-(x/30.)**2.0) * np.cos(x)

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
	# generate an initial point
	best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate the initial point
	best_eval = objective(best)
	# current working solution
	curr, curr_eval = best, best_eval
	scores = list()
	# run the algorithm
	for i in range(n_iterations):
		# take a step
		candidate = curr + randn(len(bounds)) * step_size
		# evaluate candidate point
		candidate_eval = objective(candidate)
		# check for new best solution
		if candidate_eval < best_eval:
			# store new best point
			best, best_eval = candidate, candidate_eval
			# keep track of scores
			scores.append(best_eval)
			# report progress
			print('>%d f(%s) = %.5f' % (i, best, best_eval))
		# difference between candidate and current point evaluation
		diff = candidate_eval - curr_eval
		# calculate temperature for current epoch
		t = temp / float(i + 1)
		# calculate metropolis acceptance criterion
		metropolis = exp(-diff / t)
		# check if we should keep the new point
		if diff < 0 or rand() < metropolis:
			# store the new current point
			curr, curr_eval = candidate, candidate_eval
	return [best, best_eval, scores]


if __name__ == '__main__':
    # plotting the function
    x = np.arange(-30, 30, 0.1)
    plt.plot(x, objective(x))
    plt.show()
    # seed the pseudorandom number generator
    seed(int(time()))
    # define range for input
    bounds = asarray([[-30.0, 30.0]])
    # define the total iterations
    n_iterations = 2000
    # define the maximum step size
    step_size = 5.
    # initial temperature
    temp = 10
    # perform the simulated annealing search
    best, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
    print('Done!')
    print('f(%s) = %f' % (best, score))
    # line plot of best scores
    plt.plot(scores, '.-')
    plt.xlabel('Improvement Number')
    plt.ylabel('Evaluation f(x)')
    plt.show()