from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Literal, Any

QuestionType = Literal["mc", "tf", "text"]

@dataclass
class Question:
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
