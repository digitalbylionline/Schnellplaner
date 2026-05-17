import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env", override=True)

from database import get_all_leads, init_db, ADMIN_PASSWORD

st.set_page_config(page_title="Admin – Schnellplaner", layout="wide")

init_db()

# ── Auth ──────────────────────────────────────────────────────────────────────
if "admin_ok" not in st.session_state:
    st.session_state.admin_ok = False

if not st.session_state.admin_ok:
    st.title("Admin-Bereich")
    pw = st.text_input("Passwort:", type="password")
    if st.button("Einloggen"):
        if pw == ADMIN_PASSWORD:
            st.session_state.admin_ok = True
            st.rerun()
        else:
            st.error("Falsches Passwort.")
    st.stop()

# ── Dashboard ─────────────────────────────────────────────────────────────────
st.title("5-Post-Schnellplaner · Leads")

leads = get_all_leads()

total = len(leads)
converted = sum(1 for l in leads if l["result_generated"])

col1, col2, col3 = st.columns(3)
col1.metric("Leads gesamt", total)
col2.metric("Plan erstellt", converted)
col3.metric("Conversion", f"{round(converted/total*100)}%" if total else "—")

st.divider()

if not leads:
    st.info("Noch keine Leads vorhanden.")
else:
    import pandas as pd

    df = pd.DataFrame(leads)
    df = df.rename(columns={
        "id": "ID",
        "email": "E-Mail",
        "situation": "Situation",
        "zielgruppe": "Zielgruppe",
        "startidee": "Startidee",
        "thema": "Thema",
        "ziel": "Ziel",
        "result_generated": "Plan erstellt",
        "created_at": "Datum",
    })
    df["Plan erstellt"] = df["Plan erstellt"].map({1: "✓", 0: "—"})
    df["Datum"] = pd.to_datetime(df["Datum"]).dt.strftime("%d.%m.%Y %H:%M")

    st.dataframe(
        df[["ID", "E-Mail", "Startidee", "Thema", "Ziel", "Plan erstellt", "Datum"]],
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Alle Details anzeigen"):
        st.dataframe(df, use_container_width=True, hide_index=True)

    # E-Mail-Liste kopieren
    st.subheader("E-Mail-Liste")
    emails = "\n".join(l["email"] for l in leads)
    st.text_area("Alle E-Mails:", value=emails, height=150)

if st.button("Ausloggen"):
    st.session_state.admin_ok = False
    st.rerun()
