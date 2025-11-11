from models import Question
from storage import JSONStorage
from services import QuizService
import admin
from utils import uid

def seed_if_empty(store: JSONStorage):
    if store.list_questions():
        return
    # Beispiel-Fragen
    store.add_question(Question(id=uid(), topic="Grundlagen", text="Was ist Inflation?", type="mc",
                                options=["Preisniveau sinkt", "Preisniveau steigt"], answer=1))
    store.add_question(Question(id=uid(), topic="BIP", text="BIP steht für Bruttoinlandsprodukt.", type="tf", answer=True))
    store.add_question(Question(id=uid(), topic="BIP", text="Wofür steht BIP?", type="text", answer="Bruttoinlandsprodukt"))

def run_quiz(store: JSONStorage):
    topics = input("Themen (Kommagetrennt, z.B. Grundlagen,BIP): ").split(",")
    topics = [t.strip() for t in topics if t.strip()]
    quiz = store.assemble_quiz_by_topics("Ad-hoc Quiz", topics, limit_per_topic=None)
    print(f"\\nQuiz '{quiz.title}' mit {len(quiz.questions)} Fragen.\\n")
    svc = QuizService(quiz)
    while svc.has_next():
        q = svc.current_question()
        print(f"Frage: {q.text}")
        if q.type == 'mc':
            for i, opt in enumerate(q.options or []):
                print(f"  {i}) {opt}")
            ans = int(input("Antwort (Index): "))
        elif q.type == 'tf':
            ans = input("(t/f): ").strip().lower() == 't'
        else:
            ans = input("Antwort: ").strip()
        ok = svc.submit_answer(ans)
        print("✅ Richtig\\n" if ok else "❌ Falsch\\n")
    res = svc.result()
    print(f"Ergebnis: {res['correct']} / {res['total']}\\n")
    if 'solutions' in res:
        print("Lösungen:")
        for s in res['solutions']:
            print(f"- ({s['type']}) {s['text']} -> {s['answer']}")

def main():
    store = JSONStorage("data.json")
    seed_if_empty(store)
    while True:
        print("\\nWirtschaftsquiz – Menü")
        print("1) Quiz starten")
        print("2) Frage hinzufügen")
        print("3) Frage bearbeiten")
        print("4) Frage löschen")
        print("5) Fragen auflisten")
        print("0) Beenden")
        choice = input("> ").strip()
        if choice == '1':
            run_quiz(store)
        elif choice == '2':
            admin.add_question_cli(store)
        elif choice == '3':
            admin.edit_question_cli(store)
        elif choice == '4':
            admin.delete_question_cli(store)
        elif choice == '5':
            for q in store.list_questions():
                print(f"{q.id} | {q.topic} | {q.type} | {q.text}")
        elif choice == '0':
            break
        else:
            print("Unbekannte Auswahl.")

if __name__ == "__main__":
    main()
