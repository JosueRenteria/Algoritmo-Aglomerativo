#Título Programa: PRACTICA 5: Algoritmo Aglomerativo
#Fecha: 8-diciembre-2022
#Autor: Renteria Arriaga Josue

# Declaracion de Librerias.
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from math import sqrt

# Declaramos nuestras muestras y conjuntos (para cada centroide).
muestras = np.random.rand(9,2)
centroides = muestras 
conjuntos = [[i] for i in range(9)]

# Funcion para las distancias entre puntos.
def distancia_ecu(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

# Generamos la Matriz de todas las Distancias.
matriz_distancia = np.full((9, 9), fill_value=10000, dtype = np.double)
for i in range(9): # calculo inicial de las distancias entre clusters
    for j in range(i):
        matriz_distancia[i][j] = distancia_ecu(muestras[i][0], muestras[i][1], muestras[j][0], muestras[j][1])

# Funcion para sacar los centroides.
def centroide(puntos):
    xs = np.fromiter(map(lambda p: muestras[p][0], puntos), dtype=np.double)
    ys = np.fromiter(map(lambda p: muestras[p][1], puntos), dtype=np.double)
    return [np.mean(xs), np.mean(ys)]

# Funcion que genera un nuevo conjunto.
def nuevo_conjunto(c1, c2):
    conjuntos.append(conjuntos[c1]+conjuntos[c2])
    print(f'Nuevo conjunto: {conjuntos[-1]}')
    del conjuntos[c1]
    del conjuntos[c2]
    print('Conjuntos actuales: ')
    print(conjuntos)

# Funcion que saca la distancia entre centroides.
def distancia_centroide(nC):
    return [distancia_ecu(nC[0], nC[1], p[0], p[1]) for p in centroides]

# Arreglo con los colores de los conjuntos.
color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'pink','gold']

# Funcion que grafica los conjuntos.
def graficar(graficar):
    i = 0
    for c in graficar:
        plt.scatter(muestras[[c],0], muestras[[c],1], c=color[i], label=str(i))
        i+=1

# Mostramos los primeros Datos.
print(muestras)
graficar(conjuntos)
plt.legend()
plt.show()
print("\nMatriz de Distancias:")
print(matriz_distancia)
print("\n")

# Ciclo que genera los conjuntos.
while 1:
    min_ = np.amin(matriz_distancia) # distancia más cercana entre conjuntos.
    f, c = np.where(matriz_distancia==np.amin(matriz_distancia)) # conjuntos.
    print(f'Distancia minima: {min_}: {f},{c}')

    # Eliminamos los centroides
    centroides = np.delete(centroides, f, 0)
    centroides = np.delete(centroides, c, 0)
    nuevo_conjunto(int(f), int(c)) # concatena los puntos para generar nuevo.
    nC = centroide(conjuntos[-1])
    print(f'Nuevo centroide: {nC}')

    if(matriz_distancia.shape != (2,2)):
        if (f > c):
            mayor = f
            menor = c
        else:
            mayor = c
            menor = f
    
        matriz_distancia = np.delete(matriz_distancia, mayor, axis=0)
        matriz_distancia = np.delete(matriz_distancia, menor, axis=0)
        matriz_distancia = np.delete(matriz_distancia, mayor, axis=1)
        matriz_distancia = np.delete(matriz_distancia, menor, axis=1)
    else:
        break

    nuevoC = np.array([distancia_centroide(nC)])
    print(f'Nueva fila: {nuevoC}')
    matriz_distancia = np.append(matriz_distancia, nuevoC, axis=0)
    
    # Mostramos los nuevos Datos.
    nuevaZero = np.full((matriz_distancia.shape[0],1), fill_value=10000,dtype = np.double)
    matriz_distancia = np.append(matriz_distancia,nuevaZero, axis=1)
    centroides = np.append(centroides, np.array([nC]), axis = 0)
    graficar(conjuntos)
    plt.legend()
    plt.show()
    print("\nMatriz de Distancias:")
    print(matriz_distancia)
    print("\n")

# Grafica Final.
graficar(conjuntos)
plt.legend()
plt.show()
