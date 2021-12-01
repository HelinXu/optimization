import random
from copy import deepcopy
from time import time
from math import sqrt


def get_distance(p1, p2):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )


class tsp():
    def __init__(self, num_points=10, width=100, point_file=None):
        self.num_points = num_points
        self.width = width
        self.point_list = []
        if point_file == None:
            random.seed(int(time()))
            for i in range(self.num_points):
                self.point_list.append((random.randint(0, self.width), random.randint(0, self.width)))
        else:
            pass
        self.distance = self.total_distance()
        self.best_point_list = deepcopy(self.point_list)
        self.best_distance = self.distance


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
        if self.distance < self.best_distance:
            self.best_distance = self.distance
            self.best_point_list = deepcopy(self.point_list)
        return


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
