from DBSCAN import DBSCAN
from KMeans import KMeans
from MeanShift import MeanShift

filename = "db/Y100.JPG"

print("----------------DBSCAN---------------")
DBSCAN(filename)
print("----------------KMeans---------------")
KMeans()
print("--------------Mean Shift-------------")
MeanShift()
