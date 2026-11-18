# Google ADK 2 im Marketing

Deutsches Quarto-Buch mit lauffähigen Beispielen zu Google ADK 2 (google-adk 2.13.0, Python 3.13). Durchgehender Fall ist die erfundene Rösterei Morgenrot.

[Das Buch lesen](https://kirenz.github.io/google-adk-2-marketing/)

## Lokal starten

```bash
uv sync
cp .env.example .env      # eigenen Gemini-Schlüssel eintragen
uv run pytest             # prüft die Werkzeuge ohne Schlüssel
uv run adk web beispiele  # startet die Oberfläche
```

## Buch bauen

`quarto preview` zeigt das Buch unter `http://localhost:4203`. Beim Push auf `main` veröffentlicht die GitHub Action das Buch auf dem Branch `gh-pages`. Die Python-Beispiele werden beim Rendern nicht ausgeführt.

## Aufbau

- `kapitel/`: ein Kapitel je Datei
- `beispiele/`: je Kapitel ein Agentenordner mit `agent.py` und `tools.py`
- `daten/`: erfundene Daten des Falls
- `tests/`: prüft die Werkzeuge, läuft in der Action „Beispiele testen“
