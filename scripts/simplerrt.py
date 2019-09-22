import matplotlib.pyplot as plt
import numpy as np
import imageio
import math

#k=5
qinit=50 #qinit = Initial Configuration
dist=1.0 #delata = Incremental distance
max=100 #D = The planning domain
iter=100 # K=number of vertices in RRT
count=0
result=[[qinit, qinit]]
unscal=[[qinit, qinit]]
#hmath=[[qinit, qinit]]
#ydist=math.sqrt(dist-(xdist*xdist))
for i in range(0, iter):
    hcan=[max] #h candidate: an array where, as far as the code has checked, the last value in the array is the smallest hypotenuse found so far
    xnew=max*np.random.rand()
    ynew=max*np.random.rand()
    unscal=[xnew, ynew]
    count=count+1
    for j in range(0, count):
        hyp=math.sqrt((unscal[0]-result[j][0])*(unscal[0]-result[j][0])+(unscal[1]-result[j][1])*(unscal[1]-result[j][1]))
        #hcomp.append(hyp)

        if hyp<hcan[-1]:
            hcan.append(hyp)
            hwin=[[result[j][0], result[j][1]], [unscal[0], unscal[1]]]
    permx=(unscal[0]-hwin[0][0])/hcan[-1]
    permy=(unscal[1]-hwin[0][1])/hcan[-1]
    result.append([hwin[0][0]+permx, hwin[0][1]+permy])
    plt.plot([hwin[0][0],result[-1][0]], [hwin[0][1],result[-1][1]], 'k',)
    #1st should be [hwin[0][0],result[-1][0]], [hwin[0][1], result[-1][1]], 'ro',
    plt.axis([0, max, 0, max])
plt.show()
