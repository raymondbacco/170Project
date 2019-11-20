import random
import numpy as np
import matplotlib.pyplot as plt
import math 

def calculateDistance(x1,y1,x2,y2):  
    dist = round((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)),5)  
    return dist

try:
    num_points = int(sys.argv[1])
except:
    num_points = 50

#create requested number of points
point_arr = []
for k in range(num_points):
    p = [random.randint(0,128),random.randint(0,128)]
    while p in point_arr:
        p = [random.randint(0,128),random.randint(0,128)]
    point_arr.append(p)
    
#print a cartisian plot
for a in point_arr:
    plt.scatter(a[0], a[1])
plt.show()

#create empty matrix nxn
n = len(point_arr)
matrix = [[0 for i in range(n)] for j in range(n)]
#print (np.array(matrix))

# create the complete adjaceny matrix with the weights as strings and no point connected to itself  
posx = 0
for pi in point_arr:
    posy = 0
    for q in point_arr:   
        matrix[posx][posy]=(calculateDistance(pi[0],pi[1],q[0],q[1]))
        posy+=1
    posx+=1
# No vertex connects to itself
for i in range(len(point_arr)):
    matrix[i][i] = "x"
#print(np.array(matrix))

filename = str(num_points)+"CompleteAdj.in"

f= open(filename,"w+")

#adjacency matrix
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        f.write((str(matrix[y][x])+" "))
    f.write("\n")
f.close() 
