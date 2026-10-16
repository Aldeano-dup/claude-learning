# https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback

from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    fallbacks="default",
    betas=["server-side-fallback-2026-07-01"],
)
print(response.model)