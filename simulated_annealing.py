# simulated annealing search of a one-dimensional objective function
from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import rand
from numpy.random import randn
from time import time
from numpy import arange, asarray, meshgrid

def objective(x, y):
 return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * 
  pi * x)+cos(2 * pi * y))) + e + 20

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # generate an initial point
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    best_eval = objective(best[0], best[1])
    # current working solution
    curr, curr_eval = best, best_eval
    scores = []
    points = [best, ]
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate = curr + randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective(candidate[0], candidate[1])
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best, best_eval = candidate, candidate_eval
            # keep track of scores
            scores.append(best_eval)
            points.append(best)
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
    return [best, best_eval, scores, points]


if __name__ == '__main__':
    r_min, r_max = -32.768, 32.768
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
    # perform the simulated annealing search
    best, score, scores, points = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
    print('Done!')
    print('f(%s) = %f' % (best, score))
    # line plot of best scores
    plt.plot(scores, '.-')
    plt.xlabel('Improvement Number')
    plt.ylabel('Evaluation f(x)')
    plt.show()

    
    xaxis = arange(r_min, r_max, 2.0)
    yaxis = arange(r_min, r_max, 2.0)
    x, y = meshgrid(xaxis, yaxis)
    results = objective(x, y)
    figure = plt.figure()
    axis = figure.gca( projection='3d')
    axis.plot_surface(x, y, results, cmap='jet', shade= "false")
    plt.show()
    plt.contour(x,y,results)
    plt.show()
    plt.scatter(x, y, results)
    plt.show()
