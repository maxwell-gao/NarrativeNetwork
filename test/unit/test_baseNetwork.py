import unittest
import json
from src.common.base import BaseNetwork
from itertools import permutations


class TestBaseNetwork(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.agent_ids = [1, 2, 3]
        self.network = BaseNetwork(self.agent_ids, p=0.5)

    def test_initialization(self):
        """Test that the graph is initialized correctly."""
        # Check if all agent IDs are in the graph
        self.assertCountEqual(self.network.graph.keys(), self.agent_ids)

        # Check that the graph is directed (no bidirectional edges unless explicitly added)
        for start, neighbors in self.network.graph.items():
            for end in neighbors:
                self.assertNotIn(start, self.network.graph.get(end, []))

    def test_uuid_generation(self):
        """Test that each instance has a unique UUID."""
        network2 = BaseNetwork(self.agent_ids)
        # UUIDs should be unique
        self.assertNotEqual(self.network.uuid, network2.uuid)

    def test_to_json(self):
        """Test that the to_json method returns a valid JSON string."""
        json_str = self.network.to_json()
        # Check if the JSON string can be loaded back into a Python object
        graph_from_json = json.loads(json_str)
        # Convert original graph keys to strings for comparison
        expected_graph = {str(k): v for k, v in self.network.graph.items()}
        self.assertEqual(graph_from_json, expected_graph)

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

    def print(self):
        agent_ids = [1, 2, 3, 4, 5]
        network = BaseNetwork(agent_ids)
        print("Network UUID:", network)  # Print the UUID
        print("Directed Graph (JSON):")
        # Print the JSON representation of the directed graphk
        print(network.to_json())


if __name__ == "__main__":
    unittest.main()
