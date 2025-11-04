
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Literal, Any
import json
import uuid
import os



QuestionType = Literal["mc", "tf", "text"]

@dataclass
class Question:
    """
    Basismodell für eine Frage.
    - type: 'mc' (Multiple Choice), 'tf' (True/False), 'text' (Freitext)
    - options: nur für 'mc' relevant (Liste von Antwortmöglichkeiten)
    - answer: 
        - bei 'mc': Index (int) der richtigen Option
        - bei 'tf': bool (True/False)
        - bei 'text': str (Lösungstext oder Musterlösung)
    """
    id: str
    topic: str
    text: str
    type: QuestionType
    options: Optional[List[str]] = None
    answer: Any = None
    meta: Dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.text.strip():
            raise ValueError("Fragetext darf nicht leer sein.")
        if not self.topic.strip():
            raise ValueError("Thema darf nicht leer sein.")
        if self.type not in ("mc", "tf", "text"):
            raise ValueError("Ungültiger Fragetyp.")

        if self.type == "mc":
            if not self.options or len(self.options) < 2:
                raise ValueError("MC-Fragen benötigen mindestens 2 Optionen.")
            if not isinstance(self.answer, int) or not (0 <= self.answer < len(self.options)):
                raise ValueError("MC-Antwort muss ein gültiger Index sein.")
        elif self.type == "tf":
            if not isinstance(self.answer, bool):
                raise ValueError("TF-Antwort muss bool (True/False) sein.")
        elif self.type == "text":
            if not isinstance(self.answer, str) or not self.answer.strip():
                raise ValueError("Text-Antwort benötigt eine Musterlösung (str).")

@dataclass
class Quiz:
    """
    Ein Quiz besteht aus:
    - title: Anzeigename
    - questions: geordnete Liste von Fragen (IDs oder Objekte)
    - show_solutions: ob nach Abschluss die Lösungen gezeigt werden
    """
    id: str
    title: str
    questions: List[Question] = field(default_factory=list)
    show_solutions: bool = True

    def validate(self) -> None:
        if not self.title.strip():
            raise ValueError("Quiz-Titel darf nicht leer sein.")
        if not self.questions:
            raise ValueError("Ein Quiz benötigt mindestens eine Frage.")
        for q in self.questions:
            q.validate()



class JSONStorage:
    """
    Verwaltet das Lesen/Schreiben von Fragen & Quizzen in JSON-Dateien.
    Struktur der Datei:
    {
      "questions": [...],
      "quizzes": [...]
    }
    """
    def __init__(self, path: str = "data.json"):
        self.path = path
        self.data: Dict[str, Any] = {"questions": [], "quizzes": []}
        self._ensure_file()

    def _ensure_file(self) -> None:
        if os.path.exists(self.path):
            self.load()
        else:
            self.save()

    def load(self) -> None:
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        # Fallbacks, falls Schlüssel fehlen
        self.data.setdefault("questions", [])
        self.data.setdefault("quizzes", [])

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def list_questions(self, topic: Optional[str] = None) -> List[Question]:
        items = self.data["questions"]
        if topic:
            items = [q for q in items if q.get("topic") == topic]
        return [Question(**q) for q in items]

    def get_question(self, qid: str) -> Optional[Question]:
        for q in self.data["questions"]:
            if q["id"] == qid:
                return Question(**q)
        return None

    def add_question(self, q: Question) -> Question:
        q.validate()
        self.data["questions"].append(asdict(q))
        self.save()
        return q

    def update_question(self, qid: str, **changes) -> Question:
        found = None
        for i, q in enumerate(self.data["questions"]):
            if q["id"] == qid:
                q.update(changes)
                # Validieren mit Modell
                candidate = Question(**q)
                candidate.validate()
                self.data["questions"][i] = asdict(candidate)
                found = Question(**self.data["questions"][i])
                break
        if not found:
            raise KeyError(f"Frage {qid} nicht gefunden.")
        self.save()
        return found

    def delete_question(self, qid: str) -> None:
        before = len(self.data["questions"])
        self.data["questions"] = [q for q in self.data["questions"] if q["id"] != qid]
        after = len(self.data["questions"])
        if before == after:
            raise KeyError(f"Frage {qid} nicht gefunden.")
        # Frage auch aus Quizzen entfernen
        for quiz in self.data["quizzes"]:
            quiz["questions"] = [q for q in quiz["questions"] if q["id"] != qid]
        self.save()

    def list_quizzes(self) -> List[Quiz]:
        return [Quiz(q["id"], q["title"], [Question(**qq) for qq in q["questions"]], q.get("show_solutions", True))
                for q in self.data["quizzes"]]

    def get_quiz(self, quiz_id: str) -> Optional[Quiz]:
        for q in self.data["quizzes"]:
            if q["id"] == quiz_id:
                return Quiz(q["id"], q["title"], [Question(**qq) for qq in q["questions"]], q.get("show_solutions", True))
        return None

    def add_quiz(self, quiz: Quiz) -> Quiz:
        quiz.validate()
        payload = {
            "id": quiz.id,
            "title": quiz.title,
            "show_solutions": quiz.show_solutions,
            "questions": [asdict(q) for q in quiz.questions],
        }
        self.data["quizzes"].append(payload)
        self.save()
        return quiz

    def update_quiz(self, quiz_id: str, **changes) -> Quiz:
        found = None
        for i, q in enumerate(self.data["quizzes"]):
            if q["id"] == quiz_id:
                q.update(changes)
                # Validieren mit Modell
                candidate = Quiz(
                    id=q["id"],
                    title=q["title"],
                    show_solutions=q.get("show_solutions", True),
                    questions=[Question(**qq) for qq in q["questions"]],
                )
                candidate.validate()
                # zurück in dict-Form
                self.data["quizzes"][i] = {
                    "id": candidate.id,
                    "title": candidate.title,
                    "show_solutions": candidate.show_solutions,
                    "questions": [asdict(qq) for qq in candidate.questions],
                }
                found = self.get_quiz(quiz_id)
                break
        if not found:
            raise KeyError(f"Quiz {quiz_id} nicht gefunden.")
        self.save()
        return found

    def delete_quiz(self, quiz_id: str) -> None:
        before = len(self.data["quizzes"])
        self.data["quizzes"] = [q for q in self.data["quizzes"] if q["id"] != quiz_id]
        after = len(self.data["quizzes"])
        if before == after:
            raise KeyError(f"Quiz {quiz_id} nicht gefunden.")
        self.save()

    def assemble_quiz_by_topics(self, title: str, topics: List[str], limit_per_topic: Optional[int] = None) -> Quiz:
        """
        Stellt ein Quiz aus Fragen bestimmter Themen zusammen.
        - limit_per_topic: wenn gesetzt, pro Thema maximal diese Anzahl.
        """
        chosen: List[Question] = []
        for t in topics:
            qs = [q for q in self.list_questions(topic=t)]
            if limit_per_topic is not None:
                qs = qs[:limit_per_topic]
            chosen.extend(qs)
        if not chosen:
            raise ValueError("Keine passenden Fragen gefunden.")
        quiz = Quiz(id=_uid(), title=title, questions=chosen, show_solutions=True)
        return self.add_quiz(quiz)



