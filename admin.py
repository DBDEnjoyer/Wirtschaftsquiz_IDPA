# 3.B: Admin-CLI für Hinzufügen, Bearbeiten, Löschen
from typing import List
from models import Question
from storage import JSONStorage
from utils import uid

def add_question_cli(store: JSONStorage) -> None:
    topic = input("Thema: ").strip()
    text = input("Fragetext: ").strip()
    qtype = input("Typ (mc/tf/text): ").strip()
    if qtype == "mc":
        options: List[str] = []
        print("Antwortoptionen (mind. 2). Leere Eingabe beendet:")
        while True:
            o = input(f"Option {len(options)}: ").strip()
            if not o:
                break
            options.append(o)
        correct = int(input("Index der richtigen Option (0-basiert): ").strip())
        q = Question(id=uid(), topic=topic, text=text, type="mc", options=options, answer=correct)
    elif qtype == "tf":
        ans = input("Richtig (t) / Falsch (f): ").lower().strip() == "t"
        q = Question(id=uid(), topic=topic, text=text, type="tf", answer=ans)
    else:
        ans = input("Musterlösung (Text): ").strip()
        q = Question(id=uid(), topic=topic, text=text, type="text", answer=ans)
    store.add_question(q)
    print("Frage hinzugefügt:", q.id)

def edit_question_cli(store: JSONStorage) -> None:
    qid = input("ID der zu bearbeitenden Frage: ").strip()
    q = store.get_question(qid)
    if not q:
        print("Nicht gefunden."); return
    print("Leer lassen, um Wert zu behalten.")
    topic = input(f"Thema ({q.topic}): ").strip() or q.topic
    text  = input(f"Fragetext ({q.text}): ").strip() or q.text
    if q.type == "mc":
        print("Aktuelle Optionen:", q.options)
        change = input("Optionen neu eingeben? (j/n): ").lower().strip() == "j"
        options = q.options
        answer  = q.answer
        if change:
            options = []
            while True:
                o = input(f"Option {len(options)}: ").strip()
                if not o: break
                options.append(o)
            answer = int(input("Index der richtigen Option: ").strip())
        store.update_question(qid, topic=topic, text=text, options=options, answer=answer)
    elif q.type == "tf":
        ans_in = input(f"Antwort (t/f) ({'t' if q.answer else 'f'}): ").strip().lower()
        if ans_in in ('t','f'):
            store.update_question(qid, topic=topic, text=text, answer=(ans_in=='t'))
        else:
            store.update_question(qid, topic=topic, text=text)
    else:
        ans = input(f"Musterlösung ({q.answer}): ").strip() or q.answer
        store.update_question(qid, topic=topic, text=text, answer=ans)
    print("Frage aktualisiert.")

def delete_question_cli(store: JSONStorage) -> None:
    qid = input("ID der zu löschenden Frage: ").strip()
    store.delete_question(qid)
    print("Frage gelöscht.")
