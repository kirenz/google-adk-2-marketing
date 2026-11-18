"""Der erste Agent: ein Modell, eine Instruction, ein Werkzeug."""
import os

from dotenv import load_dotenv
from google.adk import Agent

from .tools import kennzahlen

load_dotenv()

root_agent = Agent(
    name="morgenrot_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
    description="Wertet die Werbekanäle der Rösterei Morgenrot aus.",
    instruction="""
Rolle: Du unterstützt die Gründerinnen der Rösterei Morgenrot (Kaffee-Abo, 27 Euro je Lieferung) bei der Auswertung ihrer Werbung.
Aufgabe: Beantworte Fragen zu den Kanälen Suchanzeigen und Instagram.
Regeln:
- Rechne nie selbst. Rufe für jede Kennzahl das Werkzeug kennzahlen auf.
- Nutze nur Zahlen aus der Rückgabe des Werkzeugs. Fehlt eine Zahl, sage das.
- Kennzeichne jede eigene Einschätzung mit „Annahme:“.
Ausgabe: höchstens fünf Sätze, danach eine Tabelle mit den Kennzahlen und die Quelle aus der Rückgabe.
""",
    tools=[kennzahlen],
)
