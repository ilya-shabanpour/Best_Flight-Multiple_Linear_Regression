import pandas as pd

import A_Star
import Flight_List
import dijkstra
from math import radians, cos, sin, asin, sqrt
import time


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return c * r


# -----------------------------------------------------------------------------------------------------------------------

def cost_func(f: Flight_List.FLight):  # cost funtion is a linear combination of price and fly time of the flight.
    return round(f.Distance, 3)


def output_files(djk: list, a_star: list, djk_time, a_star_time):
    output_file_djk = open("[8]-UIAI4021-PR1-Q1_djk.txt", "w+")
    output_file_a_star = open("[8]-UIAI4021-PR1-Q1_AStar.txt", "w+")

    output_file_djk.write("Dijkstra Algorithm\n")
    output_file_djk.write("Execution Time: " + str(round(djk_time * 1000, 2)) + "ms")
    output_file_djk.write("\n")
    output_file_djk.write(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

    if djk is None:
        output_file_djk.write("There is no path from source airport to destination airport")
    else:
        c = 0
        total_price = 0
        total_time = 0
        total_distance = 0
        for i in range(len(djk) - 1):
            output_file_djk.write("Flight #" + str(i + 1) + "\nFrom: ")
            for f in Flight_List.flights_list:
                if f.SourceAirport == djk[c] and f.DestinationAirport == djk[c + 1]:
                    output_file_djk.write(f.SourceAirport_City + "-" + f.SourceAirport + ". "
                                          + f.SourceAirport_Country + "\n")
                    output_file_djk.write("To: " + f.DestinationAirport_City + "-" + f.DestinationAirport + ". "
                                          + f.DestinationAirport_Country + "\n")
                    output_file_djk.write("Distance: " + str(round(f.Distance)) + "km\n" + "Time: " + str(round(f.FlyTime))
                                          + "h\n" + "Price: " + str(round(f.Price)) + "$\n")
                    output_file_djk.write("----------------------------\n")
                    total_price += round(f.Price)
                    total_time += round(f.FlyTime)
                    total_distance += round(f.Distance)
                    break
            c += 1
        output_file_djk.write("Total Price: " + str(total_price) + "$\n" + "Total Distance: " + str(total_distance)
                              + "km\n" + "Total Time: " + str(total_time) + "h")
    output_file_djk.close()


    output_file_a_star.write("A* Algorithm\n")
    output_file_a_star.write("Execution Time: " + str(round(a_star_time * 1000, 2)) + "ms")
    output_file_a_star.write("\n")
    output_file_a_star.write(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

    if a_star is None:
        output_file_a_star.write("There is no path from source airport to destination airport")
    else:
        c = 0
        total_price = 0
        total_time = 0
        total_distance = 0
        for i in range(len(a_star) - 1):
            output_file_a_star.write("Flight #" + str(i + 1) + "\nFrom: ")
            for f in Flight_List.flights_list:
                if f.SourceAirport == a_star[c] and f.DestinationAirport == a_star[c + 1]:
                    output_file_a_star.write(f.SourceAirport_City + "-" + f.SourceAirport + ". "
                                          + f.SourceAirport_Country + "\n")
                    output_file_a_star.write("To: " + f.DestinationAirport_City + "-" + f.DestinationAirport + ". "
                                          + f.DestinationAirport_Country + "\n")
                    output_file_a_star.write("Distance: " + str(round(f.Distance)) + "km\n" + "Time: " + str(round(f.FlyTime))
                                          + "h\n" + "Price: " + str(round(f.Price)) + "$\n")
                    output_file_a_star.write("----------------------------\n")
                    total_price += round(f.Price)
                    total_time += round(f.FlyTime)
                    total_distance += round(f.Distance)
                    break
            c += 1
        output_file_a_star.write("Total Price: " + str(total_price) + "$\n" + "Total Distance: " + str(total_distance)
                              + "km\n" + "Total Time: " + str(total_time) + "h")
    output_file_a_star.close()


# -----------------------------------------------------------------------------------------------------------------------

def dijkstra_graph():
    graph = {}
    for fl in Flight_List.flights_list:
        if fl.SourceAirport not in graph.keys():
            graph[fl.SourceAirport] = {fl.DestinationAirport: cost_func(fl)}
        else:
            graph[fl.SourceAirport][fl.DestinationAirport] = cost_func(fl)

    return graph


# -----------------------------------------------------------------------------------------------------------------------

def a_star_graph():
    graph_astar = {}
    for fli in Flight_List.flights_list:
        if fli.SourceAirport not in graph_astar.keys():
            graph_astar[fli.SourceAirport] = {fli.DestinationAirport: [cost_func(fli),
                                                                       distance(fli.SourceAirport_Latitude,
                                                                                h_latitude,
                                                                                fli.SourceAirport_Longitude,
                                                                                h_longitude)]}
        else:
            graph_astar[fli.SourceAirport][fli.DestinationAirport] = [cost_func(fli),
                                                                      distance(fli.SourceAirport_Latitude,
                                                                               h_latitude,
                                                                               fli.SourceAirport_Longitude,
                                                                               h_longitude)]
    return graph_astar


# -----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    user_input = input("Please enter source and destination airport:")
    input_split = user_input.split(" - ")
    src_airport = input_split[0]  # putting input airports in variables
    dest_airport = input_split[1]

    h_altitude = 0
    h_longitude = 0
    h_latitude = 0
    for flight in Flight_List.flights_list:
        if flight.DestinationAirport == dest_airport:
            h_altitude = flight.DestinationAirport_Altitude
            h_longitude = flight.DestinationAirport_Longitude
            h_latitude = flight.DestinationAirport_Latitude
            break

    graph_djk = dijkstra_graph()
    graph_a_star = a_star_graph()

    start1 = time.time()
    dijkstra_shortest_path = dijkstra.dijkstra(graph_djk, src_airport, dest_airport)
    end1 = time.time()
    djk_exe_time = end1 - start1
    print(djk_exe_time)
    print(dijkstra_shortest_path)

    start2 = time.time()
    a_star_shortest_path = A_Star.a_star(graph_a_star, src_airport, dest_airport)
    end2 = time.time()
    a_star_exe_time = end2 - start2
    print(a_star_shortest_path)
    print(a_star_exe_time)
    output_files(dijkstra_shortest_path, a_star_shortest_path, djk_exe_time, a_star_exe_time)
    # print(dijkstra_shortest_path)
