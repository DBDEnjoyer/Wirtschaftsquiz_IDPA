# Wirtschaftsquiz_IDPA


# Projekt-Dokumentation

**Bytyqi, Grigioni, Lai**

| Datum      | Version | Zusammenfassung |
| ---------- | ------- | ---------------- |
| 29.10.2025 | 0.0.1   | Projektidee und Anforderungen festgelegt |
| 29.10.2025 | 0.0.2   | Erste User Stories formuliert |
| 05.11.2025 | 0.1.0   | Planen, Diagramme und Codegrundlagen  |
| 12.11.2025 | 0.2.0   |Implementierung der Logik, Frageverwaltung und Lösungsausgabe abgeschlossen |
| 19.11.2025 | 0.3.0   |Implementierung der GUI Testen und respektives BUGfixen|
| 26.11.2025 | 0.4.0   |Testen und respektives BUGfixen|
| 2.12.2025 | 0.9.0   |Testphase abgeschlossen, Präsentation gestartet und Dokumentation überarbeitet|






---

## 1 Informieren

### 1.1 Ihr Projekt

Wir entwickeln ein **Wirtschaftsquiz**, mit dem Schülerinnen und Schüler ihr Wissen zur Wirtschaft testen und erweitern können.  
Das Programm enthält verschiedene Fragetypen (Multiple Choice, Richtig/Falsch, Freitext) und ermöglicht es Lehrpersonen, **eigene Fragen und Themenbereiche hinzuzufügen**.  
Ein Quiz kann erstellt, gespeichert und an Lernende weitergegeben werden. Nach Abschluss werden die **korrekten Lösungen** angezeigt.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Rolle | Beschreibung |
|------|----------------|-------|---------------|
| 1 | Muss | **Lernende** | Als Lernende*r möchte ich ein Quiz zu einem ausgewählten Wirtschaftsthema starten können, damit ich meinen Wissensstand überprüfen kann. |
| 2 | Muss | **Lernende** | Als Lernende*r möchte ich nach jeder Abgabe sehen, ob meine Antwort richtig oder falsch war, damit ich aus Fehlern lernen kann. |
| 3 | Muss | **Lehrperson** | Als Lehrperson möchte ich neue Fragen mit Thema, Fragetyp und Lösung erfassen können, damit ich den Fragenkatalog erweitern kann. |
| 4 | Muss | **Lehrperson** | Als Lehrperson möchte ich bestehende Fragen bearbeiten oder löschen können, damit fehlerhafte oder veraltete Inhalte korrigiert werden können. |
| 5 | Muss | **Lehrperson** | Als Lehrperson möchte ich aus mehreren Themen ein Quiz zusammenstellen und exportieren können, damit ich es an Lernende weitergeben kann. |
| 6 | Kann | **Lernende** | Als Lernende*r möchte ich ein von der Lehrperson erhaltenes Quiz laden können, damit ich genau dieses Quiz bearbeiten kann. |
| 7 | Kann | **Lernende** | Als Lernende*r möchte ich am Ende eine Übersicht meiner Antworten und der korrekten Lösungen sehen, damit ich gezielt nachlernen kann. |


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

### Testkonzept

**Testumgebung**
- Getestet auf Windows-PC mit Python 3.x
- Einzelplatzbetrieb (kein Netzwerk, kein Server)

**Testmethode**
- Manuelle Tests anhand definierter Testfälle
- Exploratives Testen bei der GUI-Bedienung

**Nicht getestet**
- Keine Tests auf mobilen Geräten
- Keine Mehrbenutzer-Szenarien
- Keine Performance- oder Netzwerktests

### Bewertung nach Leitfrage A14 (Testfälle)

Das Wirtschaftsquiz wurde mit einem vollständigen Satz an funktionalen Testfällen getestet. 
Alle Muss-User-Stories (Quiz starten, Fragen beantworten, Auswertung anzeigen, Fragen verwalten) 
sind durch konkrete Testfälle mit erwarteten Ergebnissen abgedeckt.

