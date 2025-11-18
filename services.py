from typing import Any, Dict, List
from models import Quiz, Question

class QuizService:
    """3.A: Logik für Beantwortung & Auswertung + 3.C: Lösungen zeigen"""
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

        self.answers.append({"id": q.id, "given": user_answer, "ok": ok})
        if ok:
            self.correct += 1
        self.index += 1
        return ok

    def result(self) -> Dict[str, Any]:
        res = {
            "total": len(self.quiz.questions),
            "correct": self.correct,
            "answers": self.answers,
        }
        if self.quiz.show_solutions:
            res["solutions"] = [
    {
        "id": q.id,
        "text": q.text,
        "type": q.type,
        "answer": q.answer,
        "topic": q.topic,
        "options": q.options,
    }
    for q in self.quiz.questions
]
        return res
