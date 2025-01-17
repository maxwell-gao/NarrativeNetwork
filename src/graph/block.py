import hashlib
import time
import json
from state import WorldState 


class WorldBlock:
    def __init__(self, index, world_state, previous_hash):
        """
        Initialize the World Block.

        :param index: The index of the block (integer).
        :param world_state: The current state of the world (json).
        :param previous_hash: The hash of the previous block (str).
        """
        self.index = index
        self.timestamp = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime())  # Current timestamp
        self.world_state = world_state
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the current block.

        :return: The hash value (string).
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "world_state": self.world_state,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def is_valid(self, previous_block):
        # Verify if the hash value is correct
        if self.hash != self.calculate_hash():
            return False
        # Verify if the link to the previous block is valid
        if previous_block and self.previous_hash != previous_block.hash:
            return False
        return True

    def __repr__(self):
        """
        Return the string representation of the block.
        """
        return (f"WorldBlock(index={self.index}, timestamp={self.timestamp}, "
                f"world_state={self.world_state}, previous_hash={self.previous_hash}, "
                f"hash={self.hash})")
