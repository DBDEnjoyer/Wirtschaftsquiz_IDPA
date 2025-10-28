# Wirtschaftsquiz_IDPA


# Projekt-Dokumentation

**Bytyqi, Grigioni, Lai**

| Datum      | Version | Zusammenfassung |
| ---------- | ------- | ---------------- |
| 29.10.2025 | 0.0.1   | Projektidee und Anforderungen festgelegt |
| 29.10.2025 | 0.0.2   | Erste User Stories formuliert |
| 05.11.2025 | 0.1.0   | Testfälle erstellt und Planungsphase begonnen |
| 12.11.2025 | 0.2.0   | Grundstruktur und GUI-Entwurf erstellt |
| 26.11.2025 | 0.3.0   | Fragenverwaltung und Auswertung programmiert |
| 10.12.2025 | 0.8.0   | Fehlerbehebung, Tests und Feinschliff |
| 13.01.2026 | 1.0.0   | Projekt fertiggestellt und abgegeben |

---

## 1 Informieren

### 1.1 Ihr Projekt

Wir entwickeln ein **Wirtschaftsquiz**, mit dem Schülerinnen und Schüler ihr Wissen zur Wirtschaft testen und erweitern können.  
Das Programm enthält verschiedene Fragetypen (Multiple Choice, Richtig/Falsch, Freitext) und ermöglicht es Lehrpersonen, **eigene Fragen und Themenbereiche hinzuzufügen**.  
Ein Quiz kann erstellt, gespeichert und an Lernende weitergegeben werden. Nach Abschluss werden die **korrekten Lösungen** angezeigt.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ         | Beschreibung |
| ---- | --------------- | ----------- | ------------ |
| 1    | Muss            | Funktional  | Als Lernender möchte ich Fragen zu verschiedenen Wirtschaftsthemen beantworten können, um mein Wissen zu testen. |
| 2    | Muss            | Funktional  | Als Lernender möchte ich nach dem Beantworten die richtigen Antworten sehen, damit ich aus Fehlern lernen kann. |
| 3    | Muss            | Funktional  | Als Lehrperson möchte ich eigene Fragen und Themen hinzufügen können, damit das Quiz flexibel erweiterbar ist. |
| 4    | Muss            | Funktional  | Als Lehrperson möchte ich bestehende Fragen bearbeiten oder löschen können, damit der Fragenkatalog aktuell bleibt. |
| 5    | Kann            | Qualität    | Als Lehrperson möchte ich mehrere Quiz-Themen zusammenstellen können, damit ich gezielte Tests für Lernende vorbereiten kann. |
| 6    | Kann            | Funktional  | Als Lernender möchte ich mein Ergebnis am Ende sehen, um meinen Lernfortschritt zu erkennen. |

### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  | Programmstart | Start-Button | Hauptmenü mit Auswahl „Quiz starten“ oder „Fragen bearbeiten“ wird angezeigt |
| 2.1  | Lernender startet ein Quiz | Auswahl eines Themas | Fragen werden nacheinander angezeigt |
| 2.2  | Lernender beantwortet alle Fragen | Klick auf „Auswerten“ | Anzeige der richtigen und falschen Antworten |
| 3.1  | Lehrperson öffnet Bearbeitungsmodus | Klick auf „Neue Frage hinzufügen“ | Formular zur Eingabe einer neuen Frage erscheint |
| 3.2  | Lehrperson gibt fehlerhafte Eingabe ein (z. B. leere Felder) | Speichern | Fehlermeldung „Bitte alle Felder ausfüllen“ |
| 4.1  | Lehrperson wählt „Frage löschen“ | Klick auf Bestätigen | Frage wird aus der Datenbank entfernt |
| 5.1  | Lernender schließt das Quiz ab | Klick auf „Beenden“ | Ergebnis mit Punktzahl und Korrekturen wird angezeigt |

---

## 2 Planen

| AP-№ | Frist      | Zuständig | Beschreibung | geplante Zeit |
| ---- | ---------- | --------- | ------------ | ------------- |
| 1.A  | 29.10.2025 | Team      | Projektidee festlegen, Anforderungen verstehen | 45’ |
| 1.B  | 29.10.2025 | Team      | User Stories und Testfälle formulieren | 60’ |
| 2.A  | 05.11.2025 | Grigioni  | Grundstruktur des Quiz-Programms (Klassen, Module) erstellen | 90’ |
| 2.B  | 05.11.2025 | Bytyqi    | Datenspeicherung für Fragen & Themen (z. B. JSON oder CSV) umsetzen | 90’ |
| 2.C  | 05.11.2025 | Lai       | GUI-Design für Quiz-Startseite und Fragenanzeige entwerfen | 90’ |
| 3.A  | 12.11.2025 | Grigioni  | Logik für Beantwortung & Auswertung implementieren | 90’ |
| 3.B  | 12.11.2025 | Bytyqi    | Funktion zum Hinzufügen, Bearbeiten und Löschen von Fragen implementieren | 90’ |
| 3.C  | 12.11.2025 | Lai       | Anzeige der korrekten Lösungen nach Abschluss umsetzen | 90’ |
| 4.A  | 26.11.2025 | Team      | Testphase: Fehler beheben und UI verbessern | 120’ |
| 5.A  | 10.12.2025 | Team      | Dokumentation erweitern und Feedback umsetzen | 90’ |
| 6.A  | 13.01.2026 | Team      | Abschluss, finale Doku & Abgabe | 60’ |

**Total:** ca. 12 Arbeitspakete ≈ 18 Stunden

---

