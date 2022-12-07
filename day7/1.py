import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

def add_size_to_parents(graph, node, size, sizes):
    nx.set_node_attributes(graph, {node: sizes[node] + size}, "size")
    for parent in graph.predecessors(node):
        add_size_to_parents(graph, parent, size, sizes)


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip().split(" ") for line in lines]
        disk = nx.DiGraph()
        current_node = None
        node_num = 0

        for line in lines:
            if line[0] == "$" and line[1] == "cd": #INSTRUCTION - CD
                if line[2] == "..": ## Move back up a level
                    for node in disk.predecessors(current_node): 
                        current_node = node
                        break
                else: ## Move down into tree
                    disk.add_node(f"{line[2]}.{node_num}", size=0, directory=True)
                    if current_node != None: ## Not the first node
                        disk.add_edge(current_node, f"{line[2]}.{node_num}")
                        
                    current_node = f"{line[2]}.{node_num}"
            elif line[0] == "dir": #DIRECTORY
                pass
            elif line[0].isnumeric(): #FILE
                disk.add_node(f"{line[1]}.{node_num}", size=int(line[0]), directory=False)
                disk.add_edge(current_node, f"{line[1]}.{node_num}")
                add_size_to_parents(disk, f"{line[1]}.{node_num}", int(line[0]), nx.get_node_attributes(disk, 'size'))

            node_num += 1

        print(nx.is_forest(disk))

        sum = 0
        for node, attributes in disk.nodes(data=True):
            if attributes['directory'] == True and attributes["size"] <= 100000:
                print(node, attributes)
                sum += attributes["size"]

        print(sum)

        pos = graphviz_layout(disk, prog="dot")
        nx.draw(disk, pos, with_labels=True, arrows=True)
        plt.show()