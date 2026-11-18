"""Startet einen Agenten oder Workflow einmal im Terminal: uv run python -m beispiele.laufen"""
import asyncio
import sys
from uuid import uuid4

from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


async def einmal(agent, text: str) -> str:
    sessions = InMemorySessionService()
    ids = {"user_id": uuid4().hex, "session_id": uuid4().hex}
    await sessions.create_session(app_name="beispiele", **ids)
    runner = Runner(agent=agent, app_name="beispiele", session_service=sessions)
    antworten = []
    async for event in runner.run_async(**ids, new_message=types.Content(role="user", parts=[types.Part(text=text)])):
        if event.content and event.is_final_response():
            t = "".join(p.text or "" for p in event.content.parts or [])
            if t:
                antworten.append(t)
    return "\n".join(antworten)


if __name__ == "__main__":
    from beispiele.morgenrot_workflow.agent import root_agent
    print(asyncio.run(einmal(root_agent, " ".join(sys.argv[1:]) or "Bericht")))
