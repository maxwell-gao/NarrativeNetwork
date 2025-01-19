import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List
import random
from itertools import permutations

# Use python-dotenv to read .env file
from dotenv import load_dotenv
from openai import OpenAI
import networkx as nx

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


class BaseMessage:
    """
    Represents a message in the broadcast system.
    """

    def __init__(
        self,
        sender: str,
        receiver: str,
        message_type: str,
        content: List[Dict[str, str]],
    ):
        """
        Initialize a new Message.

        :param sender: The ID of the sender.
        :param receiver: The ID of the receiver.
        :param message_type: The type of message (e.g., "global_event", "local_event").
        :param content: The content of the message.
        """
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.content = content
        self.timestamp = datetime.now().isoformat()

    def to_json(self):
        """
        Serialize the message to a JSON string.

        :return: A JSON string representing the message.
        """
        return json.dumps(
            {
                "sender": self.sender,
                "receiver": self.receiver,
                "message_type": self.message_type,
                "content": self.content,
                "timestamp": self.timestamp,
            },
            indent=4,
        )

    @classmethod
    def from_json(cls, json_str: str):
        """
        Deserialize a JSON string into a Message object.

        :param json_str: A JSON string representing the message.
        :return: A Message object.
        """
        if isinstance(json_str, str):
            data = json.loads(json_str)
        else:
            data = json_str
        return cls(
            sender=data["sender"],
            receiver=data["receiver"],
            message_type=data["message_type"],
            content=data["content"],
        )

    def __repr__(self):
        """
        Return a string representation of the message.
        """
        return (
            f"Message(sender={self.sender}, receiver={self.receiver}, "
            f"message_type={self.message_type}, content={self.content}, "
            f"timestamp={self.timestamp})"
        )


class BaseConversation:
    """
    Represents a conversation with client via DeepSeek API.
    """

    def __init__(self, conversation_id: str, messages: List[BaseMessage]):
        """
        Initialize a new Conversation.

        :param conversation_id: The ID of the conversation.
        :param messages: A list of messages in the conversation.
        """
        self.conversation_id = conversation_id
        self.messages = messages

    def to_json(self):
        """
        Serialize the conversation to a JSON string.

        :return: A JSON string representing the conversation.
        """
        return json.dumps(
            {
                "conversation_id": self.conversation_id,
                "messages": [
                    json.loads(message.to_json()) for message in self.messages
                ],
            },
            indent=4,
        )

    @classmethod
    def from_json(cls, json_str: str):
        """
        Deserialize a JSON string into a Conversation object.

        :param json_str: A JSON string representing the conversation.
        :return: A Conversation object.
        """
        data = json.loads(json_str)
        messages = [BaseMessage.from_json(message)
                    for message in data["messages"]]
        return cls(conversation_id=data["conversation_id"], messages=messages)

    def add_message(self, message: BaseMessage):
        """
        Add a message to the conversation.

        :param message: The message to add to the conversation.
        """
        self.messages.append(message)

    def add_api_message(self, message: BaseMessage):
        """
        Add a message to the conversation.

        :param message: The message to add to the conversation.
        """
        self.messages.append(message)
        # Prepare the messages for the API call
        api_messages = [
            {
                "role": "user",
                "content": json.dumps(msg.content, default=str) if msg.content else "",
            }
            for msg in self.messages[-50:]
        ]

        # Call the DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-chat", messages=api_messages
        )

        # Extract the system message from the response
        system_message_content = response.choices[0].message
        system_message = BaseMessage(
            sender="system",
            receiver=self.conversation_id,
            message_type="system_response",
            content=[{"text": system_message_content}],
        )
        # Add the system message to the conversation
        self.messages.append(system_message)

    def __repr__(self):
        """
        Return a string representation of the conversation.
        """
        return (
            f"Conversation(conversation_id={self.conversation_id}, "
            f"messages={self.messages})"
        )


class BaseAgent:
    """
    A base class for all agents in the system.
    """

    def __init__(self):
        """
        Initialize a new BaseAgent with a unique identifier.
        """
        self.agent_id = str(uuid.uuid4())  # Generate a unique ID for the agent

    def to_json(self) -> str:
        """
        Convert the agent's state to a JSON string.

        :return: A JSON string representing the agent's state.
        """
        return json.dumps({"agent_id": self.agent_id}, indent=4)

    def interact_with_deepseek(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate interaction with the DeepSeek API.

        :param input_data: A dictionary containing input data for the API.
        :return: A dictionary containing the API's response.
        """
        # Simulate a API response
        return {
            "agent_id": self.agent_id,
            "input": input_data,
            "output": {"status": "success", "message": "Processed by DeepSeek API"},
        }

    def __repr__(self):
        """
        Return a string representation of the agent.
        """
        return f"BaseAgent(agent_id={self.agent_id})"


class BaseNetwork:
    def __init__(self, agent_ids, p=0.5):
        """
        Initialize a random directed network using NetworkX.

        Args:
            agent_ids (list): List of agent IDs.
            p (float, optional): Probability of generating a directed edge. Defaults to 0.5.
        """
        self.agent_ids = agent_ids
        self.p = p
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(agent_ids)
        self.generate_random_digraph()
        # Generate a UUID and store it as a string
        self.uuid = str(uuid.uuid4())

    def generate_random_digraph(self):
        """
        Generate a random directed graph with the specified edge probability.
        """
        for start, end in permutations(self.agent_ids, 2):
            if random.random() < self.p:
                self.graph.add_edge(start, end)

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

    def __repr__(self):
        """
        Return the string representation of the object (its UUID).

        Returns:
            str: UUID of the object.
        """
        return self.uuid

    def disconnect_edge(self, start, end):
        """
        Disconnect a specific edge between two nodes.

        Args:
            start: The starting node ID.
            end: The ending node ID.
        """
        if self.graph.has_edge(start, end):
            self.graph.remove_edge(start, end)

    def connect_edge(self, start, end):
        """
        Connect a new edge between two nodes.

        Args:
            start: The starting node ID.
            end: The ending node ID.
        """
        if not self.graph.has_edge(start, end):
            self.graph.add_edge(start, end)

    def reverse_edge(self, start, end):
        """
        Reverse the direction of a specific edge if both nodes agree.

        Args:
            start: The starting node ID.
            end: The ending node ID.

        Returns:
            bool: True if the edge was reversed, False otherwise.
        """
        if self.graph.has_edge(start, end):
            # Simulate agreement between nodes
            agree = self.agreement(start, end)
            if agree:
                self.graph.remove_edge(start, end)
                self.graph.add_edge(end, start)
                return True
        return False

    def agreement(self, start, end):
        """
        Simulate agreement between two nodes to reverse an edge.

        Args:
            start: The starting node ID.
            end: The ending node ID.

        Returns:
            bool: True if both nodes agree, False otherwise.
        """
        # For simplicity, assume both nodes agree 50% of the time
        return random.random() < 0.5
