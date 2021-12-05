from function.d2_simulated_annealing import simulated_annealing
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
def objective(x, y):
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * 
            pi * x)+cos(2 * pi * y))) + e + 20

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--o', '--output_root', help='path to the output files', default='./sa_results')
    opt = parser.parse_args()

    os.system(f'mkdir {opt.o}')
    r_min, r_max = -10, 10
    # seed the pseudorandom number generator
    seed(int(time()))
    # define range for input
    bounds = asarray([[r_min, r_max], [r_min, r_max]])
    # define the total iterations
    n_iterations = 10000
    # define the maximum step size
    step_size = 2.
    # initial temperature
    temp = 100
    print('Done!')

    result_dist_list = []
    for i in range(20):
        # perform the simulated annealing search
        best, score, scores, points = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
        result_dist_list.append(float(score))

    # get results and save to file
    print(sorted(result_dist_list, key = lambda x:float(x)))
    print(len(result_dist_list))
    mean_results = mean(result_dist_list)
    var_results = variance(result_dist_list)
    print(f'mean: {mean_results}, var: {var_results}')
    f = open(os.path.join(opt.o, 'result_2d.txt'), 'a')
    f.write(f'20 time resluts: {sorted(result_dist_list, key = lambda x:float(x))}')
    f.write(f'\nmean: {mean_results}, var: {var_results}')
    f.write('\n\n')
    f.close()