import json, os
from dataclasses import asdict
from typing import List, Dict, Any, Optional
from models import Question, Quiz
from utils import uid
from typing import Any

class JSONStorage:
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
        self.data.setdefault("questions", [])
        self.data.setdefault("quizzes", [])

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    # --- CRUD Fragen ---
    def list_questions(self, topic: Optional[str] = None):
        items = self.data["questions"]
        if topic:
            items = [q for q in items if q.get("topic") == topic]
        return [Question(**q) for q in items]
    
    def assemble_quiz_by_topics(self, title: str, topics: list[str], limit_per_topic=None):
        chosen = []
        for t in topics:
            qs = [q for q in self.list_questions(topic=t)]
            if limit_per_topic:
                qs = qs[:limit_per_topic]
            chosen.extend(qs)

        if not chosen:
            raise ValueError("Keine passenden Fragen gefunden.")

        # Quiz nur erstellen (nicht automatisch speichern, optional!)
        from models import Quiz
        return Quiz(id=uid(), title=title, questions=chosen, show_solutions=True)


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
        for i, q in enumerate(self.data["questions"]):
            if q["id"] == qid:
                q.update(changes)
                obj = Question(**q)
                obj.validate()
                self.data["questions"][i] = asdict(obj)
                self.save()
                return obj
        raise KeyError(f"Frage {qid} nicht gefunden.")

    def delete_question(self, qid: str) -> None:
        before = len(self.data["questions"])
        self.data["questions"] = [q for q in self.data['questions'] if q['id'] != qid]
        if len(self.data["questions"]) == before:
            raise KeyError(f"Frage {qid} nicht gefunden.")
        # Aus Quizzen entfernen
        for quiz in self.data["quizzes"]:
            quiz["questions"] = [qq for qq in quiz["questions"] if qq["id"] != qid]
        self.save()

    # --- Quiz ---
    def add_quiz(self, quiz: Quiz) -> Quiz:
        quiz.validate()
        payload = {
            "id": quiz.id,
            "title": quiz.title,
            "show_solutions": quiz.show_solutions,
            "questions": [asdict(q) for q in quiz.questions],
        }

        # Nur EIN Quiz pro Titel speichern (ersetzen statt duplizieren)
        replaced = False
        for i, q in enumerate(self.data["quizzes"]):
            if q.get("title") == quiz.title:
                self.data["quizzes"][i] = payload
                replaced = True
                break

        if not replaced:
            self.data["quizzes"].append(payload)

        self.save()
        return quiz

    
    # --- Export / Import (Quiz weitergeben) ---

    def export_quiz_to_file(self, quiz: Quiz, path: str) -> None:
        quiz.validate()
        payload = {
            "id": quiz.id,
            "title": quiz.title,
            "show_solutions": quiz.show_solutions,
            "questions": [asdict(q) for q in quiz.questions],
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def load_quiz_from_file(self, path: str) -> Quiz:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)

        questions_raw = payload.get("questions", [])
        questions = [Question(**q) for q in questions_raw]

        quiz = Quiz(
            payload.get("id") or uid(),
            payload.get("title") or "Wirtschaftsquiz",
            questions,
            bool(payload.get("show_solutions", True)),
        )
        quiz.validate()
        return quiz

    