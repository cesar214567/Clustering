from DBSCAN import DBSCAN
from KMeans import KMeans
from MeanShift import MeanShift
from PIL import Image
from scipy import misc
import numpy as np

def read_db():
    file = open("files.txt","r")
    for line in file:
        print(line)
        points = []
        im = Image.open(line[:-1], 'r')
        pix_val=list(im.getdata())
        #pix_val = im.convert("RGB")
        #pix_val=list([] im.getdata())
        pix_val = np.array(im)
        h,w = len(pix_val),len(pix_val[0])
        for y in range(h):
            for x in range(w):
                points.append((x*2.5, y*2.5, pix_val[y][x]/2))
        print("----------------DBSCAN---------------")
        DBSCAN(points)
        #print("----------------KMeans---------------")
        #KMeans(points,w,h)
        #print("--------------Mean Shift-------------")
        #MeanShift(pix_val)
        break

read_db()
