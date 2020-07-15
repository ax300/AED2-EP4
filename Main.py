import json
import sys
import matplotlib.pyplot as plt
import queue


sys.setrecursionlimit(10000) # Aumenta o limite padrão de recursões, se não dá erro. 
population = {}
visited = []
component_size = []


def bfs(V, x):
      
    # array to store level of each node  
    level = [None] 
    marked = [False]
    # create a queue  
    que = queue.Queue() 
  
    # enqueue element x  
    que.put(x)  
  
    # initialize level of source  
    # node to 0  
    level[x] = 0
  
    # marked it as visited  
    marked[x] = True
  
    # do until queue is empty  
    while (not que.empty()): 
  
        # get the first element of queue  
        x = que.get()  
  
        # traverse neighbors of node x 
        for i in range(len(population.items())): 
              
            # b is neighbor of node x  
            b = population[x][1][i]  
  
            # if b is not marked already  
            if (not marked[b]):  
                que.put(b)  
                # level of b is level of x + 1  
                level[b] = level[x] + 1
                marked[b] = True
                
    # display all nodes and their levels  
    print("Nodes", " ", "Level") 
    for i in range(V): 
        print(" ",i,  " --> ", level[i]) 


def add_person(v_ori, v_dest): # Cria o lista de adjacencia 
    global population

    if v_ori in population: # Se o no ja existe
        if v_dest not in population[v_ori][1]:
            population[v_ori][1].append(v_dest)
    else: # Se o no eh novo
        population[v_ori] = [False, [v_dest]] # O false indica que o vértice ainda não foi visitado
    
def plot():
    x_array = []
    y_array = []
    size_components = {}

    for x in component_size: 
        if x not in size_components:      
            size_components[x] = 1
        else:
            size_components[x] += 1

    for k, v in size_components.items():
        x_array.append(k)
        y_array.append(v)

    plt.bar(x_array, y_array)
    plt.xlabel('Tamanho da componente')
    plt.ylabel('Nº de componentes')
    plt.xticks(rotation='vertical')
    plt.show()


if __name__ == "__main__":
    
    with open('componeteG_cenario3.txt') as f:

        v = f.readline().replace('\n', '')
        e = f.readline().replace('\n', '')

        for l in f.readlines():
            v_ori, v_dest = l.replace('\n', '').split(' ')
            add_person(v_ori, v_dest)
            add_person(v_dest, v_ori) # Adiciona a volta também para fazer um grafo não direcionado
    # print(population)
    # print(component_size)
    values_view = population.values()
    value_iterator = iter(values_view)
    first_value = next(value_iterator)
    bfs(v,first_value)
    plot()