Als Testmethoden wurden manuelle Tests anhand der definierten Testfälle sowie exploratives Testen der GUI verwendet.

Nicht abgedeckt sind automatisierte Unit-Tests, Performance- oder Netzwerktests. 
Trotzdem decken die vorhandenen Testfälle die Benutzeranforderungen nahezu vollständig ab.

### 1.4 Wissensbeschaffung und Informationsquellen

Für die Umsetzung des Wirtschaftsquiz-Projekts haben wir gezielt fachlich passende und projektbezogene Informationsquellen verwendet. Die Auswahl der Quellen erfolgte nach dem Kriterium, dass sie direkt zur Lösung unserer Aufgaben (GUI-Entwicklung, Datenhaltung, Quizlogik) beitragen.

**Verwendete Informationsquellen:**

- **Python-Dokumentation**  
  https://docs.python.org  
  Grundlagen der Programmiersprache, Datentypen, Fehlerbehandlung

- **Tkinter GUI-Dokumentation**  
  https://docs.python.org/3/library/tkinter.html  
  Aufbau von Fenstern, Buttons, Eingabefeldern und Layouts für die Quiz-Oberfläche

- **JSON-Format (RFC 8259 / Python json-Modul)**  
  https://docs.python.org/3/library/json.html  
  Speicherung und Laden von Fragen, Themen und Quizzen

- **GitHub Docs**  
  https://docs.github.com  
  Versionsverwaltung, Repository-Struktur, Dokumentation im Team

- **Lehrmittel Wirtschaft (Schulunterlagen)**  
  Inhaltliche Grundlage für die Quizfragen (z. B. BIP, Angebot & Nachfrage, Staatseinnahmen)

---

### Nutzung der Quellen

Aus diesen Quellen haben wir die für unser Projekt relevanten Informationen gezielt ausgewählt und angewendet, z. B.:

- Verwendung von **tkinter-Widgets** (Buttons, Radiobuttons, Eingabefelder) für die Quiz-GUI  
- Einsatz von **JSON-Dateien** zur Speicherung von Fragen, Themen und Lösungen  
- Strukturierung des Programms mit **Klassen und Modulen** (Question, Quiz, QuizService, Storage)

Die Informationen wurden nicht nur kopiert, sondern **auf unser eigenes Projekt übertragen**, indem wir sie an unsere Anforderungen (Multiple-Choice, Freitext, Auswertung, Fragenverwaltung) angepasst haben.

---

### Nachvollziehbarkeit

Alle verwendeten Quellen sind öffentlich zugänglich und für Lehrpersonen sowie Projektbeteiligte jederzeit überprüfbar.  
Die Umsetzung ist im Code-Repository dokumentiert:
---

### 1.5 Systemgrenzen und Schnittstellen zur Aussenwelt

Das Wirtschaftsquiz ist als **eigenständige Desktop-Anwendung** konzipiert.  
Das System selbst umfasst die Benutzeroberfläche (GUI), die Quizlogik, die Auswertung sowie die Verwaltung der Fragen.

Alles, was **nicht direkt Teil der Anwendung ist**, gehört zur Aussenwelt.

---

### Beteiligte Akteure (Aussenwelt)

| Akteur | Rolle im System |
|-------|----------------|
| Lernende | Starten ein Quiz, beantworten Fragen und sehen ihr Ergebnis |
| Lehrpersonen | Erstellen, bearbeiten und exportieren Quizze |
| Betriebssystem | Startet das Programm und verwaltet Dateien |
| Dateisystem | Speichert und lädt Quizdateien (JSON) |

---

### Systemgrenze

Das System beginnt dort, wo die Anwendung startet (`main.py`) und endet dort, wo Dateien gespeichert oder geladen werden.

Nicht Teil des Systems sind:
- Das Betriebssystem (Windows, macOS, Linux)
- Der Benutzer (Lehrperson oder Lernende)
- Der Dateiaustausch (z. B. Weitergabe von Quizdateien per USB, Mail oder Teams)

