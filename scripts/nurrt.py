import matplotlib.pyplot as plt
import numpy as np
import math

max=98
obstacle=[]
imx = plt.imread('./N_map.png')
im=np.fliplr(imx)
plt.imshow(im)
plt.axis([0, 100, 0, 100])
for i in range (0, 99):
    for j in range (0, 99):
        if float(format(im[j, i, 0])) == 0.0:
            obstacle.append([i, j])

dist=1.0
maxhyp=math.sqrt(2*(max*max))
count=0
sensitivity=.5
hwin=[]
startx=40 #max*np.random.rand()
starty=40 #max*np.random.rand()
endx=60 #max*np.random.rand()
endy=60 #max*np.random.rand()
m=0
p=0
sintersect=0
eintersect=0

while m==0:
    for o in range (0, len(obstacle)):
        cx=obstacle[o][0]
        cy=obstacle[o][1]
        if (startx<cx+sensitivity and startx>cx-sensitivity and starty<cy+sensitivity and starty>cy-sensitivity):
            sintersect = sintersect + 1
    if sintersect > 0:
        startx=max*np.random.rand()
        starty=max*np.random.rand()
        sintersect=0
    else:
        m=1

while p==0:
    for q in range (0, len(obstacle)):
        cx=obstacle[q][0]
        cy=obstacle[q][1]
        if (endx<cx+sensitivity and endx>cx-sensitivity and endy<cy+sensitivity and endy>cy-sensitivity):
            eintersect=eintersect+1
    if eintersect > 0:
        endx=max*np.random.rand()
        endy=max*np.random.rand()
        eintersect=0
    else:
        p=1

result=[[startx, starty]]
unscal=[[startx, starty]]
hnew=[]
xfinal=-3
yfinal=-3
goodpath=1

while True:
    for r in range (0, len(obstacle)):
        ax=result[-1][0]
        ay=result[-1][1]
        bx=endx
        by=endy
        cx=obstacle[r][0]
        cy=obstacle[r][1]
        rslope=float(by-ay)/(bx-ax)
        xs1=1
        xs2=-1
        if rslope==xs1 or rslope==xs2:
            rslope=rslope+.0001
        rb=by-(rslope*bx)
        xb1=(cy+.5)-(xs1)*(cx+.5)
        xb2=(cy-.5)-(xs2)*(cx+.5)
        interx1=(xb1-rb)/(rslope-xs1)
        interx2=(xb2-rb)/(rslope-xs2)
        if ((ax<cx+sensitivity and ax>cx-sensitivity and ay<cy+sensitivity and ay>cy-sensitivity) or (bx<cx+sensitivity and bx>cx-sensitivity and by<cy+sensitivity and by>cy-sensitivity))or((interx1>ax or interx1>bx)and(interx1<ax or interx1<bx)and(interx1>(cx+.5) or interx1>(cx-.5))and(interx1<(cx+.5) or interx1<(cx-.5)))or((interx2>ax or interx2>bx)and(interx2<ax or interx2<bx)and(interx2>(cx+.5) or interx2>(cx-.5))and(interx2<(cx+.5) or interx2<(cx-.5))):
            goodpath=0
            break
        else:
            goodpath=1
    if goodpath==1:
        xfinal=endx
        yfinal=endy
        hnew=[result[-1]]
        break

    hcan=[maxhyp]
    xnew=max*np.random.rand()
    ynew=max*np.random.rand()
    unscal=[xnew, ynew]
    count=count+1
    for j in range(0, count):
        hyp=math.sqrt((unscal[0]-result[j][0])*(unscal[0]-result[j][0])+(unscal[1]-result[j][1])*(unscal[1]-result[j][1]))

        if hyp<hcan[-1]:
            hcan.append(hyp)
            resultjt = [result[j][0], result[j][1]]
            hnew=[resultjt, [unscal[0], unscal[1]]]

    permx=(unscal[0]-hnew[0][0])/hcan[-1]
    permy=(unscal[1]-hnew[0][1])/hcan[-1]
    xfinal=hnew[0][0]+permx
    yfinal=hnew[0][1]+permy

    for l in range(0, len(obstacle)):
        ax=hnew[0][0]
        ay=hnew[0][1]
        bx=xfinal
        by=yfinal
        cx=obstacle[l][0]
        cy=obstacle[l][1]
        rslope=float(by-ay)/(bx-ax)
        xs1=1
        xs2=-1
        if rslope==xs1 or rslope==xs2:
            rslope=rslope+.0001
        rb=by-(rslope*bx)
        xb1=(cy+.5)-(xs1)*(cx+.5)
        xb2=(cy-.5)-(xs2)*(cx+.5)
        interx1=(xb1-rb)/(rslope-xs1)
        interx2=(xb2-rb)/(rslope-xs2)
        if ((ax<cx+sensitivity and ax>cx-sensitivity and ay<cy+sensitivity and ay>cy-sensitivity) or (bx<cx+sensitivity and bx>cx-sensitivity and by<cy+sensitivity and by>cy-sensitivity))or((interx1>ax or interx1>bx)and(interx1<ax or interx1<bx)and(interx1>(cx+.5) or interx1>(cx-.5))and(interx1<(cx+.5) or interx1<(cx-.5)))or((interx2>ax or interx2>bx)and(interx2<ax or interx2<bx)and(interx2>(cx+.5) or interx2>(cx-.5))and(interx2<(cx+.5) or interx2<(cx-.5))):
            intersect=0 #DOES intersect
            break
        else:
            intersect=1
            impo=0

    if intersect==0:
        count=count-1
        impo=impo+1
    else:
        hwin.append(resultjt)
        hwin.append([xfinal, yfinal])
        result.append([xfinal, yfinal])
        plt.plot(startx, starty, 'xr')
        plt.plot(endx, endy, 'xg')
        plt.plot([hnew[0][0],result[-1][0]], [hnew[0][1],result[-1][1]], 'b',) # [hnew[0][0],result[-1][0]], [hnew[0][1], result[-1][1]], 'bo',
        plt.axis([0, max, 0, max])
        impo=0
        plt.pause(0.0001)
    if impo==400:
        print('impossible at iteration #' + str(citer))

plt.plot([xfinal, hnew[0][0]], [yfinal, hnew[0][1]], 'm')
px=hnew[0][0]

while px != startx:
    for k in range(0, len(hwin)/2):
        if hwin[2*k+1][0]==px:
            ploc=hwin[2*k]
            cloc=hwin[2*k+1]
            px=hwin[2*k][0]
            plt.plot([cloc[0], ploc[0]], [cloc[1], ploc[1]], 'm')
            break

#plt.plot(startx, starty, 'xr')
#plt.plot(endx, endy, 'xg')
plt.show()
