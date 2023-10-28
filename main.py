import pandas as pd

df = pd.read_csv("Flight_Data.csv")

data2 = df.drop(columns='Airline')

df2 = data2.drop_duplicates(keep='first')

extracted_col = df["Airline"]
df2.insert(0, 'Airline', extracted_col)
