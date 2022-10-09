

print("hello cluster")

from scipy.cluster.vq import kmeans,vq, whiten
from numpy import array, vstack
from numpy.random import rand

a = rand(100,3) + array([.5,.5,.5])
print(a)
b = rand(100,3)
data = vstack((a,b))
print(data.shape)

data = whiten(data)

centroids, _ = kmeans(data,3)
print(centroids)

clx, _ = vq(data, centroids)
print(clx)
