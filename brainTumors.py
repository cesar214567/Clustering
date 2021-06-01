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
        for y in range(len(pix_val)):
            for x in range(len(pix_val[0])):
                points.append((x, y, pix_val[y][x]))
        print("----------------DBSCAN---------------")
        DBSCAN(points)
        print("----------------KMeans---------------")
        KMeans(points)
        print("--------------Mean Shift-------------")
        MeanShift(pix_val)
        break

read_db()
