import json
import anthropic
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Du bist ein Instagram-Contentplaner für berufstätige Mamas, die online starten wollen und wenig Zeit haben.

Regeln:
- Einfache Alltagssprache, keine Guru-Sprache
- Berufstätige Mamas direkt und warmherzig ansprechen
- Keine übertriebenen Einkommensversprechen
- Keine Aussagen wie "passives Einkommen über Nacht"
- Kein langer Strategietext
- Jeder Post soll auch mit wenig Instagram-Erfahrung umsetzbar sein
- CTAs passend zum angegebenen Ziel formulieren"""


def generate_plan(situation: str, zielgruppe: str, startidee: str,
                  thema: str, ziel: str) -> list[dict]:

    user_prompt = f"""Erstelle auf Basis dieser Eingaben einen 5-Post-Plan für Instagram.

Situation der Nutzerin: {situation}
Zielgruppe: {zielgruppe}
Startidee: {startidee}
Thema: {thema}
Ziel des Contents: {ziel}

Erstelle genau 5 Posts in dieser Reihenfolge:
1. Story-Post — Verbindung aufbauen (zeigt warum sie online startet)
2. Problem-Post — Wiedererkennung erzeugen (spricht das Problem der Zielgruppe aus)
3. Wunsch-Post — Sehnsucht sichtbar machen (zeigt was digitales Einkommen verändern soll)
4. Lösungs-Post — erste Orientierung geben (erklärt einen einfachen ersten Schritt)
5. CTA-Post — Handlung auslösen (lädt zur nächsten Aktion ein)

Antworte NUR mit einem gültigen JSON-Objekt, ohne Markdown-Code-Blöcke, ohne Erklärungen davor oder danach:

{{"posts": [
  {{
    "nummer": 1,
    "typ": "Story-Post",
    "titel": "Dein Warum",
    "hook": "...",
    "thema": "...",
    "struktur": "...",
    "cta": "..."
  }},
  {{
    "nummer": 2,
    "typ": "Problem-Post",
    "titel": "Das Problem",
    "hook": "...",
    "thema": "...",
    "struktur": "...",
    "cta": "..."
  }},
  {{
    "nummer": 3,
    "typ": "Wunsch-Post",
    "titel": "Der Wunsch",
    "hook": "...",
    "thema": "...",
    "struktur": "...",
    "cta": "..."
  }},
  {{
    "nummer": 4,
    "typ": "Lösungs-Post",
    "titel": "Der erste Schritt",
    "hook": "...",
    "thema": "...",
    "struktur": "...",
    "cta": "..."
  }},
  {{
    "nummer": 5,
    "typ": "CTA-Post",
    "titel": "Deine Einladung",
    "hook": "...",
    "thema": "...",
    "struktur": "...",
    "cta": "..."
  }}
]}}

hook: 1-2 Sätze, starker Einstieg der sofort Aufmerksamkeit zieht
thema: 1 kurzer Satz was der Post behandelt
struktur: 2-3 Sätze wie der Post aufgebaut sein soll
cta: 1 konkreter Call to Action passend zum Ziel "{ziel}"
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    raw = message.content[0].text.strip()

    # Strip markdown code blocks if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    data = json.loads(raw)
    return data["posts"]
