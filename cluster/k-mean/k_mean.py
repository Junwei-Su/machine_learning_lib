"""
knn_cluster:
start with y class
given a new object x, find its closest k neighbors from the given class
among the k neighbors, count the number from each class and label the new point
with the class with most elements in that k neighbors

purpose:

fucntions:

"""

import string
import math

class Point:
    def __init__(self,label, x, y):
        self.label, self.x, self.y = label, x, y


class Knn_cluster(object):
    
    def __init__(self,cl):
        self.classes_list = cl

    def distance(self, point1, point2):
        x_diff      = abs(point1.x - point2.x)
        y_diff      = abs(point1.y - point2.y)
        square_sum  = math.pow(x_diff,2) + math.pow(x_diff,2)
        return math.pow(square_sum,0.5)

    def knn(self,cl,np):
        #how to find the k nearest point efficiently
        





def main():
    cl = []
    p1   = Point("1",1,1)
    p2   = Point("2",2,2)
    test = Knn_cluster(cl)
    dist = test.distance(p1,p2)
    print(dist)

if __name__ == '__main__':
    main()


