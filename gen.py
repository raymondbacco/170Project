import numpy as np
import random
import names
import sys
import matplotlib.pyplot as plt
import math 

def calculateDistance(x1,y1,x2,y2):  
    dist = round((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)),5)  
    return dist

def random_adjacency_matrix(n):   
    matrix = [[random.randint(0, 1) for i in range(n)] for j in range(n)]

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0
    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]
    return matrix

# get graph size and max number of homes or set to a default of 50,25
try:
    n = int(sys.argv[1])
except:
	n = 50
try:
	home_max = int(sys.argv[2])
except:
	home_max = 25
num_homes = random.randint(1, home_max+1)


def completeMatrix(n):
	#create requested number of points
	point_arr = []
	for k in range(n):
		p = [random.randint(0,128),random.randint(0,128)]
		while p in point_arr:
			p = [random.randint(0,128),random.randint(0,128)]
		point_arr.append(p)

	#create empty matrix nxn
	n = len(point_arr)
	matrix = [[0 for i in range(n)] for j in range(n)]

	# create the complete adjaceny matrix with the weights as strings and no point connected to itself  
	posx = 0
	for pi in point_arr:
		posy = 0
		for q in point_arr:   
			matrix[posx][posy]=(calculateDistance(pi[0],pi[1],q[0],q[1]))
			posy+=1
		posx+=1
	# Verify No vertex connects to itself
	for i in range(len(point_arr)):
		matrix[i][i] = "x"
	return matrix



# names all the locations with a unique first name
name_arr=[]
for i in range(n):
	name = names.get_first_name()
	while name in name_arr or len(name)>20:
		name = names.get_first_name()
	name_arr.append(name)
name_string = ""
for q in name_arr:
	name_string += (q+" ")

#select the choosen number of homes from the locations
home_arr=[]
for k in range(num_homes):
	h = name_arr[random.randint(0,len(name_arr)-1)]
	while h in home_arr:
		h = name_arr[random.randint(0,len(name_arr)-1)]
	home_arr.append(h)
home_string = ""
for w in home_arr:
	home_string+=(w+" ") 

#generate random adjacency matrix
g = random_adjacency_matrix(n)
#g = completeMatrix(n)


# set all zeros to x
for y in range(len(g)):
	for x in range(len(g[y])):
		if (g[y][x]==0):
			g[y][x]="x"

filename = str(n)+".in"

f= open(filename,"w+")
#num locations
f.write(str(n)+"\n")
#num homes
f.write(str(num_homes)+"\n")
#names of all locations
f.write(name_string+"\n")
#names of homes
f.write(home_string+"\n")
#name of starting location
f.write(name_arr[0]+"\n")
#adjacency matrix
for y in range(len(g)):
	for x in range(len(g[y])):
		f.write((str(g[y][x])+" "))
	f.write("\n")	

f.close() 
