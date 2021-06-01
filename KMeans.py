import numpy as np
import math
import matplotlib.pyplot as mp
from random import random, randrange
from PIL import Image
import random


class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = 0
        self.dimensions = len(self.point)
        

class Cluster:
    def __init__(self,tupla):
        self.point = list(tupla)
        self.items = []
    def moveCenter(self):
        tempnode = self.items[0]
        for dimension in range(tempnode.dimensions):
            average = 0
            for node in self.items:
                if(isinstance(node, Node)):
                    average += node.point[dimension]
            average = average/len(self.items)
            self.point[dimension] = average

def dist(a, b):
    return math.dist(a,b)

def KMeans(pix_val):
    nodes=[]
    for item in pix_val:
        nodes.append(Node(item))

    clusters = []
    size = len(nodes)
    K = 3
    for i in range(K):
        clusters.append(Cluster(nodes[random.randint(size*i/K,size*(i+1)/K)].point))
    for i in clusters:
        print(i.point)

    for node in nodes:
        minimum = dist(node.point, clusters[0].point)
        node.cluster = 0
        for i in range(len(clusters)):
            distance = dist(node.point, clusters[i].point)
            if (distance < minimum):
                minimum = distance
                node.cluster = i
            clusters[node.cluster].items.append(node)

    for cluster in clusters:
        cluster.moveCenter()
    for i in clusters:
        print(i.point)
