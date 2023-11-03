from math import radians, cos, sin, asin, sqrt
import pandas as pd
import main

df = pd.read_csv("Flight_Data.csv")
data2 = df.drop(columns='Airline')
df2 = data2.drop_duplicates(keep='first')
extracted_col = df["Airline"]
df2.insert(0, 'Airline', extracted_col)
df = df2


class FLight:  # making a class for flights' detail
    def __init__(self):
        self.Airline = None
        self.SourceAirport = None
        self.DestinationAirport = None
        self.SourceAirport_City = None
        self.SourceAirport_Country = None
        self.SourceAirport_Latitude = None
        self.SourceAirport_Longitude = None
        self.SourceAirport_Altitude = None
        self.DestinationAirport_City = None
        self.DestinationAirport_Country = None
        self.DestinationAirport_Latitude = None
        self.DestinationAirport_Longitude = None
        self.DestinationAirport_Altitude = None
        self.Distance = None
        self.FlyTime = None
        self.Price = None


flights_list = []  # a list of all flights
for index, row in df.iterrows():  # allocating all "needed" attributes
    flight = FLight()
    flight.Airline = row["Airline"]
    flight.SourceAirport = row["SourceAirport"]
    flight.DestinationAirport = row["DestinationAirport"]
    flight.SourceAirport_City = row["SourceAirport_City"]
    flight.SourceAirport_Country = row["SourceAirport_Country"]
    flight.SourceAirport_Latitude = row["SourceAirport_Latitude"]
    flight.SourceAirport_Longitude = row["SourceAirport_Longitude"]
    flight.SourceAirport_Altitude = row["SourceAirport_Altitude"]
    flight.DestinationAirport_City = row["DestinationAirport_City"]
    flight.DestinationAirport_Country = row["DestinationAirport_Country"]
    flight.DestinationAirport_Latitude = row["DestinationAirport_Latitude"]
    flight.DestinationAirport_Longitude = row["DestinationAirport_Longitude"]
    flight.DestinationAirport_Altitude = row["DestinationAirport_Altitude"]
    flight.Distance = row["Distance"]
    flight.FlyTime = row["FlyTime"]
    flight.Price = row["Price"]
    flights_list.append(flight)


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


h_altitude = 0
h_longitude = 0
h_latitude = 0
for flight in flights_list:
    if flight.DestinationAirport == main.dest_airport:
        h_altitude = flight.DestinationAirport_Altitude
        h_longitude = flight.DestinationAirport_Longitude
        h_latitude = flight.DestinationAirport_Latitude
        # print(distance(flight.SourceAirport_Latitude, h_latitude, flight.SourceAirport_Longitude, h_longitude), "K.M")
        break


def cost_func(f: FLight):  # cost funtion is a linear combination of price and fly time of the flight.
    return round(((f.Price / 1000) * 3 + f.FlyTime), 3)


# making Adjacency dic
graph_astar = {}
for flight in flights_list:
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
graph_djk = {}
for flight in flights_list:
    if flight.SourceAirport not in graph_djk.keys():
        graph_djk[flight.SourceAirport] = {flight.DestinationAirport: cost_func(flight)}
    else:
        graph_djk[flight.SourceAirport][flight.DestinationAirport] = cost_func(flight)
