---
id: SYS-002
titel: Konventionen und Arbeitsablauf
typ: regelwerk
erstellt: 2026-11-16
letzte_pruefung: 2026-11-16
---

# Konventionen und Arbeitsablauf

## IDs und Dateinamen

| Präfix | Bereich | Beispiel |
|---|---|---|
| `BIO-` | Körper/Biologie (`01_`) | `BIO-001_Entzuendung_akut_und_chronisch` |
| `LM-` | Lebensmittel (`02_`) | `LM-003_Kurkuma` |
| `NS-` | Nährstoffe (`03_`) | `NS-002_Magnesium` |
| `EM-` | Ernährungsmuster (`04_`) | `EM-001_Mediterrane_Ernaehrung` |
| `Q-<BEREICH>-NN` | Quelle (`09_`) | `Q-KUR-04` |
| Aussage-ID | innerhalb einer Akte | `A-KUR-03` |
| `VID-` | Video-Briefing (`07_`) | `VID-0001_Kurkuma_Bioverfuegbarkeit` |
| `QB-` | Qualitätsbericht | `QB-2026-11-16_Qualitaetsbericht_Phase1` |

- Dateinamen ohne Umlaute und Leerzeichen (`ae`, `oe`, `ue`, `ss`), damit Wikilinks robust bleiben.
- Datumsformat immer `JJJJ-MM-TT`.

## Wikilinks
- Quellen werden in Akten **immer** als `[[Q-…]]` verlinkt, nicht als Freitext.
- Akten verlinken verwandte Akten im Feld `verknuepft` (YAML) und im Abschnitt „Verknüpfte Wissensdateien".
- Nicht existierende Ziele sind nur erlaubt, wenn sie im [[Recherche_Backlog]] stehen.

## Tags (YAML `tags`)
`#akte`, `#quelle`, `#vorlage`, `#regelwerk`, `#stub`, `#botanical`, `#naehrstoff`, `#risiko-schwangerschaft`, `#risiko-medikamente`, `#mythos`

## Arbeitsablauf je Thema
1. Thema aus [[Recherche_Backlog]] auswählen.
2. Akte aus [[Vorlage_Forschungsakte]] anlegen, Status R0.
3. Quellen recherchieren (Priorität: Leitlinien/Behörden → Cochrane/systematische Reviews/Metaanalysen → große RCTs → Kohorten → Mechanismus). Jede Quelle als Notiz aus [[Vorlage_Quelle]] anlegen.
4. Aussagen einzeln bewerten (A–D, W-Vorschlag, R0).
5. Qualitätskontrolle (Checkliste unten), Bericht in `00_System/Qualitaetsberichte/`.
6. Menschliche Fachprüfung → R1; danach erst Video-Briefings.

## QS-Checkliste je Akte
- [ ] Jede Aussage hat ≥ 1 verlinkte Quelle mit V ≤ 2
- [ ] Keine Quelle mit V3 als Beleg
- [ ] Zahlen (n, Dosis, Effekt, Dauer) stimmen mit Quelle überein
- [ ] Korrelation vs. Kausalität, Biomarker vs. klinisch, Labor vs. Mensch ausgewiesen
- [ ] Widersprechende Studien genannt
- [ ] Risiken, Wechselwirkungen, Risikogruppen vollständig
- [ ] Interessenkonflikte geprüft
- [ ] Keine Werbesprache, keine Heilversprechen
- [ ] W-Status nur als Vorschlag
- [ ] Alle Wikilinks auflösbar
