#Student_ID = 250201035
import numpy as np
import matplotlib.pyplot as plt

print("Please wait, shouldnt take more than 30 second.")

def plothist(data,title):
    plt.figure()
    plt.hist(data, 50)
    plt.grid(b=True, axis='both', linewidth=0.2)
    plt.title(title)
    plt.show()

def plot(data,color,title):
    plt.plot(data,color)
    plt.title(title)
    plt.grid(b=True, axis='both')
    plt.show()


A = []
B = []
C = []
X = []
Xvar = []
Aavg = []
Bavg = []
Cavg = []
Xavg = []

tmp = 0
for i in range(100000):
    ran = np.random.rand()
    if ran < 1/6 :
        a = 1
    elif 1/6 <= ran < 2/6:
        a = 2
    elif 2/6 <= ran < 3/6:
        a = 3
    elif 3/6 <= ran < 4/6:
        a = 4
    elif 4/6 <= ran < 5/6:
        a = 5
    else:
        a = 6

    ran = np.random.rand()

    A.append(a)

    if ran < 1/4:
        b = 1
    elif 1/4 <= ran < 2/4:
        b = 2
    elif 2/4 <= ran < 3/4:
        b = 3
    else:
        b = 4

    B.append(b)

    ran = np.random.rand()

    if ran < 1/2:
        c = 1
    else:
        c = -1

    C.append(c)

    x = a + b * c

    X.append(x)

    tmp += 1
    #It takes forever if update avg and var each simulation to fix that updated avg and var values 2000 times total.
    if tmp%50 == 0:
        Xvar.append(np.var(X))
        Aavg.append(np.average(A))
        Bavg.append(np.average(B))
        Cavg.append(np.average(C))
        Xavg.append(np.average(X))


plothist(A,"Histogram of A")
plothist(B,"Histogram of B")
plothist(C,"Histogram of C")
plothist(X,"Histogram of X")

plot(Aavg,"g.","Average Value of A")
plot(Bavg,"g.","Average Value of B")
plot(Cavg,"g.","Average Value of C")
plot(Xavg,"g.","Average Value of X")
plot(Xvar,"r.","Variance of X")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               


