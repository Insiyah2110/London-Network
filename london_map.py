from final_project_part1 import *
import csv
import math

def london_map():

    g = DirectedWeightedGraph();

    with open('london_stations.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        first_row = next(reader, None)
        stationData = list(reader)

    with open('london_connections.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        first_row = next(reader, None)
        connectionData = list(reader)

    for row in stationData:
        g.add_node(int(row[0]))

    for row in connectionData:
        for row2 in stationData:
            if row2[0] == row[0]:
                lat1 = float(row2[1])
                long1 = float(row2[2])
                p = (lat1, long1)
            if row2[0] == row[1]:
                lat2 = float(row2[1])
                long2 = float(row2[2])
                q = (lat2, long2)
        w = math.dist(p,q)
        g.add_edge(int(row[0]),int(row[1]),w)
        g.add_edge(int(row[1]),int(row[0]),w)

    return g

graph = london_map()
#print(graph.adj)

pairs = [(i, j) for i in graph.adj.keys() for j in graph.adj.keys()]
print(len(pairs))











