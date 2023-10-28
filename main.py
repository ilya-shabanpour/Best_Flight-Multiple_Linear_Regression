import pandas as pd

df = pd.read_csv("Flight_Data.csv")

user_input = input("Please enter source and destination airport:")
input_split = user_input.split(" - ")
src_port = input_split[0]  # putting input airports in variables
dest_port = input_split[1]




