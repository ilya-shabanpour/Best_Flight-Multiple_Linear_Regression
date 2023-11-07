def a_star(graph: dict, src_airport, dest_airport):
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
        dist[destination] = edges[destination][0]
        unexplored[destination] = edges[destination][0] + edges[destination][1]
        prev[destination] = src_airport

    while 1:
        # v = least-valued unexplored vertex
        v_distance = min(unexplored.values())
        v = list(unexplored.keys())[list(unexplored.values()).index(v_distance)]
        if v not in graph.keys():
            unexplored.pop(v)
            continue

        explored.append(v)
        if dest_airport in explored:
            break
        unexplored.pop(v)

        edges = graph[v]
        for w in edges.keys():
            if w not in explored:
                if dist[v] + edges[w][0] < dist[w]:
                    dist[w] = dist[v] + edges[w][0]
                    unexplored[w] = dist[w] + edges[w][1]
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