class QuizService:
    """
    Fachlogik fürs Durchführen eines Quiz (ohne GUI).
    """
    def __init__(self, quiz: Quiz):
        quiz.validate()
        self.quiz = quiz
        self.index = 0
        self.correct = 0
        self.answers: List[Dict[str, Any]] = []

    def has_next(self) -> bool:
        return self.index < len(self.quiz.questions)

    def current_question(self) -> Question:
        return self.quiz.questions[self.index]

    def submit_answer(self, user_answer: Any) -> bool:
        q = self.current_question()
        ok = False
        if q.type == "mc":
            ok = (user_answer == q.answer)
        elif q.type == "tf":
            ok = (bool(user_answer) == q.answer)
        elif q.type == "text":
            ok = str(user_answer).strip().lower() == str(q.answer).strip().lower()

        self.answers.append({"id": q.id, "ok": ok, "given": user_answer})
        if ok:
            self.correct += 1
        self.index += 1
        return ok

    def result(self) -> Dict[str, Any]:
        return {
            "total": len(self.quiz.questions),
            "correct": self.correct,
            "answers": self.answers,
            "show_solutions": self.quiz.show_solutions,
            "solutions": [ {"id": q.id, "type": q.type, "answer": q.answer} for q in self.quiz.questions ]
        }


def _uid() -> str:
    return uuid.uuid4().hex


if __name__ == "__main__":
    store = JSONStorage("data.json")

    # Beispiel-Fragen hinzufügen (nur wenn leer)
    if not store.list_questions():
        q1 = Question(id=_uid(), topic="Grundlagen", text="Inflation bedeutet ...", type="mc",
                      options=["Preisniveau sinkt", "Preisniveau steigt", "Arbeitslosigkeit sinkt"], answer=1)
        q2 = Question(id=_uid(), topic="Grundlagen", text="Angebot und Nachfrage bestimmen den Preis.", type="tf",
                      answer=True)
        q3 = Question(id=_uid(), topic="BIP", text="Wofür steht BIP?", type="text", answer="Bruttoinlandsprodukt")

        for q in (q1, q2, q3):
            store.add_question(q)

    # Quiz aus Themen zusammenstellen & speichern
    quiz = store.assemble_quiz_by_topics(title="Wirtschaft Basics", topics=["Grundlagen", "BIP"], limit_per_topic=5)
    print(f"Quiz erstellt: {quiz.title} mit {len(quiz.questions)} Fragen (ID={quiz.id})")

    # Quiz-Service (ohne GUI) kurz demonstrieren
    svc = QuizService(quiz)
    while svc.has_next():
        cur = svc.current_question()
        # Demo-Antworten (hier stumpf immer 0/True/Text) – später durch GUI/CLI ersetzen
        if cur.type == "mc":
            answer = 0
        elif cur.type == "tf":
            answer = True
        else:
            answer = "Bruttoinlandsprodukt"
        svc.submit_answer(answer)

    print("Ergebnis:", svc.result())
