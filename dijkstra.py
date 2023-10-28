

def dijkstra(graph, src_airport, dest_airport):
    dist = {}
    path = {}
    explored = []

    for vertex in graph.keys():
        dist[vertex] = float('inf')  # setting all vertices dist to infinity
        path[vertex] = []  # path list is empty yet

    dist[src_airport] = 0
    for source in graph.keys():
        if source == src_airport:
            sourceDict = source.get()
            for destination in sourceDict.keys():
                dist[destination] = sourceDict[destination]
    source = src_airport

    while dest_airport not in explored:
        pass



