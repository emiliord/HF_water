import os
import numpy

file=os.path.join('./', 'water.inp') #generalize later
#geom_matrix=numpy.genfromtxt(fname=file, dtype=('U2',float,float,float))

outfile = open(file,"r")
data = outfile.readlines()

for line in data:
    if 'geom={' in line:
        sp = line
        print(sp)

outfile.close()
