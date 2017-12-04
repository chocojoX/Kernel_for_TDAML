import numpy as np
import random
import matplotlib.pyplot as plt


def create_new_point_at_distance(p, distance):
    x, y = p
    is_ok = False
    cpt = 0
    while cpt<100 and not is_ok:
        theta = 2*np.pi * random.random()
        quadrant = int((theta + np.pi/4)/(np.pi/2))%4
        if quadrant == 0:
            new_point = [x+distance, y + distance * np.sin(theta)/np.cos(theta)]
        if quadrant == 1:
            new_point = [x + distance * np.cos(theta)/np.sin(theta) , y + distance]
        if quadrant == 2:
            new_point = [x - distance, y - distance * np.sin(theta)/np.cos(theta)]
        if quadrant == 3:
            new_point = [x - distance * np.cos(theta)/np.sin(theta) , y - distance]
        if new_point[1]>new_point[0] and new_point[0]>=0:
            is_ok = True
    if not is_ok:
        return None
    return new_point


def infinite_dist(p, new_point):
    return max(np.abs(p[0]-new_point[0]), np.abs(p[1]-new_point[1]))


def distance_to_diagonal(p):
    return p[1]-p[0]


class Persistence_diagram(object):
    def __init__(self, points=[], high = 10):
        self.high = 10
        self.points = []
        for p in points:
            x, y = p
            if y>x:
                self.points.append(p)
        # No infinite points in the digram for this work...

    def bottleneck_distance(self, diagram2):
        pass
        # TODO (or not TODO)


    def add_point(self, p):
        self.points.append(p)


    def create_close_diagram(self, n_points=10, distance=1, high=None):
        """ Returns a daigram with at least n_points points that is at a Wasserstein (infinite) distance of exactly distance of the given persistence diagram """

        if high is None:
            high = self.high
        new_diagram = Persistence_diagram()
        p_diag = random.random() # proportion of points that will be closer than "distance" from the diagonal

        # Step 1 find the point that will maximize the bottleneck distance
        found = False
        while not found:
            start_point = random.choice(self.points)
            new_point = create_new_point_at_distance(start_point, distance)
            if new_point is not None:
                found = True
                for p in self.points:
                    if infinite_dist(p, new_point)<distance:
                        found = False
                        break
        new_diagram.add_point(new_point)

        # Step 2 : Link each point of the original daigram to a point in the new one
        # except if these points are close to the diagonal or are the new point itself

        close_to_diag_points = 0
        for p in self.points:
            if p is not start_point:
                if distance_to_diagonal(p)>distance:
                    dist = distance*random.random()
                    new_point = create_new_point_at_distance(p, dist)
                    new_diagram.add_point(new_point)

                else:
                    close_to_diag_points += 1
                    dist = distance*random.random()
                    proba = random.random()
                    if proba>p_diag:
                        new_point = create_new_point_at_distance(p, dist)
                        new_diagram.add_point(new_point)

        # Step 3 add some noisy points close enough to the diagonal
        for i in range(int(p_diag*close_to_diag_points)):
            y = high * random.random()
            x = y - distance * random.random()
            new_diagram.add_point([x, y])

        return new_diagram


    def get_symmetricized_diagram(self):
        symmetric_diagram = persistence_diagram()
        for p in self.points:
            symmetric_diagram.add_point(p)
            symmetric_diagram.add_point([-p[0], -p[1]])

        return symmetric_diagram


    def kernel_value(self, diag2, sigma):
        val = 0
        for p1 in self.points:
            for p2 in diag2.points:
                x, y = p1
                x2, y2 = p2
                val += 1/(8*np.pi*sigma) * ( np.exp(-((x-x2)**2 + (y-y2)**2)/(8*sigma)) -
                                             np.exp(-((x-y2)**2 + (y-x2)**2)/(8*sigma)) )
        return val



    def compute_W1(self, diag2):
        # TODO
        pass
