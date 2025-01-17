# src/worldblock/chain.py
from .block import WorldBlock


class WorldChain:
    """
    A chain of WorldBlocks, representing the history of the world state.
    """

    def __init__(self):
        """
        Initialize the WorldChain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block (the first block in the chain).

        :return: The genesis block (WorldBlock object).
        """
        return WorldBlock(0, {"info_flow": {}, "dominance": {}}, "0")

    def add_block(self, world_state):
        """
        Add a new block to the chain.

        :param world_state: A dictionary representing the new world state.
        :return: The newly added block (WorldBlock object).
        """
        previous_block = self.get_latest_block()
        new_block = WorldBlock(
            index=previous_block.index + 1,
            world_state=world_state,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)
        return new_block

    def get_latest_block(self):
        """
        Get the latest block in the chain.

        :return: The latest block (WorldBlock object).
        """
        return self.chain[-1]

    def get_block_by_index(self, index):
        """
        Get a block by its index.

        :param index: The index of the block (integer).
        :return: The block at the specified index (WorldBlock object), or None if not found.
        """
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None

    def get_block_by_hash(self, block_hash):
        """
        Get a block by its hash.

        :param block_hash: The hash of the block (string).
        :return: The block with the specified hash (WorldBlock object), or None if not found.
        """
        for block in self.chain:
            if block.hash == block_hash:
                return block
        return None

    def is_chain_valid(self):
        """
        Validate the entire chain.

        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if not current_block.is_valid(previous_block):
                return False
        return True

    def __repr__(self):
        """
        Return a string representation of the chain.
        """
        return f"WorldChain(blocks={len(self.chain)}, valid={self.is_chain_valid()})"
