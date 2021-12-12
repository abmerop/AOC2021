import sys
from Part1 import CaveGraph


class DerivCaveGraph(CaveGraph):

    def __init__(self, input_file):
        super().__init__(input_file)

        self.visited_small_caves = []

    def walk(self, node, path=[]):

        assert(node in self.nodes)
        
        # Terminate if (a) Reach "end" or revisted a small cave twice
        if node == "end":
            self.all_paths.append(path)
            return
        elif self.is_small_cave(node) and node in path:
            # Allow it if no other small node is in the list twice and not start/end
            if node != "start" and node != "end":
                has_duplicates = False
                for tmp_node in path:
                    if self.is_small_cave(tmp_node) and path.count(tmp_node) > 1:
                        has_duplicates = True
                        break
                if has_duplicates:
                    return
            else:
                return

        path.append(node)

        for neighbor in self.nodes[node]:
            neighbor_path = path.copy()
            self.walk(neighbor, neighbor_path)


if __name__ == "__main__":
    cave_graph = DerivCaveGraph(sys.argv[1])
    cave_graph.walk("start")
    cave_graph.print_paths()