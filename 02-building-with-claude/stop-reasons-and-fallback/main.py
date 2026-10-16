# https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

"""
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
if response.stop_reason == "end_turn":
    # Process the complete response
    for block in response.content:
        if block.type == "text":
            print(block.text)
"""

"""
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=10,
    messages=[{"role": "user", "content": "Explain quantum physics"}],
)

if response.stop_reason == "max_tokens":
    # Response was truncated
    print("Response was cut off at token limit")
    # Consider making another request to continue
"""

"""
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    stop_sequences=["END", "STOP"],
    messages=[{"role": "user", "content": "Generate text until you say END"}],
)

if response.stop_reason == "stop_sequence":
    print(f"Stopped at sequence: {response.stop_sequence}")
"""


# client = anthropic.Anthropic()
# weather_tool = {
#     "name": "get_weather",
#     "description": "Get the current weather in a given location",
#     "input_schema": {
#         "type": "object",
#         "properties": {
#             "location": {"type": "string", "description": "City and state"},
#         },
#         "required": ["location"],
#     },
# }


# def execute_tool(name, tool_input):
#     """Execute a tool and return the result."""
#     return f"Weather in {tool_input.get('location', 'unknown')}: 72°F"


# response = client.messages.create(
#     model="claude-opus-5-5",
#     max_tokens=1024,
#     tools=[weather_tool],
#     messages=[{"role": "user", "content": "What is the weather in San Francisco?"}],
# )

# if response.stop_reason == "tool_use":
#     # Extract and execute the tool
#     for block in response.content:
#         if block.type == "tool_use":
#             result = execute_tool(block.name, block.input)
#             # Return result to Claude for final response

# response = client.messages.create(
#     model="claude-opus-5-5",
#     max_tokens=4096,
#     tools=[{"type": "web_search_20250305", "name": "web_search"}],
#     messages=[{"role": "user", "content": "Search for latest AI news"}],
# )

# if response.stop_reason == "pause_turn":
#     # Continue the conversation by sending the response back
#     messages = [
#         {"role": "user", "content": "Search for latest AI news"},
#         {"role": "assistant", "content": response.content},
#     ]
#     continuation = client.messages.create(
#         model="claude-opus-5-5",
#         max_tokens=4096,
#         messages=messages,
#         tools=[{"type": "web_search_20250305", "name": "web_search"}],
#     )

#     print(continuation)