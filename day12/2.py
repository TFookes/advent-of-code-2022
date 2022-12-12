import networkx as nx

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
                    #print((i, j), current_value, previous_value)
                    if current_value - previous_value <= 1: grid.add_edge((x - 1, y), (x, y))
                    if previous_value - current_value <= 1: grid.add_edge((x, y), (x - 1, y))

                if not y == 0:
                    #print((i, j), current_value, dict(grid.nodes(data="value"))[(i - 1, j)])
                    if current_value - dict(grid.nodes(data="value"))[(x, y - 1)] <= 1: grid.add_edge((x, y - 1), (x, y))
                    if dict(grid.nodes(data="value"))[(x, y - 1)] - current_value <= 1: grid.add_edge((x, y), (x, y - 1))

                previous_value = current_value
            
            previous_line = line

        nodes = dict(grid.nodes(data="value"))
        sources = []
        for i, value in enumerate(list(nodes.values())):
            if value == 1: sources = sources + [list(nodes.keys())[i]]

        path_lengths = []
        for source in sources:
            try:
                path_lengths = path_lengths + [nx.dijkstra_path_length(grid, source, destination)]
            except:
                pass # No path
        
        print(path_lengths)
        print(min(path_lengths))