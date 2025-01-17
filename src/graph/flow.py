import networkx as nx


class InformationFlow:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id):
        self.graph.add_node(node_id)

    def add_edge(self, source, target, weight):
        self.graph.add_edge(source, target, weight=weight)

    def simulate_flow(self, source, target):
        try:
            path = nx.shortest_path(
                self.graph, source=source, target=target, weight='weight')
            return path
        except nx.NetworkXNoPath:
            return None
