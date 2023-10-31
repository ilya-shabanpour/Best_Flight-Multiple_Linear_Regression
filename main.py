import pandas as pd
import Flight_List

# df = pd.read_csv("Flight_Data.csv")
# data2 = df.drop(columns='Airline')
# df2 = data2.drop_duplicates(keep='first')
# extracted_col = df["Airline"]
# df2.insert(0, 'Airline', extracted_col)


user_input = input("Please enter source and destination airport:")
input_split = user_input.split(" - ")
src_airport = input_split[0]  # putting input airports in variables
dest_airport = input_split[1]


def output_files(djk: list, a_star: list):
    output_file_djk = open("[8]-UIAI4021-PR1-Q1_djk.txt", "w+")
    output_file_AStar = open("[8]-UIAI4021-PR1-Q1_AStar.txt", "w+")

    output_file_djk.write("Dijkstra Algorithm\n")
    output_file_djk.write("Execution Time: ")
    # output_file_djk.write(,"\n") # TODO
    output_file_djk.write(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

    c = 0
    for i in range(len(djk)-1):
        output_file_djk.write("Flight #" + str(i) + "\nFrom:")



    output_file_djk.close()
    output_file_AStar.close()
