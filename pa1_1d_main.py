from function.d1_simulated_annealing import simulated_annealing
import argparse
import os
import numpy as np
from statistics import mean, variance
from numpy import asarray
from numpy.random import seed
from matplotlib import pyplot as plt
from math import *
import numpy as np
from time import time

# objective function
def objective(x):
    return -np.exp(-(x/30.)**2.0) * np.cos(x)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--o', '--output_root', help='path to the output files', default='./sa_1d_results')
    opt = parser.parse_args()

    os.system(f'mkdir {opt.o}')
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

    result_dist_list = []
    for i in range(20):
        # perform the simulated annealing search
        best, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
        result_dist_list.append(float(score))

    # get results and save to file
    print(sorted(result_dist_list, key = lambda x:float(x)))
    print(len(result_dist_list))
    mean_results = mean(result_dist_list)
    var_results = variance(result_dist_list)
    print(f'mean: {mean_results}, var: {var_results}')
    f = open(os.path.join(opt.o, 'result.txt'), 'a')
    f.write(f'20 time resluts: {sorted(result_dist_list, key = lambda x:float(x))}')
    f.write(f'\nmean: {mean_results}, var: {var_results}')
    f.write('\n\n')
    f.close()