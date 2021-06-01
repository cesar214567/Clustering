import numpy as np
import math
import matplotlib.pyplot as mp
from random import random, randrange
from PIL import Image
import random
from scipy import spatial
#https://rtree.readthedocs.io/en/latest/install.html#nix
#https://libspatialindex.org/en/latest/#current-release-mit
#https://stackoverflow.com/questions/3493061/how-do-range-queries-work-in-pythons-kd-tree

def dist(a, b):
    return math.dist(a,b)    

class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = 0
        self.dimensions = len(self.point)


class Cluster:
    def __init__(self,tupla,r):
        self.point = list(tupla)
        self.items = []
        self.r = r 
    def moveCenter(self):
        tempnode = self.items[0]
        for dimension in range(tempnode.dimensions):
            average = 0
            for node in self.items:
                if(isinstance(node, Node)):
                    average += node.point[dimension]
            average = average/len(self.items)
            self.point[dimension] = average

    def getItems(self,tree,nodes):
        data =tree.query_ball_point(self.point,self.r)
        self.items = [Node(nodes[item].point) for item in data]
        return self.items

    def recalc(self, iters,tree,nodes):
        print(self.point)
        for i in range(iters):
            self.getItems(tree,nodes)
            self.moveCenter()
        print(self.point)
def MeanShift(pix_val):
    nodes=[]
    tree =spatial.KDTree(pix_val)

    for item in pix_val:
        nodes.append(Node(item))

    clusters = []
    size = len(nodes)
    K = 3
    r = 20 
    for i in range(K):
        #clusters.append(Cluster(nodes[random.randint(0,size)].point,r))
        clusters.append(Cluster(nodes[random.randint(size*i/K,size*(i+1)/K)].point,r))

    for cluster in clusters:
        cluster.recalc(100,tree,nodes)
