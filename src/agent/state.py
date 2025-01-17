from common.relic import Relic
from typing import List, Dict, Any


class AgentState:

    """
    Represents the state of an agent, including its Relic, private event chain, and graph position.
    """

    def __init__(
        self,
        relic: Relic,
        private_event_chain: List[Dict[str, Any]],
        graph_position_index: int
    ):
        """
        Initialize a new AgentState.

        :param relic: The agent's Relic object.
        :param private_event_chain: A list of private events/memories.
        :param graph_position_index: The agent's position in the agent graph.
        """
        self.relic = relic
        self.private_event_chain = private_event_chain
        self.graph_position_index = graph_position_index

    def to_dict(self):
        """
        Convert the AgentState to a dictionary.

        :return: A dictionary representation of the AgentState.
        """
        return {
            "relic": self.relic.to_dict(),
            "private_event_chain": self.private_event_chain,
            "graph_position_index": self.graph_position_index
        }

    def __repr__(self):
        """
        Return a string representation of the AgentState.
        """
        return (f"AgentState(relic={self.relic}, private_event_chain={self.private_event_chain}, "
                f"graph_position_index={self.graph_position_index})")
