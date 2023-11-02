import heapq

from pandas import Series
from pandas.core.arrays import ExtensionArray

from Time import Time
from Dijkstra import Dijkstra
from typing import Set, Any, Union

import networkx as nx
import pandas as pd

# Step 1: Read the CSV file
flight_data = pd.read_csv('flight_data.csv')

# Step 2: Create an empty directed graph
flight_graph = nx.DiGraph()

# Add nodes for airports
all_airports: Set[Any] = set(flight_data['SourceAirport']).union(
    set(flight_data['DestinationAirport']))  # The set() function is used to create a set,
# which automatically eliminates duplicates,
# ensuring that each airport name is unique.
for airport in all_airports:
    flight_graph.add_node(airport)

# Add directed edges for flight routes
for index, row in flight_data.iterrows():  # Extracting fields from data frame , each represents a flight route
    source_airport = row['SourceAirport']  # row['ColumnName'] is used to access the value in each  column.
    destination_airport = row['DestinationAirport']
    distance = row['Distance']
    price = row['Price']
    duration = row['FlyTime']
    source_country = row['SourceAirport_Country']
    destination_country = row['DestinationAirport_Country']
    source_city = row['SourceAirport_City']
    destination_city = row['DestinationAirport_City']
    flight_graph.add_edge(source_airport, destination_airport, distance=distance, price=price,
                          duration=duration, source_country = source_country, destination_country = destination_country,
                          source_city = source_city, destination_city = destination_city)  # Adding attributes




starting_airport: str
ending_airport: str


input_string = input("Enter Path: ")

starting_airport, ending_airport = input_string.split(" - ")

dijkstra = Dijkstra(flight_graph)
time_inst = Time()
time_inst.Time_starting_()

# Find the shortest flight route from 'San Francisco' to 'New York'.
shortest_path, total_distance = dijkstra.find_shortest_path(starting_airport, ending_airport)

time_inst.Time_Ending_()

# Calculate the execution time in seconds
execution_time = time_inst.Execution() * 1000

minutes, seconds = divmod(execution_time / 1000, 60)
seconds, milliseconds = divmod(seconds, 1)
milliseconds = int(milliseconds * 1000)

if shortest_path:

    # Convert the execution time to minutes and seconds
    minutes, seconds = divmod(execution_time, 60)

    # Print the execution time in minutes and seconds
    print("Dijkstra")
    print("Execution time: {} minutes {} seconds {} milliseconds".format(int(minutes), int(seconds), milliseconds))
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    total_price = 0
    total_duration = 0
    flight_NO = 1
    for i in range(len(shortest_path) - 1):
        departure_airport = shortest_path[i]
        arrival_airport = shortest_path[i + 1]
        flight_info = flight_graph[departure_airport][arrival_airport]
        total_price += flight_info['price']
        total_duration += flight_info['duration']
        print(f"Flight #{flight_NO}")
        print(

            f" From: {flight_info['source_city']}-{departure_airport} . {flight_info['source_country']}\n "
            f"To: {flight_info['destination_city']}-{arrival_airport} . {flight_info['destination_country']}\n"
            f" Distance: {flight_info['distance']} km\n"
            f" Price: ${flight_info['price']}\n"
            f" Duration: {flight_info['duration']} hours")

        flight_NO = flight_NO + 1
        print("----------------------------")
    print(f"Total Distance: {total_distance} km")
    print(f"Total Price: ${total_price}")
    print(f"Total Duration: {total_duration} hours")
else:
    print("No flight route found.")
