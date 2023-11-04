from graph_module import *
from a_star_module import *
from dijkstra_module import *
from data_module import *
import pandas as pd


if __name__ == '__main__':
    pass


def readData(input_values):
    df = pd.read_csv("Flight_Data.csv", encoding="latin-1", on_bad_lines="skip")
    g = Graph()
    size = len(df.SourceAirport_City)
    for i in range(0, size):
        source_data = Data(df.SourceAirport[i], df.SourceAirport_City[i], df.SourceAirport_Latitude[i],
                           df.SourceAirport_Longitude[i], df.SourceAirport_Country[i])

        destination_data = Data(df.DestinationAirport[i], df.DestinationAirport_City[i],
                                df.DestinationAirport_Latitude[i], df.DestinationAirport_Longitude[i],
                                df.DestinationAirport_Country[i])

        edge = Edge(df.Distance[i], df.FlyTime[i], df.Price[i])

        g.add_edge(edge, source_data, destination_data)