---

### Schnittstellen

| Schnittstelle | Richtung | Beschreibung |
|--------------|--------|---------------|
| GUI (Tkinter) | Benutzer → System | Eingabe von Antworten, Auswahl von Themen, Erstellen von Fragen |
| GUI (Tkinter) | System → Benutzer | Anzeige von Fragen, Ergebnissen, Fehlermeldungen |
| JSON-Dateien | System → Aussenwelt | Export von Quizzen durch Lehrpersonen |
| JSON-Dateien | Aussenwelt → System | Import von Quizzen durch Lernende |
| Dateisystem | System ↔ Betriebssystem | Lesen und Schreiben der Quizdateien |

---

### Einbettung in den Schulalltag

Das System ist so gestaltet, dass Lehrpersonen Quizdateien erstellen und an Lernende weitergeben können, z. B.:
- per USB-Stick  
- per E-Mail  
- über Teams oder Schulplattform  

Die Lernenden laden diese Dateien in das Programm und bearbeiten genau dieses Quiz.  
Dadurch ist das Quiz **nicht an einen einzelnen Computer gebunden**, sondern kann realistisch im Unterricht eingesetzt werden.
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
### Abbildung: Zeitplan

<img width="1013" height="262" alt="image" src="https://github.com/user-attachments/assets/c38c4722-9cd5-4386-a22b-82fcbb0290ac" />


---
## 3 Entscheiden

### 3.1 Grundsätzliche Entscheidungen

 **Programmiersprache:**  
  Das Projekt wird in **Python** umgesetzt, da es einfach zu lesen ist, gute Bibliotheken für GUIs (z. B. *tkinter*) und Datenverwaltung (z. B. *json*) bietet.

 **Benutzeroberfläche (GUI):**  
  Die GUI wird mit **tkinter** erstellt. Diese Bibliothek ist plattformunabhängig, leichtgewichtig und ideal für Lernprojekte geeignet.  
  Ziel ist eine **klare und strukturierte Darstellung** mit Buttons, Menüs und Textfeldern.

**Datenverwaltung:**  
  Fragen, Themen und Quizze werden in **JSON-Dateien** gespeichert.  
  JSON ist leicht editierbar, wodurch Lehrpersonen direkt im Dateisystem Fragen ergänzen oder ändern können.

**Fragetypen:**  
  Das System unterstützt mehrere Typen:
  - *Multiple Choice*  
  - *Richtig/Falsch*  
  - *Freitext-Eingaben*  

 **Rollen & Berechtigungen:**  
  - *Lernende* können Quiz starten und Fragen beantworten.  
  - *Lehrpersonen* können Fragen und Themen verwalten (Hinzufügen, Ändern, Löschen).  

 **Zielsystem:**  
  Die Anwendung ist als **Offline-Desktop-App** konzipiert (Windows / macOS / Linux).

 **Designprinzipien:**  
  - Einfache Navigation und verständliche Benutzerführung.  
  - Übersichtliche Darstellung der Fragen.  
  - Sofortige Rückmeldung nach Abschluss des Quiz (richtige/falsche Antworten).  
  - Klare Trennung zwischen Lernenden- und Lehrpersonen-Bereich.
    
## 3.2 Vorgehensmodell und Informationsbasis

Zu Beginn des Projekts haben wir uns mit der Aufgabenstellung der IDPA sowie den Anforderungen an ein Lernprogramm auseinandergesetzt.
Wir haben uns entschieden, nach einem vereinfachten iterativen Vorgehensmodell (ähnlich Scrum) zu arbeiten:

Anforderungen wurden zuerst in User Stories festgehalten

Anschliessend in Arbeitspakete aufgeteilt

Danach schrittweise implementiert und getestet

Dieses Vorgehen war sinnvoll, da wir früh eine lauffähige Version hatten und Fehler (z. B. bei Multiple-Choice oder der GUI) in späteren Iterationen gezielt beheben konnten.

