import random
from copy import deepcopy
from time import time
from math import sqrt
from numpy.random import rand, randn
from numpy import exp

def get_distance(p1, p2):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )


class tsp():
    def __init__(self, num_points=30, width=1000, point_file=None):
        self.num_points = num_points
        self.width = width
        self.point_list = []
        if point_file == None:
            random.seed(int(time()))
            for i in range(self.num_points):
                self.point_list.append((random.randint(0, self.width), random.randint(0, self.width)))
        else:
            self.read_points(point_file)
        self.distance = self.total_distance()
        self.best_point_list = [deepcopy(self.point_list), ]
        self.best_distance = [(self.distance, 0), ]

    def total_distance(self):
        dis = get_distance(self.point_list[0], self.point_list[-1])
        for i in range(self.num_points-1):
            dis += get_distance(self.point_list[i], self.point_list[i+1])
        return dis

    def swap(self, i, j, delta_distance):
        tmp = self.point_list[i]
        self.point_list[i] = self.point_list[j]
        self.point_list[j] = tmp
        self.distance += delta_distance

    def delta_distance(self, i, j):
        d = 0
        d -= (
            get_distance(self.point_list[i], self.point_list[(i+1)%self.num_points]) +
            get_distance(self.point_list[i-1], self.point_list[i]) +
            get_distance(self.point_list[j], self.point_list[(j+1)%self.num_points]) +
            get_distance(self.point_list[j-1], self.point_list[j])
        )
        d += (
            get_distance(self.point_list[j], self.point_list[(i+1)%self.num_points]) +
            get_distance(self.point_list[i-1], self.point_list[j]) +
            get_distance(self.point_list[i], self.point_list[(j+1)%self.num_points]) +
            get_distance(self.point_list[j-1], self.point_list[i])
        )
        return d

    def rand_pair(self):
        pair = random.sample(range(self.num_points), 2)
        while abs(pair[1] - pair[0]) == 1 or abs(pair[1] - pair[0]) == self.num_points - 1:
            pair = random.sample(range(self.num_points), 2)
        return pair
    
    def sim_ann(self, n_iterations=10000, temperature=1000):
        for i in range(n_iterations):
            # take a step: random swap
            candidate_pair = self.rand_pair()
            # evaluate candidate
            candidate_del_dis = self.delta_distance(candidate_pair[0], candidate_pair[1])
            self.swap(candidate_pair[0], candidate_pair[1], candidate_del_dis)
            # check for new best solution
            if self.best_distance[-1][0] > self.distance:
                # update and record scores
                self.best_distance.append((self.distance, i+1))
                self.best_point_list.append(deepcopy(self.point_list))
                print(f'>{i}: swap {candidate_pair[0]}, {candidate_pair[1]}, best dist = {self.best_distance[-1]}')
            # calculate temperature for current epoch
            t = temperature / float(i + 1)
            # calculate metropolis acceptance criterion
            metropolis = exp(-candidate_del_dis / t)
            # check if we should keep the new point
            if candidate_del_dis < 0 or rand() < metropolis: # by chance of metropolis, accept worse solution
                pass # accept new solution
            else: # undo
                self.swap(candidate_pair[0], candidate_pair[1], -candidate_del_dis)  
            assert abs(self.distance - self.total_distance()) < 1e-7, f'iter {i}:swap{candidate_pair[0]},{candidate_pair[1]} {self.distance} != {self.total_distance()}'

    def save_best_result(self, filename=None):
        if filename is None: filename = f'tcp_{self.num_points}.txt'
        f = open(filename, 'w')
        for point in self.best_point_list[-1]:
            f.write(f'{point[0]} {point[1]}\n')
        f.close()
    
    def read_points(self, filename=None):
        f = open(filename, 'r')
        for line in f.readlines():
            line = line.split(' ')
            self.point_list.append((int(line[0]), int(line[1])))


tsp = tsp(num_points=60, point_file='tcp_60.txt')
print(tsp.distance)
tsp.sim_ann(temperature=1000000, n_iterations=1000000)
print(tsp.distance)
print(tsp.best_distance)
tsp.save_best_result()

