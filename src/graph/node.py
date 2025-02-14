from ..common.base import BaseNetwork, BaseMessage
from ..common.broadcast import Broadcast
from state import WorldState
import block
import chain
import random
import uuid


class Node:
    """
    Represents a node to control the dynamics of the network.
    """

    def __init__(self, base_network: BaseNetwork, p: float, role: str):
        """
        Initialize a new node.

        :param base_network: A BaseNetwork object representing the base network.
        :param p: Probability of broadcasting a message to another node.
        :param role: Role of the node in the network.
        """
        self.base_network = base_network
        self.broadcast = Broadcast([], [base_network])
        self.p = p
        self.identity = None
        self.node_id = str(uuid.uuid4())
        self.role = role

    def broadcast_messages(self, message: BaseMessage):
        """
        Broadcast messages to all nodes in the network.

        Each message is sent with a probability p.
        """
        for node in self.base_network.graph.nodes():
            if random.random() < self.p:
                new_message = BaseMessage(
                    sender=self.node_id,
                    receiver=node,
                    message_type=message.message_type,
                    content=message.content,
                    contribution_metric=-1
                )
                self.broadcast.messages.append(new_message)

    def evaluate_messages(self, state: WorldState):
        """
        Evaluate the messages received from all nodes in the network using DeepSeek API.
        """
        for message in self.broadcast.messages:
            # Evaluate the contribution_metric using DeepSeek API
            message.contribution_metric = state.evaluate(
                message)

    def cherrypick_messages(self):
        """
        Cherrypick the most important messages to commit to the block representing the current state of the network.
        """
        for message in self.broadcast.messages:
            if message.contribution_metric > 0.5:
                self.chain.add_block(message)


class SuperNode:
    """
    Represents a central node dominating the network out of the base network.

    It is responsible for broadcasting messages to all nodes in the network, randomly selecting a set of nodes and sending messages to them.

    It is also responsible for receiving messages from all nodes in the network and cherrypicking the most important messages to commit to the block representing the current state of the network.
    """
