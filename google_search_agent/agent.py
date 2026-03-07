import os

from google.adk.agents import Agent
from google.adk.tools import google_search


def call_phone(number: str, msg: str) -> dict:
    print(f"calling {number} with {msg}")
    return {"status": "success", "reply": "thank you we will pick up our son, let him know we will be there in about 15 minutes"}


def call_grab_car(pickup_address: str, destination_address) -> dict:
    """calls grab car for pickup at pickup_address for destination: destination_address. Returns status and pickup location."""
    print(
        f"calling grab car for pickup at {pickup_address} for destination: {destination_address}"
    )
    return {"status": "success", "pickup": "level 2 private hire pickup point"}


# Default models for Live API with native audio support:
# - Gemini Live API: gemini-2.5-flash-native-audio-preview-12-2025
# - Vertex AI Live API: gemini-live-2.5-flash-native-audio
agent = Agent(
    name="google_search_agent",
    model=os.getenv(
        "DEMO_AGENT_MODEL", "gemini-2.5-flash-native-audio-preview-12-2025"
    ),
    tools=[google_search, call_grab_car, call_phone],
    instruction="You are a helpful assistant that can search the web, turn on or off lights, can call a grab car. Respond with the tone a good friend.",
)
