from graph_module import *
from a_star_module import *
from dijkstra_module import *
from data_module import *
from time_module import *
import pandas as pd

graph = Graph()
dijkstra = Dijkstra(graph)


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


def write_answer(list, execution, file_name, algorithm_name):
    with open(file_name + ".txt", "w", encoding="utf8") as file:
        execution_time = round(execution, 2)
        minutes, seconds = divmod(execution_time, 60)
        file.write(algorithm_name + " algorithm\nExecution Time : " + str(minutes) + "m" + str(seconds) + "s" +
                   "\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
        total_price = 0
        total_distance = 0
        total_fly_time = 0

        for i in range(len(list) - 1):
            values = "Flight #" + str(i + 1) + "\n"
            source_node = list[i]
            source_airport = source_node.data.airport
            source_country = source_node.data.country

            destination_node = list[i + 1]
            destination_airport = destination_node.data.airport
            destination_country = destination_node.data.country

            edge = source_node.neighbors[destination_node]
            price = edge.price
            distance = edge.distance
            fly_time = edge.fly_time

            values += "From: " + source_airport + " , " + source_country + "\nTo: " + \
                      destination_airport + " , " + destination_country + "\n"

            values += "Distance: " + str(distance) + "Km\n"
            values += "Time: " + str(fly_time) + "h\n"
            values += "Price: " + str(price) + "$\n"

            file.write(values + "-------------------------------------\n")

            total_distance += distance
            total_price += price
            total_fly_time += fly_time

        file.write("Total Price: " + str(total_price) + "\nTotal Distance: " +
                   str(total_distance) + "\nTotal Time: " + str(total_fly_time))


if __name__ == '__main__':
    readData()
    # input_values=input("Enter source and destination : ")
    input_values = "Imam Khomeini International Airport - Raleigh Durham International Airport"
    starting_airport, ending_airport = input_values.split(" - ")

    a_star_time = Time()
    a_star_time.Time_starting_()
    a_star_list = a_star_search(graph, starting_airport, ending_airport)
    a_star_time.Time_Ending_()

    dijkstra_time = Time()
    dijkstra_time.Time_starting_()
    dijkstra_list = dijkstra.find_shortest_path(starting_airport, ending_airport)
    dijkstra_time.Time_Ending_()

    write_answer(a_star_list, a_star_time.Execution(), "a_star", "A*")
    write_answer(dijkstra_list, dijkstra_time.Execution(), "dijkstra", "Dijkstra")
