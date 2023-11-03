def dijkstra(graph: dict, src_airport, dest_airport):
    dist = {}
    prev = {}
    explored = []
    unexplored = {}

    for vertex in graph.keys():
        dist[vertex] = float('inf')  # setting all source_airport dist to infinity

    for dictionary in graph.values():
        for vertex in dictionary.keys():
            if vertex not in dist.keys():
                dist[vertex] = float('inf')  # setting all destination_airport dist to infinity

    dist[src_airport] = 0
    explored.append(src_airport)

    # setting values for children of src_airport
    edges = graph[src_airport]
    for destination in edges.keys():
        dist[destination] = edges[destination]
        unexplored[destination] = edges[destination]
        prev[destination] = src_airport

    while 1:
        # v = least-valued unexplored vertex
        v_distance = min(unexplored.values())
        v = list(unexplored.keys())[list(unexplored.values()).index(v_distance)]
        explored.append(v)
        if dest_airport in explored:
            break
        unexplored.pop(v)

        edges = graph[v]
        for w in edges.keys():
            if w not in explored:
                if dist[v] + edges[w] < dist[w]:
                    dist[w] = dist[v] + edges[w]
                    unexplored[w] = dist[w]
                    prev[w] = v

    path = []
    destination = dest_airport
    path.append(destination)
    while 1:
        path.append(prev[destination])
        destination = prev[destination]
        if src_airport in path:
            break
    path.reverse()
    return path

