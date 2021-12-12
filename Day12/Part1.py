import sys


class CaveGraph:

    def __init__(self, input_file):
        self.nodes = {}
        self.all_paths = []

        with open(input_file, 'r') as inp:
            for line in inp:
                edge = line.rstrip().split('-')

                # Add left node -> right node connection
                if edge[0] in self.nodes:
                    if not edge[1] in self.nodes[edge[0]]:
                        self.nodes[edge[0]].append(edge[1])
                else:
                    self.nodes[edge[0]] = [edge[1]]

                # Add reverse path right node -> left node connection
                if edge[1] in self.nodes:
                    if not edge[0] in self.nodes[edge[1]]:
                        self.nodes[edge[1]].append(edge[0])
                else:
                    self.nodes[edge[1]] = [edge[0]]

    def is_small_cave(self, node):

        return node == node.lower()

    def walk(self, node, path=[], depth=0):

        assert(node in self.nodes)
        
        # Terminate if (a) Reach "end" or revisted a small cave twice
        if node == "end":
            self.all_paths.append(path)
            return
        elif self.is_small_cave(node) and node in path:
            return

        path.append(node)

        for neighbor in self.nodes[node]:
            # Important: make a copy otherwise it will pass by reference
            # and all of the paths will be the same
            neighbor_path = path.copy()
            self.walk(neighbor, neighbor_path, depth+1)

    def print_paths(self):

        for path in self.all_paths:
            print(path)
        print("There are {} paths".format(len(self.all_paths)))


if __name__ == "__main__":
    cave_graph = CaveGraph(sys.argv[1])
    cave_graph.walk("start")
    cave_graph.print_paths()