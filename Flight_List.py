import pandas as pd

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
    flight.DestinationAirport_City = row["DestinationAirport_City"]
    flight.DestinationAirport_Country = row["DestinationAirport_Country"]
    flight.Distance = row["Distance"]
    flight.FlyTime = row["FlyTime"]
    flight.Price = row["Price"]
    flights_list.append(flight)


def cost_func(f: FLight):  # cost funtion is a linear combination of price and fly time of the flight.
    return round(((f.Price / 1000) * 3 + f.FlyTime), 3)


# making Adjacency dic
graph = {}
for flight in flights_list:
    if flight.SourceAirport not in graph.keys():
        graph[flight.SourceAirport] = {flight.DestinationAirport: cost_func(flight)}
    else:
        graph[flight.SourceAirport][flight.DestinationAirport] = cost_func(flight)

