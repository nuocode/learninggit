import numpy as np
from vector_method import vector_mean, dot, sum_of_squares, vector_substract, squared_distance
import math, random
from matplotlib import pyplot as plt

#导入数据
X = [-50,-50,-48,-40,-35,-26,-22,-19,-18,-15,-14,-12,-10,-9,10,12,17,20,21,26]
Y = [0,15,5,8,-2,-10,-18,-11,-3,-5,-6,-7,-20,-18,15,14,28,26,22,12]
input = list(zip(X,Y))
print(input)


#通用方法
class KMeans(object):
    def __init__(self,k):
        self.k = k #聚类的数目
        self.means = None #聚类的均值

    def classify(self,input):
        return min(range(self,k),key=lambda i:squared_distance(input,self.means[i]))

    def train(self,inputs):
        #随机选择质心
        self.means = random.sample(inputs,self.k)

        assignments = None
        while True:
            #查找新分配
            new_assignments = map(self.classify,inputs)

            #如果所有数据点不再被重新分配，那么就停止
            if assignments == new_assignments:
                return

            #基于新的分配计算新的均值
            for i in range(self,k):
                #查找分配给聚类i的所有的点
                i_points = [p for p,a in zip(inputs,assignments) if a ==i]

                # 确保i_point不是空的，因此除数不为0
                if i_points:
                    self.means[i] = vector_mean(i_points)

#把图画出来
plt.scatter(X, Y,marker="o")
plt.title("Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

random.seed(0)
clusterer = KMeans(3)
custerer.train(inputs)
print(cluster.means)
