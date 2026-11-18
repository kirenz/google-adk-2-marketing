"""Der erste Agent: ein Modell, eine Instruction mit Kontext, ein Werkzeug."""
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk import Agent

from .tools import kennzahlen

load_dotenv()

PROJEKT = Path(__file__).resolve().parents[2]


def lies(pfad: str) -> str:
    """Liest eine Textdatei aus dem Projektordner, z. B. kontext/unternehmen.md."""
    return (PROJEKT / pfad).read_text(encoding="utf-8")


root_agent = Agent(
    name="morgenrot_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    description="Wertet die Werbekanäle der Rösterei Morgenrot aus.",
    instruction=f"""
Rolle: Du unterstützt die Gründerinnen der Rösterei Morgenrot bei der Auswertung ihrer Werbung.
Aufgabe: Beantworte Fragen zu den Werbekanälen.
Werkzeug: Rechne nie selbst. Rufe für jede Kennzahl das Werkzeug kennzahlen auf.
Ausgabe: höchstens fünf Sätze, danach eine Tabelle mit den Kennzahlen und die Quelle aus der Rückgabe.

{lies("kontext/unternehmen.md")}
{lies("kontext/zielgruppe.md")}
{lies("AGENTS.md")}
""",
    tools=[kennzahlen],
)
