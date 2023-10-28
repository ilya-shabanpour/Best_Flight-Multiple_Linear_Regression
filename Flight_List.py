import main
df = main.df2


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
for i in df.index:  # allocating all "needed" attributes
    flight = FLight()
    flight.Airline = df.iloc[i].iloc[0]
    flight.SourceAirport = df.iloc[i].iloc[1]
    flight.DestinationAirport = df.iloc[i].iloc[2]
    flight.SourceAirport_City = df.iloc[i].iloc[3]
    flight.SourceAirport_Country = df.iloc[i].iloc[4]
    flight.DestinationAirport_City = df.iloc[i].iloc[8]
    flight.DestinationAirport_Country = df.iloc[i].iloc[9]
    flight.Distance = df.iloc[i].iloc[13]
    flight.FlyTime = df.iloc[i].iloc[14]
    flight.Price = df.iloc[i].iloc[15]
    flights_list.append(flight)
