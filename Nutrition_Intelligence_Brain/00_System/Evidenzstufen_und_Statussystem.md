---
id: SYS-001
titel: Evidenzstufen und Statussystem
typ: regelwerk
erstellt: 2026-11-16
letzte_pruefung: 2026-11-16
---

# Evidenzstufen und Statussystem

Jede **konkrete gesundheitliche Aussage** erhält drei voneinander unabhängige Kennzeichnungen. Ein guter Evidenzstatus bedeutet **nicht**, dass eine Aussage werblich verwendet werden darf.

## 1. Wissenschaftlicher Evidenzstatus (A–D)

| Stufe | Bedeutung | Typische Grundlage | Sprache im Video |
|---|---|---|---|
| **A** | Gute, konsistente Human-Evidenz | Mehrere hochwertige RCTs / Metaanalysen mit konsistenten Ergebnissen; Leitlinien; oder gesichertes physiologisches Lehrbuchwissen (dann als „A (Physiologie)" kennzeichnen) | „gut belegt" |
| **B** | Begrenzte oder uneinheitliche Human-Evidenz | Wenige/kleine RCTs, hohe Heterogenität, nur Surrogat-/Biomarker-Endpunkte, widersprüchliche Metaanalysen, Industriefinanzierung ohne unabhängige Replikation | „erste Hinweise", „in Studien teilweise", „nicht eindeutig" |
| **C** | Überwiegend präklinische oder mechanistische Evidenz | Zellkultur, Tierversuch, Mechanismus-Hypothesen | „im Labor beobachtet – beim Menschen nicht gezeigt" |
| **D** | Nicht ausreichend belegt oder widersprochen | Keine/negative Humanstudien, Cochrane „insufficient evidence", Mythen | „nicht belegt" / „Mythos" |

**Zusatzmarker (optional, hinter der Stufe):**
- `[Assoz.]` – nur Beobachtungsdaten (Korrelation, keine Kausalität)
- `[Biomarker]` – Effekt nur auf Laborwert/Surrogat, nicht auf klinischen Endpunkt
- `[Supplement]` – gilt für isolierte Präparate/Extrakte, nicht für übliche Lebensmittelmengen
- `[COI]` – relevanter Interessenkonflikt in der Evidenzbasis
- `[Abstract]` – nur auf Abstract-/Sekundärebene geprüft, Volltext ausstehend

Pflicht für jede bewertete Aussage (siehe [[Vorlage_Forschungsakte]]): Studienart und -qualität · Population und n · Menge und Darreichungsform · Vergleich · Endpunkte · Effektgröße · Dauer · Limitationen · Interessenkonflikte · Sicherheit der Schlussfolgerung · Einordnung Korrelation/Kausalität, Biomarker/klinisch, Labor/Mensch.

## 2. Werberechtlicher Prüfstatus (W)

| Status | Bedeutung |
|---|---|
| **W0** | Nicht geprüft |
| **W1** | Nur als neutrale, nicht-kommerzielle Information geeignet – **keine** Verwendung in Werbung, Affiliate-Kontext oder Produktnähe |
| **W2** | Zugelassene gesundheitsbezogene Angabe nach VO (EU) 432/2012 existiert – nur im exakten zugelassenen Wortlaut und unter den Verwendungsbedingungen nutzbar (Registereintrag verlinken) |
| **W3** | In kommerzieller Kommunikation unzulässig (z. B. Krankheitsbezug, Botanical-Claim, nicht zugelassener Claim) |
| **W4** | Unklar – juristische Prüfung durch Fachanwalt erforderlich |

> [!caution] Claude vergibt W-Status nur als **Vorschlag** („W3 (Vorschlag)"). Verbindlich wird ein W-Status erst durch menschliche Prüfung, bei W2/W4 durch eine rechtskundige Person. Grundlage: [[Regelwerk_Recht_DE_EU]].

## 3. Redaktioneller Freigabestatus (R)

| Status | Bedeutung | Wer setzt ihn? |
|---|---|---|
| **R0** | Entwurf (KI-erstellt oder ungeprüft) | Claude / Autor |
| **R1** | Fachlich geprüft (Quellen im Volltext gelesen, Aussage korrekt wiedergegeben) | Mensch mit Fachkompetenz (z. B. Ökotrophologin, Ernährungswissenschaftler) |
| **R2** | Fachlich **und** rechtlich geprüft | Mensch; bei Werbebezug rechtskundige Person |
| **R3** | Zur Veröffentlichung freigegeben | Verantwortliche Person des Accounts |
| **RX** | Gesperrt (fehlerhaft, Risiko, zurückgezogen) | jede prüfende Person |

## 4. Quellen-Verifikationsstatus (V)

| Status | Bedeutung |
|---|---|
| **V0** | Volltext gelesen und Aussagen gegen Volltext geprüft |
| **V1** | Existenz + bibliografische Kennung (PMID/DOI/offizielle URL) über Suchindex bestätigt; Ergebnisse aus Abstract/Sekundärzusammenfassung |
| **V2** | Existenz bestätigt, aber einzelne Kennungen oder Zahlen **nicht** bestätigt |
| **V3** | Nicht verifiziert – darf nicht als Beleg verwendet werden |

Stand 16.11.2026: **keine Quelle hat V0.** Alle Akten sind daher höchstens R0.

## 5. Freigabe-Logik (Kurzform)

```
Aussage mit Evidenz D ............................ nur als „Mythos-Aufklärung" verwendbar
Aussage mit Evidenz C ............................ nur mit ausdrücklichem „nur Labor/Tier"-Hinweis
Aussage mit W3 ................................... niemals in Werbung/Affiliate-Nähe
Akte < R1 ........................................ kein Video-Briefing
Video < R2 ....................................... keine Veröffentlichung
```
