# -*- coding: utf-8 -*-
"""
@author: Efe Can Cevher
stdID: 250201035
"""

import numpy as np
from matplotlib import pyplot as plt


def MoM(sample):
    m = np.average(sample)
    x = -m/(m-1)
    return x


def MLE(sample):

    product = 1
    for entry in sample:
        product = product * entry
    x = -(len(sample)) / np.log(product)
    return x

def func(population, sampleSize):
    samples = []
    momEst = []
    mleEst = []
    
    
    for i in range(100000):
        ranIntegers = np.random.randint(0,len(population)-1,size=sampleSize)
        sample = []
        for ranInt in ranIntegers:
            sample.append(population[ranInt])
        samples.append(sample)
        momEst.append(MoM(sample))
        mleEst.append(MLE(sample))
        
        
    plt.figure()
    plt.hist(momEst,100,alpha=0.5)
    plt.hist(mleEst,100,alpha=0.5)
    plt.show()
    
    print("mean of MoM est ")
    print(np.average(momEst))
    print("mean of MLE est ")
    print(np.average(mleEst))
    print("var of MoM est ")
    print(np.var(momEst))
    print("var of MLE est ")
    print(np.var(mleEst))


#Generate population
P = [] 
for i in range(10000000):
    u = np.random.rand()
    p = u**(1/2.4)
    P.append(p)
    
    


for N in [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]:
    print("\n \n Results for N = " + str(N))
    func(P, N)
    
    
    
    
    

