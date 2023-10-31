import pandas as pd
import Flight_List
import dijkstra

df = pd.read_csv("Flight_Data.csv")
data2 = df.drop(columns='Airline')
df2 = data2.drop_duplicates(keep='first')
extracted_col = df["Airline"]
df2.insert(0, 'Airline', extracted_col)


user_input = input("Please enter source and destination airport:")
input_split = user_input.split(" - ")
src_airport = input_split[0]  # putting input airports in variables
dest_airport = input_split[1]

dijkstra.dijkstra(Flight_List.graph, src_airport, dest_airport)