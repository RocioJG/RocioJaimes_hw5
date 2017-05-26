#Punto 2 tarea 5 Rocio Jaimes
#Para este ejercicio tomo como referencia el repositorio del curso
#https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import griddata

#cargar los datos
data= np.loadtxt("CircuitoRC.txt")
t= data[:,0]
Q= data[:,1]

#funcion para encontrar verosimilitud
def likelihood(Q, Q_model):
    chi_cuadrado= (1.0/2.0)*sum((Q-Q_model)**2)
    return np.exp(-chi_cuadrado)

#modelo para encontrar Q maximo
def Qmax (t, Q, R, C ):
    return Q*(1-np.exp(-t/R*C))

#creo listas vacias para simular MC
R_vacio= np.empty((0))
C_vacio= np.empty((0))
v_vacio= np.empty((0))

#Adiciono a mis listas inicialmente vacias valores aleatorios
R_vacio= np.append(R_vacio, np.random.random())
C_vacio= np.append(C_vacio, np.random.random())
#Evaluo Q maximo inicial con las listas aleatorias
Q_inic= Qmax(t, Q, R_vacio[0], C_vacio[0])
#anhado a mi listas de verosimilitud el calculo con base en listas random
v_vacio= np.append(v_vacio, likelihood(Q, Q_inic))
#imprimo variables
print R_vacio
print C_vacio
print v_vacio

n_it= 20000 #numero de iteraciones que deseo hacer
for i in range(n_it):
    #doy loc y scale para valores para evaluaren mi funcion Qmax
    R_prime= np.random.normal(R_vacio[i], 0.1)
    C_prime= np.random.normal(C_vacio[i], 0.1)
    #valor inicial maximo
    Q_inic= Qmax(t, Q, R_vacio[i], C_vacio[i])
    #siguiente valor Q maximo
    Q_prime= Qmax(t, Q_inic, R_prime, C_prime)
    #verosimilitud
    v_prime= likelihood(Q, Q_prime)
    v_inic= likelihood(Q, Q_inic)
    
    alpha= v_prime/v_inic
    if(alpha>=1.0):
        #Si hay mayor verosimiltud con los nuevos datos anhado el nuevo resultado
        R_vacio= np.append(R_vacio, R_prime)
        C_vacio= np.append(C_vacio, C_prime)
        v_vacio= np.append(v_vacio, v_prime)
        
    else:
        #de lo contrario genero un nuevo numero random desde el cual evaluare el nuevo optimo
        betha= np.random.random()
        if (betha<=alpha):
            #Si este nuevo numero random es peor la relacion de verosimilitud, conservo valores obtenidos antes
            R_vacio= np.append(R_vacio, R_prime)
            C_vacio= np.append(C_vacio, C_prime)
            v_vacio= np.append(v_vacio, v_prime)
        else: 
            #si este nuevo numero random da mejores resultado conservo este valor
            R_vacio= np.append(R_vacio, R_vacio[i])
            C_vacio= np.append(C_vacio, C_vacio[i])
            v_vacio= np.append(v_vacio, v_vacio[i])

plt.figure()
plt.scatter(R_vacio, C_vacio)
plt.title("Dispersion R y C")
plt.xlabel("R")
plt.ylabel("C")
#plt.show
plt.savefig("DispersionRC.pdf")

#Creo histogramas
plt.figure()
count, bins, ignored =plt.hist(R_vacio, 20, normed=True)
plt.title("Histograma R")
plt.xlabel("frequencia")
plt.ylabel("R")
#plt.show()
plt.savefig("HistogramaR.pdf")

plt.figure()
count, bins, ignored =plt.hist(C_vacio, 20, normed=True)
plt.title("Histograma C")
plt.xlabel("frequencia")
plt.ylabel("C")
#plt.show()
plt.savefig("HistogramaC.pdf")
#Encuntro la maxima verosimilitud
maxV = np.argmax(v_vacio)
#con ese valor encintro mejor R y C
mejorR = R_vacio[maxV]
mejorC = C_vacio[maxV]

#hayo Qmax
Q_maximo= Qmax(t, Q, mejorR, mejorC)
#grafico Q dado en datos y Qmax
plt.figure()
plt.scatter(t, Q)
plt.plot(t, Q_maximo, 'r')
plt.title("Q maximo en el tiempo con Monte Carlo")
plt.xlabel("tiempo")
plt.ylabel("Q maximo")
plt.savefig("Q_max.pdf")
#plt.show()
