from ..common.base import BaseNetwork, BaseMessage
from ..common.broadcast import Broadcast
import state
import chain
import random


class CentralNode:
    """
    Represents a central node dominating the network out of the base network.

    It is responsible for broadcasting messages to all nodes in the network, randomly selecting a set of nodes and sending messages to them.

    It is also responsible for receiving messages from all nodes in the network and cherrypicking the most important messages to commit to the block representing the current state of the network.
    """

    def __init__(self, base_network: BaseNetwork, p):
        """
        Initialize a new CentralNod.

        :param base_network: A BaseNetwork object representing the base network.
        """
        self.base_network = base_network
        self.broadcast = Broadcast([], [base_network])
        self.chain = chain.Chain()
        self.p = p

        def broadcast_messages(self, messagee: BaseMessage):
            """
            Broadcast messages to all nodes in the network.

            Each message is sent with a probability p.
            """
            for node in self.base_network.graph.nodes():
                if random.random() < self.p:
                    message = BaseMessage(
                        sender="CentralNod", receiver=node, content=messagee.content)
                    self.broadcast.messages.append(message)
