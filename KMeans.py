import numpy as np
import math
import matplotlib.pyplot as mp
from random import random, randrange
from PIL import Image
import random
from scipy.spatial import distance


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
    return distance.euclidean(a,b)

def get_nearests(nodes,clusters):
    for node in nodes:
        minimum = dist(node.point, clusters[0].point)
        node.cluster = 0
        for i in range(len(clusters)):
            distance = dist(node.point, clusters[i].point)
            if (distance < minimum):
                minimum = distance
                node.cluster = i
            clusters[node.cluster].items.append(node)

def while_loop(nodes, clusters,iters=None):
    if (iters==None):
        return clusters
    else:
        for i in range(iters):
            get_nearests(nodes,clusters)
            for cluster in clusters:
                cluster.moveCenter()
                cluster.items.clear()


def KMeans(points,w,h):
    
    nodes=[]
    '''
    im = Image.open(filename, 'r')
    w,h=im.size
    im2 = Image.new('RGB',(w,h))
    pix_val=list(im.getdata())
    index= 0
    for item in pix_val:
        point =[index//h,index%h]
        if isinstance(item,list):
            point.extend(list(item))
        else:
            point.append(item)
        index+=1
        nodes.append(Node(point))
    '''
    im2 = Image.new('RGB',(w,h))
    for point in points:
        nodes.append(Node(point))
    clusters = []
    size = len(nodes)
    K = 5
    for i in range(K):
        clusters.append(Cluster(nodes[random.randint(size*i//K,size*(i+1)//K)].point))
    for i in clusters:
        print(i.point)
    while_loop(nodes,clusters,1)
    for i in clusters:
        print(i.point)
    while_loop(nodes,clusters,15)
    get_nearests(nodes,clusters)
    returning_points=[]
    for cluster in clusters:
        R=randrange(255)
        G=R
        B=G
        #G=randrange(255)
        #B=randrange(255)
        for node in cluster.items:
            #print((node.point[0],node.point[1]))
            returning_points.append((node.point[1],node.point[0]))
            im2.putpixel((node.point[1],node.point[0]),(R,G,B))
    
    #im.show()
    im2.show()
    im2.save('images3.png')
    #im.show()


    return returning_points
    
    
    '''for node in nodes:
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
'''
    
