import streamlit as st
import os
import html as _html
from pathlib import Path
from dotenv import load_dotenv
from database import init_db, save_lead, mark_result_generated
from generator import generate_plan


def e(text) -> str:
    return _html.escape(str(text))

load_dotenv(Path(__file__).parent / ".env", override=True)

SPARK_URL = os.getenv("SPARK_URL", "https://www.digitalbylionline.com")

st.set_page_config(
    page_title="5-Post-Schnellplaner für Mamas",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

init_db()

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Fonts & base */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500&family=Great+Vibes&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; padding-bottom: 4rem; max-width: 720px;}

/* Headlines */
h1 { font-family: 'Playfair Display', serif !important; color: #1C1C1C !important; }
h2 { font-family: 'Playfair Display', serif !important; color: #1C1C1C !important; font-size: 1.4rem !important; }
h3 { font-family: 'Inter', sans-serif !important; font-weight: 500 !important; color: #1C1C1C !important; font-size: 1rem !important; }

/* Tool-Header */
.tool-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.tool-header h1 {
    font-size: 2rem;
    margin-bottom: 0.4rem;
    color: #1C1C1C;
}
.tool-header p {
    color: #5C5C5C;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.6;
    max-width: 520px;
    margin: 0 auto;
}
.pink-line {
    width: 48px;
    height: 3px;
    background: #B5607A;
    margin: 1.2rem auto 0;
    border-radius: 2px;
}

/* Section label */
.section-label {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #B5607A;
    margin-bottom: 0.8rem;
    margin-top: 2rem;
}

/* Divider */
.soft-divider {
    border: none;
    border-top: 1px solid #E8E0D6;
    margin: 2rem 0;
}

/* Email gate box */
.email-box {
    background: #F5EDE5;
    border-left: 3px solid #B5607A;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin: 1.5rem 0;
}
.email-box p {
    margin: 0;
    font-size: 0.92rem;
    color: #3C3C3C;
    line-height: 1.5;
}

/* Post result card */
.post-card {
    background: #FFFFFF;
    border: 1px solid #E8E0D6;
    border-radius: 12px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.post-card-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1rem;
}
.post-number {
    background: #B5607A;
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.post-type-badge {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #B5607A;
    background: #F5EDE5;
    padding: 2px 8px;
    border-radius: 20px;
}
.post-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    font-weight: 600;
    color: #1C1C1C;
    margin-bottom: 1rem;
}
.post-field-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 3px;
}
.post-field-value {
    font-size: 0.93rem;
    color: #2C2C2C;
    line-height: 1.55;
    margin-bottom: 0.9rem;
}
.hook-text {
    font-style: italic;
    color: #1C1C1C;
    font-size: 0.96rem;
    line-height: 1.6;
    border-left: 2px solid #B5607A;
    padding-left: 0.8rem;
    margin-bottom: 0.9rem;
}
.cta-text {
    background: #FAF6EF;
    border: 1px solid #E8E0D6;
    border-radius: 6px;
    padding: 0.5rem 0.8rem;
    font-size: 0.88rem;
    color: #3C3C3C;
    margin-top: 0.2rem;
}

/* Pitch section */
.pitch-section {
    background: linear-gradient(145deg, #1a0a10 0%, #2a1018 50%, #1C1C1C 100%);
    border: 1px solid #4a1a28;
    border-top: 3px solid #C01E5C;
    border-radius: 16px;
    padding: 2.5rem 2rem 2rem;
    margin-top: 0.5rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(176, 30, 92, 0.12);
}
.pitch-tag {
    display: inline-block;
    background: rgba(192, 30, 92, 0.2);
    border: 1px solid rgba(192, 30, 92, 0.4);
    color: #e06090;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 1rem;
}
.spark-name {
    font-family: 'Great Vibes', cursive;
    color: #C01E5C;
    font-size: 2.2rem;
    display: block;
    line-height: 1.1;
    margin: 0.3rem 0 0.8rem;
}
.pitch-section h2 {
    color: #FAF6EF !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.4rem !important;
    margin-bottom: 0.4rem !important;
    line-height: 1.3 !important;
}
.pitch-section p {
    color: #C8C0B8;
    font-size: 0.91rem;
    line-height: 1.7;
    max-width: 460px;
    margin: 0 auto 1.6rem;
}
.pitch-divider {
    width: 40px;
    height: 2px;
    background: #C01E5C;
    margin: 1rem auto;
    border-radius: 2px;
    opacity: 0.6;
}

/* Buttons */
.stButton > button {
    background: #B5607A !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 1.8rem !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.2s ease !important;
    width: 100%;
}
.stButton > button:hover {
    opacity: 0.88 !important;
}

/* Input fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #FFFFFF !important;
    border: 1px solid #DDD6CC !important;
    border-radius: 8px !important;
    color: #1C1C1C !important;
    font-size: 0.93rem !important;
}
.stSelectbox > div > div {
    background: #FFFFFF !important;
    border: 1px solid #DDD6CC !important;
    border-radius: 8px !important;
}

/* Success message */
.success-banner {
    background: #EDF7EE;
    border: 1px solid #C3E0C5;
    border-radius: 8px;
    padding: 0.8rem 1.2rem;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
    color: #2D6A30;
}

/* Result headline */
.result-headline {
    text-align: center;
    margin: 1rem 0 0.5rem;
}
.result-headline h2 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.6rem !important;
    color: #1C1C1C !important;
}
.result-headline p {
    color: #5C5C5C;
    font-size: 0.93rem;
    margin-top: 0.3rem;
}
</style>
""", unsafe_allow_html=True)


# ── State ─────────────────────────────────────────────────────────────────────
if "view" not in st.session_state:
    st.session_state.view = "form"   # "form" | "result"
if "posts" not in st.session_state:
    st.session_state.posts = []
if "form_inputs" not in st.session_state:
    st.session_state.form_inputs = {}
if "email_saved" not in st.session_state:
    st.session_state.email_saved = False


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="tool-header">
    <h1>Dein 5-Post-Schnellplaner</h1>
    <p>Erstelle in wenigen Minuten deine ersten 5 Instagram-Posts —<br>
    passend zu deinem Mama-Alltag, deiner Startidee und deinem Ziel.</p>
    <div class="pink-line"></div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FORMULAR-ANSICHT
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.view == "form":

    st.markdown('<p class="section-label">Schritt 1 — Deine Situation</p>', unsafe_allow_html=True)
    situation = st.text_area(
        "Beschreibe kurz deinen Alltag:",
        placeholder='z. B. „Ich bin Mama, arbeite Vollzeit und will mir online etwas Eigenes aufbauen."',
        height=90,
        label_visibility="collapsed"
    )

    st.markdown('<p class="section-label">Schritt 2 — Deine Zielgruppe</p>', unsafe_allow_html=True)
    zielgruppe = st.text_area(
        "Wen möchtest du mit deinem Content erreichen?",
        placeholder='z. B. „Andere berufstätige Mamas, die online starten wollen."',
        height=90,
        label_visibility="collapsed"
    )

    st.markdown('<p class="section-label">Schritt 3 — Deine Startidee</p>', unsafe_allow_html=True)
    startidee = st.selectbox(
        "Womit möchtest du online starten?",
        options=[
            "Bitte wählen …",
            "Affiliate-Marketing",
            "Digitales Miniprodukt",
            "KI-Tool",
            "Instagram-Aufbau",
            "Ich weiß es noch nicht genau",
        ],
        label_visibility="collapsed"
    )

    st.markdown('<p class="section-label">Schritt 4 — Dein Thema</p>', unsafe_allow_html=True)
    thema = st.text_input(
        "Worüber möchtest du posten?",
        placeholder='z. B. „Online-Business starten als Mama"',
        label_visibility="collapsed"
    )

    st.markdown('<p class="section-label">Schritt 5 — Dein Ziel</p>', unsafe_allow_html=True)
    ziel = st.selectbox(
        "Was soll dein Content aktuell erreichen?",
        options=[
            "Bitte wählen …",
            "Sichtbar werden",
            "Vertrauen aufbauen",
            "E-Mail-Liste aufbauen",
            "Mein Miniprodukt verkaufen",
            "Affiliate-Kurs bewerben",
            "Erste Nachrichten bekommen",
        ],
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    if st.button("Meinen 5-Post-Plan erstellen"):
        errors = []
        if not situation.strip():
            errors.append("Deine Situation fehlt noch.")
        if not zielgruppe.strip():
            errors.append("Deine Zielgruppe fehlt noch.")
        if startidee == "Bitte wählen …":
            errors.append("Bitte wähle deine Startidee aus.")
        if not thema.strip():
            errors.append("Dein Thema fehlt noch.")
        if ziel == "Bitte wählen …":
            errors.append("Bitte wähle dein Ziel aus.")

        if errors:
            for err in errors:
                st.error(err)
        else:
            with st.spinner("Dein Plan wird erstellt … Das dauert einen Moment."):
                try:
                    posts = generate_plan(situation, zielgruppe, startidee, thema, ziel)
                    st.session_state.posts = posts
                    st.session_state.form_inputs = {
                        "situation": situation,
                        "zielgruppe": zielgruppe,
                        "startidee": startidee,
                        "thema": thema,
                        "ziel": ziel,
                    }
                    st.session_state.email_saved = False
                    st.session_state.view = "result"
                    st.rerun()
                except Exception as ex:
                    st.error(f"Etwas ist schiefgelaufen: {ex}")


# ══════════════════════════════════════════════════════════════════════════════
# ERGEBNIS-ANSICHT
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.view == "result":

    st.markdown('<div class="result-headline"><h2>Hier sind deine ersten 5 Instagram-Posts</h2><p>Starte mit dieser Reihenfolge: Story · Problem · Wunsch · Lösung · CTA</p></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── E-Mail-Block OBEN ─────────────────────────────────────────────────────
    def render_email_block(key: str):
        if not st.session_state.email_saved:
            st.markdown(
                '<div style="background:#B5607A;border-radius:12px;padding:1.4rem 1.6rem;margin:1.2rem 0;">'
                '<p style="color:#fff;font-size:1rem;font-weight:600;margin:0 0 0.3rem;">Sicher dir deinen Plan — bevor du ihn verlierst.</p>'
                '<p style="color:#f0d8e0;font-size:0.87rem;margin:0 0 1rem;">Ich schicke dir die 5 Posts direkt per Mail. Kostenlos, kein Spam.</p>'
                '</div>',
                unsafe_allow_html=True
            )
            email_val = st.text_input(
                "E-Mail:",
                placeholder="deine@email.de",
                label_visibility="collapsed",
                key=key
            )
            if st.button("Plan per Mail sichern", key=f"btn_{key}"):
                if not email_val.strip() or "@" not in email_val:
                    st.error("Bitte gib eine gültige E-Mail-Adresse ein.")
                else:
                    fi = st.session_state.form_inputs
                    lead_id = save_lead(
                        email_val,
                        fi.get("situation", ""),
                        fi.get("zielgruppe", ""),
                        fi.get("startidee", ""),
                        fi.get("thema", ""),
                        fi.get("ziel", ""),
                    )
                    mark_result_generated(lead_id)
                    st.session_state.email_saved = True
                    st.rerun()
        else:
            st.markdown(
                '<div style="background:#EDF7EE;border:1px solid #C3E0C5;border-radius:8px;padding:0.8rem 1.2rem;font-size:0.9rem;color:#2D6A30;margin:1rem 0;">✓ &nbsp;Gespeichert! Du bekommst deinen Plan in Kürze.</div>',
                unsafe_allow_html=True
            )

    render_email_block("email_top")

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── Post-Karten ───────────────────────────────────────────────────────────
    for post in st.session_state.posts:
        nr = e(post.get('nummer', ''))
        typ = e(post.get('typ', ''))
        titel = e(post.get('titel', ''))
        hook = e(post.get('hook', ''))
        thema_post = e(post.get('thema', ''))
        struktur = e(post.get('struktur', ''))
        cta = e(post.get('cta', ''))
        card = (
            f'<div class="post-card">'
            f'<div class="post-card-header">'
            f'<div class="post-number">{nr}</div>'
            f'<span class="post-type-badge">{typ}</span>'
            f'</div>'
            f'<div class="post-title">{titel}</div>'
            f'<div class="post-field-label">Hook</div>'
            f'<div class="hook-text">{hook}</div>'
            f'<div class="post-field-label">Thema des Posts</div>'
            f'<div class="post-field-value">{thema_post}</div>'
            f'<div class="post-field-label">Post-Struktur</div>'
            f'<div class="post-field-value">{struktur}</div>'
            f'<div class="post-field-label">Call to Action</div>'
            f'<div class="cta-text">{cta}</div>'
            f'</div>'
        )
        st.markdown(card, unsafe_allow_html=True)

    st.markdown('<p style="text-align:center; color:#666; font-size:0.88rem; margin-top:0.5rem;">Diese 5 Posts sind dein Startpunkt. Fang einfach an.</p>', unsafe_allow_html=True)

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── E-Mail-Block UNTEN ────────────────────────────────────────────────────
    render_email_block("email_bottom")

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── Pitch ─────────────────────────────────────────────────────────────────
    pitch_html = (
        f'<div class="pitch-section">'
        f'<div class="pitch-tag">Dein nächster Schritt</div>'
        f'<h2>Du hast deinen Start.</h2>'
        f'<h2>Jetzt brauchst du ein System.</h2>'
        f'<div class="pitch-divider"></div>'
        f'<span class="spark-name">Spark</span>'
        f'<p>Mein Hook- &amp; Content-Generator erstellt dir regelmäßig passende Hooks, Themen und Captions — damit du nicht jede Woche wieder vor einer leeren Seite sitzt.<br><br>'
        f'Du gibst dein Thema, deine Zielgruppe oder eigenes Fachwissen ein und bekommst fertige Post-Ideen für deinen Online-Start.</p>'
        f'<a href="{SPARK_URL}" target="_blank" style="display:inline-block;background:linear-gradient(135deg,#C01E5C,#a0184d);color:white;text-decoration:none;padding:0.85rem 2.2rem;border-radius:10px;font-size:0.97rem;font-weight:600;letter-spacing:0.03em;box-shadow:0 4px 16px rgba(192,30,92,0.35);">Zum Hook- &amp; Content-Generator →</a>'
        f'</div>'
    )
    st.markdown(pitch_html, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    if st.button("← Neuen Plan erstellen"):
        st.session_state.view = "form"
        st.session_state.posts = []
        st.session_state.email_saved = False
        st.rerun()
