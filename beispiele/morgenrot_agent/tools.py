"""Werkzeuge des Morgenrot-Agenten: einfache Python-Funktionen."""
import csv
from pathlib import Path

DATEN = Path(__file__).resolve().parents[2] / "daten" / "kampagne.csv"


def kennzahlen(kanal: str) -> dict:
    """Berechnet die Kennzahlen eines Werbekanals aus daten/kampagne.csv.

    Args:
        kanal: Name des Kanals, genau wie in der Spalte kanal, z. B. "Suchanzeigen" oder "Instagram".

    Returns:
        Ein Dictionary mit Klickrate (CTR) und Conversion-Rate in Prozent, Klickpreis (CPC)
        und Kosten je Reservierung in Euro. Ist der Kanal unbekannt, enthält es den Schlüssel
        "fehler" und die Liste der vorhandenen Kanäle.
    """
    with DATEN.open(encoding="utf-8") as datei:
        zeilen = list(csv.DictReader(datei))
    for zeile in zeilen:
        if zeile["kanal"].lower() == kanal.strip().lower():
            kosten = float(zeile["kosten_eur"])
            impressionen = int(zeile["impressionen"])
            klicks = int(zeile["klicks"])
            reservierungen = int(zeile["reservierungen"])
            return {
                "kanal": zeile["kanal"],
                "klickrate_prozent": round(klicks / impressionen * 100, 2),
                "klickpreis_eur": round(kosten / klicks, 2),
                "conversion_rate_prozent": round(reservierungen / klicks * 100, 2),
                "kosten_je_reservierung_eur": round(kosten / reservierungen, 2),
                "quelle": "daten/kampagne.csv",
            }
    return {"fehler": f"Kanal {kanal!r} nicht gefunden.", "kanaele": [z["kanal"] for z in zeilen]}