## 3.3 Technische Entscheidungsfindung

Vor der Umsetzung haben wir folgende Optionen verglichen:

Bereich	Mögliche Lösungen	Unsere Entscheidung	Begründung
Programmiersprache	Python, Java, C#	Python	Einfach lesbar, schnell umsetzbar, gut für GUI & JSON
GUI	Tkinter, Web-App	Tkinter	Keine Installation im Browser nötig, einfach für Desktop
Datenspeicherung	Datenbank, CSV, JSON	JSON-Dateien	Leicht verständlich, portabel, ideal für Quiz-Export
Quiz-Verteilung	Cloud, Server, Dateien	Export/Import (JSON)	Keine Server nötig, trotzdem Quiz verteilbar

Diese Entscheidungen wurden getroffen, weil sie zum Umfang einer Schul-IDPA passen, zuverlässig funktionieren und ohne externe Infrastruktur auskommen.

## 3.4 Entscheidung zur Quiz-Verteilung

Ursprünglich speicherte das System alle Fragen nur lokal.
Da eine zentrale Cloud-Lösung zu komplex gewesen wäre (Server, Benutzerkonten, Sicherheit), entschieden wir uns für ein Export-/Import-System:

Lehrpersonen können Quizze als Datei exportieren

Lernende können diese Datei laden und bearbeiten

So wird die Anforderung „Quiz an Lernende weitergeben“ technisch sauber erfüllt, ohne unnötige Komplexität.

---

### Design & Dokumentation

Das Design des Wirtschaftsquiz-Systems wurde mit geeigneten Mitteln dokumentiert und nachvollziehbar dargestellt.
Zur Visualisierung der Benutzerführung wurde ein GUI-Mockup erstellt, welches die wichtigsten Ansichten (Startseite, Quiz, Lehrerbereich, Ergebnisanzeige) sowie die Navigation zwischen ihnen zeigt. Dieses Mockup ermöglicht es, den Ablauf der Anwendung unabhängig vom Code zu verstehen.

Zusätzlich wurde die Systemstruktur durch ein Klassendiagramm und eine Modulübersicht dokumentiert. Die wichtigsten Komponenten (QuizService, Question, Quiz, JSONStorage, GUI-Klassen) sind darin ersichtlich und ihre Beziehungen zueinander klar dargestellt.

Auch ohne formales UML erfüllt die Dokumentation ihren Zweck, da:

- die Modulaufteilung klar sichtbar ist,
- die Verantwortlichkeiten der Klassen verständlich beschrieben sind,
- und die Funktionsweise des Systems für Aussenstehende nachvollziehbar bleibt.


### ERM / Datenmodell

Für das Wirtschaftsquiz wurde ein vollständiges Datenmodell definiert, das sowohl die fachlichen Objekte als auch ihre Beziehungen abbildet.

Die folgenden Entitäten wurden modelliert:

- Quiz (quiz_id, title, created_at)
- Question (question_id, topic, type, text, correct_answer)
- Option (option_id, question_id, option_text)
- QuizQuestion (Verknüpfung zwischen Quiz und Question)

Damit sind alle fachlich relevanten Datenstrukturen eindeutig definiert.

Die Beziehungen sind korrekt modelliert:

- Ein Quiz enthält mehrere Questions (n:m über QuizQuestion)
- Eine Question kann mehrere Options besitzen (1:n)

Primärschlüssel (quiz_id, question_id, option_id) und Fremdschlüssel (question_id, quiz_id) sind klar gekennzeichnet und logisch korrekt verwendet.

Die Attributlisten sind vollständig und die Datentypen (z. B. UUID, String, Date) sind definiert, sodass sowohl die Speicherung als auch die Verarbeitung der Daten eindeutig nachvollziehbar ist.



Abbildung 1: Mockup des GUI-Entwurfs

<img width="1521" height="662" alt="image" src="https://github.com/user-attachments/assets/10859e27-8337-468f-b311-471e15ac448e" />

