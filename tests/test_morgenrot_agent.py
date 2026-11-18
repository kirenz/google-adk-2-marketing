from beispiele.morgenrot_agent.agent import root_agent
from beispiele.morgenrot_agent.tools import kennzahlen


def test_kennzahlen_suche():
    k = kennzahlen("Suchanzeigen")
    assert k["klickrate_prozent"] == 4.0
    assert k["klickpreis_eur"] == 0.6
    assert k["conversion_rate_prozent"] == 12.5
    assert k["kosten_je_reservierung_eur"] == 4.8


def test_kennzahlen_instagram():
    k = kennzahlen("instagram")
    assert k["klickrate_prozent"] == 0.8
    assert k["klickpreis_eur"] == 0.18
    assert k["conversion_rate_prozent"] == 4.25
    assert k["kosten_je_reservierung_eur"] == 4.24


def test_unbekannter_kanal():
    k = kennzahlen("TikTok")
    assert "fehler" in k
    assert k["kanaele"] == ["Suchanzeigen", "Instagram"]


def test_agent_hat_werkzeug():
    assert root_agent.name == "morgenrot_agent"
    assert kennzahlen in root_agent.tools


def test_workflow_bericht():
    import asyncio
    from beispiele.laufen import einmal
    from beispiele.morgenrot_workflow.agent import root_agent as workflow
    bericht = asyncio.run(einmal(workflow, "Bericht"))
    assert "| Instagram | 0,80 % | 0,18 € | 4,25 % | 4,24 € |" in bericht
    assert "Günstigster Kanal je Reservierung: Instagram" in bericht
