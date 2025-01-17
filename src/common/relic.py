import json
from typing import List, Dict, Any


class Relic:
    """
    Represents an agent's motif and personality traits.
    """

    def __init__(self, motif: str, personality: Dict[str, Any]):
        """
        Initialize a new Relic.

        :param motif: The agent's narrative motif.
        :param personality: A dictionary representing the agent's personality traits.
        """
        self.motif = motif
        self.personality = personality

    def to_dict(self):
        """
        Convert the Relic to a dictionary.

        :return: A dictionary representation of the Relic.
        """
        return {
            "motif": self.motif,
            "personality": self.personality
        }

    def __repr__(self):
        """
        Return a string representation of the Relic.
        """
        return f"Relic(motif={self.motif}, personality={self.personality})"
