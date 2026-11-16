---
id: SYS-003
titel: Rechercheprotokoll 16.11.2026
typ: protokoll
erstellt: 2026-11-16
---

# Rechercheprotokoll – Phase 1 (16.11.2026)

## Technische Umgebung
- Recherche durch Claude (KI) in einer Cloud-Sitzung mit Claude Code.
- **Verfügbar:** Websuche (Suchindex mit Titeln, URLs und automatisch erzeugten Zusammenfassungen).
- **Nicht verfügbar:** direkter Seitenabruf. Anfragen an `pubmed.ncbi.nlm.nih.gov`, `eutils.ncbi.nlm.nih.gov` und weitere Fachseiten wurden von der Netzwerkrichtlinie blockiert. Eine Freischaltung der Hosts (PubMed, DGE, EFSA, BfR, EUR-Lex, Cochrane u. a.) wurde angefragt und **abgelehnt**.

## Konsequenzen
1. **Kein Volltext gelesen.** Zahlen stammen aus Abstracts bzw. Zusammenfassungen im Suchindex. Alle Quellen haben höchstens Verifikationsstatus **V1**.
2. **Erreichbarkeit der Links nicht technisch geprüft** (kein HTTP-Abruf möglich). Links sind die im Suchindex angezeigten URLs oder DOI-/PMID-basierte Standard-URLs.
3. EUR-Lex, gesetze-im-internet.de und das EU Health Claims Register konnten nicht direkt eingesehen werden; Rechtsstand stammt aus Gesetzesdatenbanken, Kanzlei- und Fachpressebeiträgen im Suchindex.

## Methode
- Für jede Kernquelle gezielte Suche nach Titel + Autor + Jahr + Kennung.
- Abgleich: Titel, Erstautor, Jahr, Zeitschrift, PMID, DOI. Abweichungen wurden dokumentiert.
- Priorität: Leitlinien/Behörden → Cochrane/Metaanalysen → RCTs → Mechanismus.
- Keine Quelle wurde erfunden. Kennungen, die nicht bestätigt werden konnten, sind **leer gelassen** und mit „nicht verifiziert" markiert.

## Während der Recherche korrigierte Fehler (Beispiele)
| Fehlerquelle | Korrektur |
|---|---|
| PMID aus Erinnerung für Ried 2016 (J Nutr) | Die PMID 26764327 gehört zu Varshney & Budoff 2016, nicht zu Ried. PMID für Ried 2016 bleibt leer. |
| PMID aus Erinnerung für Cavagnaro 2007 | Korrekt laut Suchindex: 17256959 |
| DILIN-Fallserie Kurkuma „JAMA Netw Open" | Tatsächlich: Am J Med 2023;136(2):200–206 |
| Wang et al. Kurkuma-Arthrose „2021" | Tatsächlich: Ann Intern Med 2020;173(11):861–869 |
| Ingwer-Metaanalyse CRP-Effekt | SMD −5,11 bei I² = 98 % – statistisch auffällig, nicht interpretierbar als Effektstärke |

## Suchstrings (Auswahl)
Siehe einzelne Quellennotizen im [[Quellenregister]] (Feld `verifikation_notiz`).
