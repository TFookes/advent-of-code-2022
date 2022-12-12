import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

grid = None

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        source = None
        destination = None

        grid = nx.DiGraph()

        for y, line in enumerate(lines):
            for x, letter in enumerate(line):
                if letter == "S": 
                    grid.add_node((x, y), value=1, start=True)
                    current_value = 1
                    source = (x, y)
                elif letter == "E":
                    grid.add_node((x, y), value=26, end=True)
                    current_value = 26
                    destination = (x, y)
                else: 
                    current_value = ord(letter) - 96
                    grid.add_node((x, y), value=ord(letter) - 96)

                if not x == 0:
                    if current_value - previous_value <= 1: grid.add_edge((x - 1, y), (x, y))
                    if previous_value - current_value <= 1: grid.add_edge((x, y), (x - 1, y))

                if not y == 0:
                    if current_value - dict(grid.nodes(data="value"))[(x, y - 1)] <= 1: grid.add_edge((x, y - 1), (x, y))
                    if dict(grid.nodes(data="value"))[(x, y - 1)] - current_value <= 1: grid.add_edge((x, y), (x, y - 1))

                previous_value = current_value
            
            previous_line = line

        path = nx.single_source_dijkstra(grid, source, destination)

        print(path)

        #pos = {(x,y):(x,-y) for x,y in grid.nodes()}
        #nx.draw(grid, pos, with_labels=True, labels=dict(grid.nodes(data="value")), arrows=False)
        #h = grid.subgraph(path[1])
        #nx.draw_networkx_nodes(h, pos=pos, node_color='red') 
        #nx.draw_networkx_edges(h, pos=pos, edge_color='red', arrows=True)
        #plt.show()