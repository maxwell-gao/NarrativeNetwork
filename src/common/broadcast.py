import json
from typing import Any, Dict, List
from base import BaseNetwork, BaseMessage


class Broadcast:
    """
    Represents record list of BaseMessage and list of the BaseNetwork.
    """

    def __init__(self, messagesList: List[BaseMessage], networkList: List[BaseNetwork]):
        """
        Initialize a new Broadcast.

        :param messages: A list of BaseMessage objects.
        :param evolution: A list of BaseNetwork objects.
        """
        self.messages = messagesList
        self.networkList = networkList

    def to_json(self):
        """
        Serialize the broadcast to a JSON string.

        :return: A JSON string representing the broadcast.
        """
        return json.dumps(
            {
                "messages": [message.to_dict() for message in self.messages],
                "networkList": [network.to_dict() for network in self.networkList]
            },
            indent=4
        )

    def __repr__(self):
        """
        Return a string representation of the Broadcast.
        """
        return f"Broadcast(messages={self.messages}, networkList={self.networkList})"

    def from_json(cls, json_str: str):
        """
        Deserialize a JSON string into a Broadcast object.

                :param json_str: A JSON string representing the broadcast.
                :return: A Broadcast object.
                """
        data = json.loads(json_str)
        return cls(
            messagesList=[BaseMessage.from_dict(
                message) for message in data["messages"]],
            networkList=[BaseNetwork.from_dict(
                network) for network in data["networkList"]]
        )

    def update(self, message: BaseMessage, network: BaseNetwork):
        """
        Add a new message and network to the broadcast.

        :param message: A BaseMessage object.
        :param network: A BaseNetwork object.
        """
        self.messages.append(message)
        self.networkList.append(network)
