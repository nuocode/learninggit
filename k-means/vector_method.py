# -*- coding: iso-8859-15 -*-

import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial, reduce

def vector_add(v,w):
    return [v_i+w_i for v_i,w_i in zip(v,w)]

#两向量相减
def vector_substract(v,w):
    return [v_i-w_i for v_i,w_i in zip(v,w)]

#多向量相加
def vector_sum(*vectors):
    return reduce(vector_add,vectors)

#标量与向量相乘
def scalar_multiply(c,v): #c is number , v is vector
    return [c*v_i for v_i in v]

#计算向量均值
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))


#向量的点积之和，代表v在w上的投影
def dot(v,w):
    return sum(v_i * w_i for v_i,w_i in zip(v,w))


#利用点积之和计算向量的平方和
def sum_of_squares(v):
    return dot(v,v)

##### 导入math #####
#计算向量的长度
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    return sum_of_squares(vector_substract(v,w)) #差的平方和

def distance(v,w):
    return math.sqrt(squared_distance(v,w)) # 平方和开根号得到距离
