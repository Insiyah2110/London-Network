import time
import min_heap
import random
from part1 import *
from a_star import *
from london_map import *
from london_h import *
import matplotlib.pyplot as plt


def dijkstra(G, source, dest):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node


    return (dist[dest])
    
graph = london_map()

pairs = [(i, j) for i in graph.adj.keys() for j in graph.adj.keys()]


# EXPERIMENT 1: Runtime for all pairs using Dijkstra's and A* Algorithm 

times_dijkstra = []
times_a_star = []
count = 0

for pair in range(len(pairs)):

    start_time_d = time.time()
    distance_d = dijkstra(graph, pairs[pair][0], pairs[pair][1])
    end_time_d = time.time()
    running_time_d = end_time_d - start_time_d
    times_dijkstra.append(running_time_d)
    
    start_time_a = time.time()
    result_a_star = a_star(graph, pairs[pair][0], pairs[pair][1], london_h(pairs[pair][1]))
    distance_a = result_a_star[1]
    end_time_a = time.time()
    running_time_a = end_time_a - start_time_a
    times_a_star.append(running_time_a)
    
    if (running_time_d > running_time_a):
        count += 1
    
    print(f" Pair {pair+1}: From station = {pairs[pair][0]}, To station = {pairs[pair][1]}, Dijkstra running time = {running_time_d}, A* running time = {running_time_a}")

print (f"A* algorithm outperforms Dijkstra {count} times")
print (f"Dijkstra algorithm outperforms A* {len(pairs) - count} times")

plt.plot (times_dijkstra , label = 'Dijkstra running time')
plt.plot (times_a_star , label = 'A* running time')
plt.xlabel('Pairs')
plt.ylabel('Running Time (s)')
plt.title('Dijkstra vs A* Running Time')
plt.legend()
plt.show()


