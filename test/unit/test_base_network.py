import unittest
import json
from src.common.base import BaseNetwork
from itertools import permutations


class TestBaseNetwork(unittest.TestCase):

    def test_initialization(self):
        """Test that the graph is initialized correctly."""
        # Check if all agent IDs are in the graph
        self.assertCountEqual(list(self.network.graph.nodes()), self.agent_ids)

        # Check that the graph is directed (no bidirectional edges unless explicitly added)
        for start, end in self.network.graph.edges():
            self.assertFalse(self.network.graph.has_edge(end, start))

    def test_uuid_generation(self):
        """Test that each instance has a unique UUID."""
        network2 = BaseNetwork(self.agent_ids)
        # UUIDs should be unique
        self.assertNotEqual(self.network.uuid, network2.uuid)

    def to_json(self):
        """
        Convert the directed graph to a JSON-formatted string.

        Returns:
            str: JSON representation of the directed graph.
        """
        # Convert the graph to a dictionary with node IDs as keys and neighbors as values
        graph_dict = {str(node): list(self.graph.successors(node))
                      for node in self.graph.nodes}
        return json.dumps(graph_dict, indent=4)

    def test_edge_probability(self):
        """Test that edges are generated with the specified probability."""
        # Create a network with p=1 (all possible edges should exist)
        network_all_edges = BaseNetwork(self.agent_ids, p=1.0)
        expected_edges = list(permutations(self.agent_ids, 2))
        for start, end in expected_edges:
            self.assertIn(end, network_all_edges.graph[start])

        # Create a network with p=0 (no edges should exist)
        network_no_edges = BaseNetwork(self.agent_ids, p=0.0)
        for start in network_no_edges.graph:
            self.assertEqual(len(network_no_edges.graph[start]), 0)

    def test_print(self):
        agent_ids = [1, 2, 3, 4, 5]
        network = BaseNetwork(agent_ids)
        print("Network UUID:", network)  # Print the UUID
        print("Directed Graph (JSON):")
        # Print the JSON representation of the directed graphk
        print(network.to_json())

    def setUp(self):
        """Set up test fixtures."""
        self.agent_ids = [1, 2, 3]
        self.network = BaseNetwork(self.agent_ids, p=0.5)

    def test_disconnect_edge(self):
        """Test disconnecting an edge."""
        self.network.connect_edge(1, 2)
        self.assertTrue(self.network.graph.has_edge(1, 2))
        self.network.disconnect_edge(1, 2)
        self.assertFalse(self.network.graph.has_edge(1, 2))

    def test_connect_edge(self):
        """Test connecting a new edge."""
        self.network.disconnect_edge(1, 2)
        self.assertFalse(self.network.graph.has_edge(1, 2))
        self.network.connect_edge(1, 2)
        self.assertTrue(self.network.graph.has_edge(1, 2))

    def test_reverse_edge(self):
        """Test reversing an edge."""
        self.network.connect_edge(1, 2)
        self.assertTrue(self.network.graph.has_edge(1, 2))
        # Simulate agreement
        reversed = self.network.reverse_edge(1, 2)
        if reversed:
            self.assertFalse(self.network.graph.has_edge(1, 2))
            self.assertTrue(self.network.graph.has_edge(2, 1))
        else:
            self.assertTrue(self.network.graph.has_edge(1, 2))
            self.assertFalse(self.network.graph.has_edge(2, 1))


if __name__ == "__main__":
    unittest.main()
