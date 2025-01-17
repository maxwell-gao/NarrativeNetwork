from src.common.base import BaseMessage

# Define system and user prompts
system_prompt = "You are a helpful assistant and a storyteller."
user_prompt = "Tell me a story about a dragon."

# Create a message with structured content
content = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]
message = BaseMessage(
    sender="DM",
    receiver="ALL",
    message_type="global_event",
    content=content
)

# Print the message
print("Message:", message)

# Convert the message to JSON
json_str = message.to_json()
print("Message JSON:", json_str)