Abbildung 2: Use-Case-Diagramm

<img width="350" height="655" alt="image" src="https://github.com/user-attachments/assets/ea867c3a-1963-4e3f-95bf-029689d36241" />

Abbildung 3: Klassendiagramm 

<img width="279" height="521" alt="image" src="https://github.com/user-attachments/assets/27f80e86-9de0-4793-b120-ee110d8ef7fb" />

Abbildung 4: Ablaufdiagram

<img width="228" height="547" alt="image" src="https://github.com/user-attachments/assets/5a686c19-c385-48c6-a0a7-689a9b005a7d" />

Abbildung 5: ERMdiagram

<img width="436" height="299" alt="image" src="https://github.com/user-attachments/assets/0ad811f5-8a1e-4ed3-bf8f-5985e91db553" />



## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
|------|--------|------------|----------------|-------------------|
| 2.A | 05.11.2025 | Grigioni | 90’ | 100’ |
| 2.B | 05.11.2025 | Bytyqi | 90’ | 110’ |
| 2.C | 05.11.2025 | Lai | 90’ | 95’ |
| 3.A | 12.11.2025 | Grigioni | 90’ | 100’ |
| 3.B | 12.11.2025 | Bytyqi | 90’ | 105’ |
| 3.C | 12.11.2025 | Lai | 90’ | 90’ |
| 4.A | 26.11.2025 | Team | 120’ | 150’ |
| 5.A | 10.12.2025 | Team | 90’ | 120’ |
| 6.A | 13.01.2026 | Team | 60’ | 75’ |

**Kommentar:**  
Einige Arbeitspakete dauerten etwas länger als geplant, da zusätzliche Fehler behoben und die GUI weiter verbessert werden musste. Der Mehraufwand führte jedoch zu einer stabileren und benutzerfreundlicheren Anwendung.

---

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
|------|--------|----------|--------|
| 1.1 | 19.11.2025 | OK | Team |
| 2.1 | 19.11.2025 | OK | Bytyqi |
| 2.2 | 26.11.2025 | OK | Grigioni |
| 3.1 | 26.11.2025 | OK | Lai |
| 3.2 | 26.11.2025 | OK | Team |
| 4.1 | 02.12.2025 | OK | Bytyqi |
| 5.1 | 02.12.2025 | OK | Team |

**Fazit:**  
Alle definierten Testfälle wurden erfolgreich durchgeführt. Fehler in der Multiple-Choice-Auswertung und der Anzeige der Antworten wurden während der Testphase entdeckt und behoben. Das System erfüllt die Muss-Anforderungen aus den User Stories.

### 5.2 Exploratives Testen

| BR-№ | Ausgangslage | Eingabe | Erwartete Ausgabe | Tatsächliche Ausgabe |
|------|--------------|---------|-------------------|----------------------|
| I | Quiz läuft | Text statt Auswahl bei MC-Frage | Fehlermeldung | Fehlermeldung wird angezeigt |
| II | Frage wird erstellt | Leere Felder | Hinweis auf fehlende Eingaben | Warnmeldung erscheint |
| III | Quiz beendet | Klick auf „Zurück“ | Startseite wird angezeigt | Startseite erscheint korrekt |

---

## 6 Auswerten

**Lernbericht (Zusammenfassung):**

Während des Projekts haben wir gelernt, ein größeres Programm in mehrere Komponenten (GUI, Logik, Datenhaltung) aufzuteilen und diese gezielt miteinander zu verbinden. Besonders wertvoll war die Testphase, da wir dort viele versteckte Fehler gefunden haben, vor allem bei der Auswertung von Multiple-Choice-Antworten und der Darstellung der Resultate.

Die Arbeit im Team war wichtig, um verschiedene Blickwinkel einzubringen: Während ein Teil sich auf die Logik konzentrierte, arbeiteten andere an der Benutzeroberfläche und der Dokumentation. Dadurch konnten Probleme schneller erkannt und gelöst werden.



