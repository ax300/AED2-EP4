import json
import sys
import matplotlib.pyplot as plt
import queue
import operator
from datetime import datetime



sys.setrecursionlimit(10000) # Aumenta o limite padrão de recursões, se não dá erro. 
population = {}
visited = []
component_size = []
max_diametro = 0
No_max_diametro = 0 # No que deu origem ao maior diametro encontrado


def bfs(x):
    # print("entra")
    # guarda as distancias de cada Node  
    level = {}
    
    # cria fila de adjacentes
    que = queue.Queue()
  
    # enfileira elemento x  
    que.put(x)  
  
    # inicializa as distancias
    # dos nos pra zero  
    level[x] = 0
    diametro = 0
  
    # marca como visitado
    population[x][0] = True
  
    # enquanto a fila nao for vazia 
    while not que.empty(): 
  
        # pega o primeiro elemento da fila
        x = que.get()  
        # caminha pelos adjacentes do No x
        for b in population[x][1]:

            # se 'b' nao foi visitado 
            if not population[b][0]:
                que.put(b)
                # distancia de b eh level de x+1
                if level[x] + 1 > diametro:
                    # print(diametro)
                    diametro = level[x] + 1

                level[b] = level[x] + 1
                population[b][0] = True
    

    return diametro, level


def reset_flg():
    for k, v in population.items():
        v[0] = False

def add_person(v_ori, v_dest): # Cria lista de adjacencia 
    global population

    if v_ori in population: # Se o no ja existe
        if v_dest not in population[v_ori][1]:
            population[v_ori][1].append(v_dest)
    else: # Se o no eh novo
        population[v_ori] = [False,[v_dest]] # O false indica que o vértice ainda não foi visitado
    
def plot(level):
    quantidade_level = {}
    x_array = []
    y_array = []

    for k, v in level.items(): 
        if v not in quantidade_level:      
            quantidade_level[v] = 1
        else:
            quantidade_level[v] += 1


    for k, v in quantidade_level.items():
        x_array.append(k)
        y_array.append(v)

    plt.bar(x_array, y_array)
    plt.xlabel('Nível')
    plt.ylabel('Quantidade')
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":

    start = datetime.now()
    with open('cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)
            add_person(v_dest, v_ori) # Adiciona a volta também para fazer um grafo não direcionado

    with open('componenteG_cenario3.txt') as f:
        for l in f.readlines():
            # print (l.replace('\n', ''))
            di = bfs(l.replace('\n', ''))[0]
            # print(str(di))
            if di > max_diametro:
                No_max_diametro = l.replace('\n', '')
                max_diametro = di
            reset_flg()

    end = datetime.now()
    diff = end - start
    print(diff)
    plot(bfs(No_max_diametro)[1])

    # print(max_diametro)