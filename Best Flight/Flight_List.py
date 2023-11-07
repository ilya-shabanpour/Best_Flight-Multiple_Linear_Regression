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

