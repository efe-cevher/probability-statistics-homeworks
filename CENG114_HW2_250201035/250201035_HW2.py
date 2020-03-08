#Student_ID = 250201035
import numpy as np
from matplotlib import pyplot as plt

def plot(data,color,title):
    plt.figure()
    plt.plot(data,color)
    plt.title(title)
    plt.grid(b=True, axis='both')


# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
total = 0
var_top = 0
var = 0
for i in range(50000):
    u = np.random.rand()
    x = u**(1/2)
    U.append(u)
    Xa.append(x)
    total += x
    avg = total/(i+1)
    var_top += (x - avg)**2
    if i != 0:   
        var = var_top / i
    av_Xa.append(avg)
    vr_Xa.append(var)
   


# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
    
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))


# Plot the average and variance values.

plot(av_Xa,"g.","Average of Xa")
plot(vr_Xa,"r.","Variance of Xa")


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.


naccept = 0   
total = 0
var_top = 0 
var = 0
i = 0

while naccept<50000:
    x=np.random.rand()
    y=np.random.rand()*2

    if y<2*x:  
        Xb.append(x)  
        naccept=naccept+1
        total += x
        avg = total/(i+1)
        var_top += (x - avg)**2
        if i != 0:   
            var = var_top / i
        av_Xb.append(avg)
        vr_Xb.append(var)
        i += 1
    

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.

plot(av_Xb,"g.","Average of Xb")
plot(vr_Xb,"r.","Variance of Xb")

plt.show()

