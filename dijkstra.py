

def dijkstra(graph : dict, src_airport, dest_airport):
    dist = {}
    path = {}
    explored = []
    unexplored = {}

    for vertex in graph.keys():
        dist[vertex] = float('inf')  # setting all source_airport dist to infinity
        path[vertex] = []  # path list is empty yet

    for dictionary in graph.values():
        for vertex in dictionary.keys():
            if vertex not in dist.keys():
                dist[vertex] = float('inf')  # setting all destination_airport dist to infinity
                path[vertex] = []

    dist[src_airport] = 0
    explored.append(src_airport)
    for source in graph.keys():  # setting values for children of src_airport
        if source == src_airport:
            temp_dictionary = source[src_airport]
            for destination in temp_dictionary.keys():
                dist[destination] = temp_dictionary[destination]
                unexplored[destination] = temp_dictionary[destination]
    source = src_airport

    while dest_airport not in explored:
        sorted_values = sorted(unexplored)
        min_unexplored = sorted_values[0]
        min_unexplored_distance = unexplored[min_unexplored]




