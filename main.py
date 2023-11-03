import pandas as pd
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
    return round(((f.Price / 1000) * 3 + f.FlyTime), 3)


def output_files(djk: list, a_star: list, djk_time):
    output_file_djk = open("[8]-UIAI4021-PR1-Q1_djk.txt", "w+")
    output_file_a_star = open("[8]-UIAI4021-PR1-Q1_AStar.txt", "w+")

    output_file_djk.write("Dijkstra Algorithm\n")
    output_file_djk.write("Execution Time: " + str(djk_time))
    output_file_djk.write("\n")
    output_file_djk.write(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

    c = 0
    for i in range(len(djk) - 1):
        output_file_djk.write("Flight #" + str(i) + "\nFrom:")

    output_file_djk.close()
    output_file_a_star.close()


# -----------------------------------------------------------------------------------------------------------------------

def dijkstra_graph():
    graph_djk = {}
    for flight in Flight_List.flights_list:
        if flight.SourceAirport not in graph_djk.keys():
            graph_djk[flight.SourceAirport] = {flight.DestinationAirport: cost_func(flight)}
        else:
            graph_djk[flight.SourceAirport][flight.DestinationAirport] = cost_func(flight)

    return graph_djk


# -----------------------------------------------------------------------------------------------------------------------

def a_star_graph():
    graph_astar = {}
    for flight in Flight_List.flights_list:
        if flight.SourceAirport not in graph_astar.keys():
            graph_astar[flight.SourceAirport] = {flight.DestinationAirport: [cost_func(flight),
                                                                             distance(flight.SourceAirport_Latitude,
                                                                                      h_latitude,
                                                                                      flight.SourceAirport_Longitude,
                                                                                      h_longitude)]}
        else:
            graph_astar[flight.SourceAirport][flight.DestinationAirport] = [cost_func(flight),
                                                                            distance(flight.SourceAirport_Latitude,
                                                                                     h_latitude,
                                                                                     flight.SourceAirport_Longitude,
                                                                                     h_longitude)]
            return graph_astar


# -----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # df = pd.read_csv("Flight_Data.csv")
    # data2 = df.drop(columns='Airline')
    # df2 = data2.drop_duplicates(keep='first')
    # extracted_col = df["Airline"]
    # df2.insert(0, 'Airline', extracted_col)

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

    start = time.time()
    dijkstra_shortest_path = dijkstra.dijkstra(graph_djk, src_airport, dest_airport)
    end = time.time()
    djk_exe_time = end - start
    print(djk_exe_time)
    # output_files(start,end)
    print(dijkstra_shortest_path)
