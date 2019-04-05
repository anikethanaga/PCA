import numpy


z = numpy.array([[1,4,3],[10,6,3],[1,0,9]])

ev = [5,4,2]
p = numpy.array([[1,2,3],[9,7,4],[8,5,6]])
pstar = p
for i in range(len(ev)-1):
    for j in range(i+1,len(ev)):
        if ev[i]>ev[j]:
            temp = ev[i]
            ev[i] = ev[j]
            ev[j] = temp
            pstar[[i,j]] = pstar[[j,i]]
zstar = numpy.dot(z,pstar)
print(zstar)