import matplotlib.pyplot as plt
import numpy as np
import math

max=100

citer=60
rangc=5
circmin=2
circxcol=[] #startx
circycol=[] #starty
radcol=[] #0
n = 64 #64 edges

impo=0

# The basics of circle generation courtesy of YouTuber "NCLabEdTech"
for i in range(0, citer):
    rad = rangc*np.random.rand()+circmin #circle radius
    disx=max*np.random.rand()
    disy=max*np.random.rand()
    t=np.linspace(0, 2*np.pi, n+1) #circle broken into n+1 parts
    x=rad*np.cos(t)+disx
    y=rad*np.sin(t)+disy

    circxcol.append(disx)
    circycol.append(disy)

    radcol.append(rad)
    # Fill Between technique courtesy of YouTuber "Fluidic Colors"
    plt.fill_between(x, y, disy, color='k')
    plt.plot(x, y, 'k')
    plt.axis([0, max, 0, max])

dist=1.0
maxhyp=math.sqrt(2*(max*max))
count=0
sensitivity=.5
hwin=[]
startx=max*np.random.rand()
starty=max*np.random.rand()
endx=max*np.random.rand()
endy=max*np.random.rand()
m=0
p=0
sintersect=0
eintersect=0

while m==0:
    for o in range (0, citer):
        if (startx-circxcol[o])*(startx-circxcol[o]) + (starty-circycol[o])*(starty-circycol[o]) <= (radcol[o])*(radcol[o]):
            sintersect = sintersect + 1
    if sintersect > 0:
        startx=max*np.random.rand()
        starty=max*np.random.rand()
        sintersect=0
    else:
        m=1

while p==0:
    for q in range (0, citer):
        if (endx-circxcol[q])*(endx-circxcol[q]) + (endy-circycol[q])*(endy-circycol[q]) <= radcol[q]*radcol[q]:
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
while True: #while xfinal < endx-sensitivity or xfinal > endx+sensitivity or yfinal < endy-sensitivity or yfinal > endy+sensitivity:

    for p in range (0, citer):
        ax=result[-1][0]
        ay=result[-1][1]
        bx=endx
        by=endy
        cx=circxcol[p]
        cy=circycol[p]
        r=radcol[p]
        ax =ax - cx
        ay = ay-cy
        bx = bx-cx
        by = by-cy
        c = ax*ax + ay*ay - r*r
        b = 2*(ax*(bx - ax) + ay*(by - ay))
        a = (bx - ax)*(bx-ax) + (by - ay)*(by-ay)
        disc = b*b - 4*a*c
        if disc <=0:
            goodpath=1
        else:
            sqrtdisc = math.sqrt(disc)
            t1 = (-b + sqrtdisc)/(2*a)
            t2 = (-b - sqrtdisc)/(2*a)
            if((0 < t1 and t1 < 1) or (0 < t2 and t2 < 1)):
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

#Courtesy of ryu jin here: https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter
    for l in range(0, citer):
        ax=hnew[0][0]
        ay=hnew[0][1]
        bx=xfinal
        by=yfinal
        cx=circxcol[l]
        cy=circycol[l]
        r=radcol[l]
        ax =ax - cx
        ay = ay-cy
        bx = bx-cx
        by = by-cy
        c = ax*ax + ay*ay - r*r
        b = 2*(ax*(bx - ax) + ay*(by - ay))
        a = (bx - ax)*(bx-ax) + (by - ay)*(by-ay)
        disc = b*b - 4*a*c
        if disc <=0:
            intersect=1
            impo=0
        else:
            sqrtdisc = math.sqrt(disc)
            t1 = (-b + sqrtdisc)/(2*a)
            t2 = (-b - sqrtdisc)/(2*a)
            if((0 < t1 and t1 < 1) or (0 < t2 and t2 < 1)):
                intersect=0 #DOES intersect!
                break
            else:
                intersect=1
                impo=0

    if intersect==0: #1
        count=count-1
        impo=impo+1
    else:
        hwin.append(resultjt)
        hwin.append([xfinal, yfinal])
        result.append([xfinal, yfinal])
        plt.plot([hnew[0][0],result[-1][0]], [hnew[0][1],result[-1][1]], 'b',) # [hnew[0][0],result[-1][0]], [hnew[0][1], result[-1][1]], 'bo',
        plt.axis([0, max, 0, max])
        impo=0
    if impo==400:
        print('impossible at iteration #' + str(citer))

plt.plot([xfinal, hnew[0][0]], [yfinal, hnew[0][1]], 'c')
px=hnew[0][0]

while px != startx:
    for k in range(0, len(hwin)/2):
        if hwin[2*k+1][0]==px:
            ploc=hwin[2*k]
            cloc=hwin[2*k+1]
            px=hwin[2*k][0]
            plt.plot([cloc[0], ploc[0]], [cloc[1], ploc[1]], 'c')
            break

plt.plot(startx, starty, 'xr')
plt.plot(endx, endy, 'xg')
plt.show()
