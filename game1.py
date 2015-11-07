import random
from graphics import *

#this function creates an NxN array filled with zeros
def empty(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[0]
        a=a+[b]
    return a

#this function fills the array a with a portion p of live cells
def fill(a,p):
    N=len(a)
    for i in range(N):
        for j in range(N):
            if random.uniform(0,1)<p:
                a[i][j]=1

def update(A,B):
    N=len(A)
    for i in range(N):
        for j in range(N):
            neigh=A[(i-1)%N][(j-1)%N]+A[(i-1)%N][j]+A[(i-1)%N][(j+1)%N]+A[i][(j-1)%N]+A[i][(j+1)%N]+A[(i+1)%N][(j-1)%N]+A[(i+1)%N][j]+A[(i+1)%N][(j+1)%N]
            if A[i][j]==0:
                if neigh==3:
                    B[i][j]=1
                else:
                    B[i][j]=0
            else:
                if neigh==2 or neigh==3:
                    B[i][j]=1
                else:
                    B[i][j]=0


def gen2Dgraphic(N):
    a=[]
    for i in range(N):
        b=[]
        for j in range(N):
            b=b+[Circle(Point(i,j),.49)]
        a=a+[b]
    return a

def push(B,A):
    N=len(A)
    for i in range(N):
        for j in range(N):
            A[i][j]=B[i][j]
            
def drawArray(A,a,window):
#A is the array of 0,1 values representing the state of the game
#a is an array of Circle objects
#window is the GraphWin in which we will draw the circles
    N=len(A)
    for i in range(N):
        for j in range(N):
            if A[i][j]==1:
                a[i][j].undraw()
                a[i][j].draw(window)
            if A[i][j]==0:
                a[i][j].undraw()

def slider(a,x,y):
    a[0+x][0+y]=1
    a[0+x][1+y]=1
    a[2+x][1+y]=1
    a[0+x][2+y]=1
    a[1+x][2+y]=1

N=50
win = GraphWin("Title",600,600)
win.setCoords(-1,-1,N+1,N+1)
grid=empty(N)
grid2=empty(N)
circles=gen2Dgraphic(N)
#fill(grid,0.1)
for i in range(10):
    slider(grid,5*i,5*i)


    

#for i in range(100):
while True:
    drawArray(grid,circles,win)
    update(grid,grid2)
    push(grid2,grid)





#def 2Dgraphic(A):
#    N=len(A)
#    a=[]
#    for i in range(N):
#        b=[]
#        for j in range(N):
#            b=b+[Circle(Point(i,j),.49)]
#        a=a+[b]
    
#def graph2Darray(A,window):
#    N=len(A)
#    for i in range(N):
#        for j in range(N):
#            A[i][j].draw(window)
