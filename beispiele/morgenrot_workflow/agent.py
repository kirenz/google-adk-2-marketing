"""Ein Workflow aus festen Schritten: kein Modell, kein API-Schlüssel."""
import csv
from pathlib import Path

from google.adk import Event, Workflow
from google.adk.workflow import START

from beispiele.morgenrot_agent.tools import kennzahlen

DATEN = Path(__file__).resolve().parents[2] / "daten" / "kampagne.csv"


def laden(node_input: str) -> list[dict]:
    """Liest alle Zeilen aus daten/kampagne.csv. Die Eingabe wird nicht gebraucht."""
    with DATEN.open(encoding="utf-8") as datei:
        return list(csv.DictReader(datei))


def rechnen(node_input: list[dict]) -> list[dict]:
    """Ruft für jeden Kanal dasselbe Werkzeug auf, das auch der Agent aus Kapitel 1 nutzt."""
    return [kennzahlen(zeile["kanal"]) for zeile in node_input]


def zahl(wert: float) -> str:
    """Schreibt eine Zahl mit zwei Nachkommastellen und Dezimalkomma."""
    return f"{wert:.2f}".replace(".", ",")


def berichten(node_input: list[dict]):
    """Schreibt eine Tabelle und nennt den Kanal mit den niedrigsten Kosten je Reservierung."""
    zeilen = ["| Kanal | CTR | CPC | CR | Kosten je Reservierung |", "|---|---:|---:|---:|---:|"]
    for k in node_input:
        zeilen.append(
            f"| {k['kanal']} | {zahl(k['klickrate_prozent'])} % | {zahl(k['klickpreis_eur'])} € "
            f"| {zahl(k['conversion_rate_prozent'])} % | {zahl(k['kosten_je_reservierung_eur'])} € |"
        )
    guenstigster = min(node_input, key=lambda k: k["kosten_je_reservierung_eur"])
    zeilen.append("")
    zeilen.append(f"Günstigster Kanal je Reservierung: {guenstigster['kanal']}. Quelle: daten/kampagne.csv")
    yield Event(message="\n".join(zeilen))
    yield Event(output=node_input)


root_agent = Workflow(name="morgenrot_workflow", edges=[(START, laden, rechnen, berichten)])
