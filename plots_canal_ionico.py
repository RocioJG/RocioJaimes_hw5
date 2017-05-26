import matplotlib.pyplot as plt
import numpy as np

data=np.genfromtxt("Resultados_hw5.tex")
inicial= np.loadtxt("canal_ionico.txt")
iteraciones=20000
i_1=iteraciones-1
x=data[:,0]
y=data[:,1]
r=data[:,2]
x1=data[:,3]
y1=data[:,4]
r1=data[:,5]

xi=inicial[:,0]
yi=inicial[:,1]
mayorr=0
'''
for i in range(iteraciones):
	if (r[i]>mayorr):
		mayorr==r[i] 
'''

plt.figure()
plt.hist(x,  normed=True)
plt.title("Histograma normalizado X archivo 0")
plt.xlabel("valores en x")
plt.ylabel("frecuencias")
plt.savefig("Hist_x.pdf")

plt.figure()
plt.hist(y, normed=True)
plt.title("Histograma normalizado y archivo 0")
plt.xlabel("valores en y")
plt.ylabel("frecuencias")
plt.savefig("Hist_y.pdf")
#plt.show()

plt.figure()
plt.hist(r, normed=True)
plt.title("Histograma normalizado X archivo 0")
plt.xlabel("valores en r")
plt.ylabel("frecuencias")
plt.savefig("Hist_r.pdf")
#plt.show()

plt.figure()
plt.hist(x1, normed=True)
plt.title("Histograma normalizado X archivo 1")
plt.xlabel("valores en x1")
plt.ylabel("frecuencias")
plt.savefig("Hist_x1.pdf")
#plt.show()

plt.figure()
plt.hist(y1, normed=True)
plt.title("Histograma normalizado y archivo 1")
plt.xlabel("valores en y")
plt.ylabel("frecuencias")
plt.savefig("Hist_y1.pdf")
#plt.show()

plt.figure()
plt.hist(r1, normed=True)
plt.title("Histograma normalizado X archivo 1")
plt.xlabel("valores en x")
plt.ylabel("frecuencias")
plt.savefig("Hist_r1.pdf")
#plt.show()

fig= plt.figure()
circ=plt.Circle((x[i_1], y[i_1]), r[i_1])
plt.scatter(xi,yi)
ax=fig.add_subplot(1,1,1)
ax.add_patch(circ)
plt.savefig("optimo.pdf")
#plt.show()

fig1= plt.figure()
circ1=plt.Circle((x1[i_1], y1[i_1]), r1[i_1])
plt.scatter(xi,yi)
ax1=fig1.add_subplot(1,1,1)
ax1.add_patch(circ1)
plt.savefig("optimo1.pdf")
#plt.show()
