from dotenv import load_dotenv
import asyncio
import livekit.agents as agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google

# Load environment variables (ensure LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET are set)
load_dotenv()

# Import instructions and response from prompt.py
from prompt import AGENT_INSTRUCTION, AGENT_RESPONSE


class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions=AGENT_INSTRUCTION)


async def entrypoint(ctx: agents.JobContext):
    # Create session with Gemini voice model
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",
            temperature=0.8,
            instructions=AGENT_INSTRUCTION,
        ),
    )

    # Start agent in the room
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions()
    )

    # Send a greeting once the agent is ready
    await session.generate_reply(instructions=AGENT_RESPONSE)

    # Keep the agent running so IPC doesn't close
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
