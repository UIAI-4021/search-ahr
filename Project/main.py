from graph_module import *
from a_star_module import *
from dijkstra_module import *
from data_module import *
from time_module import *
import pandas as pd


graph = Graph()
dijkstra=Dijkstra(graph)


def readData():
    df = pd.read_csv("Flight_Data.csv", encoding="latin-1", on_bad_lines="skip")
    size = len(df.SourceAirport_City)
    for i in range(0, size):
        source_data = Data(df.SourceAirport[i], df.SourceAirport_City[i], df.SourceAirport_Latitude[i],
                           df.SourceAirport_Longitude[i], df.SourceAirport_Country[i])

        destination_data = Data(df.DestinationAirport[i], df.DestinationAirport_City[i],
                                df.DestinationAirport_Latitude[i], df.DestinationAirport_Longitude[i],
                                df.DestinationAirport_Country[i])

        edge = Edge(df.Distance[i], df.FlyTime[i], df.Price[i])

        graph.add_edge(edge, source_data, destination_data)


if __name__ == '__main__':
    readData()
    # input_values=input("Enter source and destination : ")
    input_values="Imam Khomeini International Airport - Raleigh Durham International Airport"
    starting_airport, ending_airport = input_values.split(" - ")

    a_star_time=Time()
    a_star_time.Time_starting_()
    a_star_list = a_star_search(graph, starting_airport, ending_airport)
    a_star_time.Time_Ending_()

    dijkstra_time = Time()
    dijkstra_time.Time_starting_()
    dijkstra_list = dijkstra.find_shortest_path(starting_airport, ending_airport)
    dijkstra_time.Time_Ending_()
