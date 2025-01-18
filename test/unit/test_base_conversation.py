# test/unit/test_base_conversation.py
import unittest
from src.common.base import BaseConversation, BaseMessage
from uuid import uuid4

class TestBaseConversation(unittest.TestCase):
    def test_conversation_initialization(self):
        """
        Test the initialization of a BaseConversation object.
        """
        # Create a conversation with an initial message
        initial_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "Hello, DeepSeek!"}]
        )
        conversation = BaseConversation(conversation_id=str(uuid4()), messages=[initial_message])

        # Verify the conversation ID and messages
        self.assertIsNotNone(conversation.conversation_id)
        self.assertEqual(len(conversation.messages), 1)
        self.assertEqual(conversation.messages[0].content[0]["content"], "Hello, DeepSeek!")

    def test_add_message(self):
        """
        Test adding a message to the conversation.
        """
        # Create an empty conversation
        conversation = BaseConversation(conversation_id=str(uuid4()), messages=[])

        # Add a user message
        user_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "What's the weather today?"}]
        )
        conversation.add_message(user_message)

        # Verify the message was added
        self.assertEqual(len(conversation.messages), 1)
        self.assertEqual(conversation.messages[0].content[0]["content"], "What's the weather today?")

    def test_to_json(self):
        """
        Test serializing the conversation to JSON.
        """
        # Create a conversation with a message
        user_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "Tell me a joke."}]
        )
        conversation = BaseConversation(conversation_id=str(uuid4()), messages=[user_message])

        # Serialize to JSON
        json_str = conversation.to_json()
        self.assertIn('"conversation_id":', json_str)
        self.assertIn('"messages":', json_str)
        self.assertIn('"Tell me a joke."', json_str)

    def test_from_json(self):
        """
        Test deserializing a conversation from JSON.
        """
        # Create a conversation with a message
        user_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "What's the capital of France?"}]
        )
        conversation = BaseConversation(conversation_id=str(uuid4()), messages=[user_message])

        # Serialize to JSON
        json_str = conversation.to_json()

        # Deserialize from JSON
        new_conversation = BaseConversation.from_json(json_str)

        # Verify the deserialized conversation
        self.assertEqual(new_conversation.conversation_id, conversation.conversation_id)
        self.assertEqual(len(new_conversation.messages), 1)
        self.assertEqual(new_conversation.messages[0].content[0]["content"], "What's the capital of France?")

    def test_add_api_message(self):
        """
        Test adding a message and simulating an API response.
        """
        # Mock the DeepSeek API response
        def mock_query(user_message: str) -> str:
            return f"Mock response to: {user_message}"

        # Create a conversation
        conversation = BaseConversation(conversation_id=str(uuid4()), messages=[])

        # Add a user message and simulate an API response
        user_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "What's the weather today?"}]
        )
        conversation.add_api_message(user_message)
        # Print the conversation
        pprint("Conversation:", conversation)
        # Verify the conversation history
        self.assertEqual(len(conversation.messages), 2)
        self.assertEqual(conversation.messages[0].content[0]["content"], "What's the weather today?")
        # self.assertEqual(conversation.messages[1].content[0]["content"], "Mock response to: What's the weather today?")
        # Start multi-round conversation
        user_message = BaseMessage(
            sender="User",
            receiver="DeepSeek",
            message_type="user_message",
            content=[{"role": "user", "content": "Tell me a joke."}]
        )
        conversation.add_api_message(user_message)
        # Print the conversation
        pprint("Conversation:", conversation)
        # Verify the conversation history
        self.assertEqual(len(conversation.messages), 4)

if __name__ == "__main__":
    unittest.main()