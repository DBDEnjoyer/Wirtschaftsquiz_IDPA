import tkinter as tk
from tkinter import ttk, messagebox
from typing import List

from storage import JSONStorage
from services import QuizService
from models import Question
from utils import uid


# ---------- Haupt-App ----------

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wirtschaftsquiz")
        self.geometry("950x600")
        self.minsize(900, 550)

        # Dark-/Modern-Style
        self.configure(bg="#1e1e1e")
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "TFrame",
            background="#1e1e1e"
        )
        style.configure(
            "Card.TFrame",
            background="#252526",
            relief="flat"
        )
        style.configure(
            "TLabel",
            background="#1e1e1e",
            foreground="#f0f0f0",
            font=("Segoe UI", 11)
        )
        style.configure(
            "Header.TLabel",
            font=("Segoe UI Semibold", 20),
            foreground="#ffffff",
            background="#1e1e1e"
        )
        style.configure(
            "SubHeader.TLabel",
            font=("Segoe UI", 12),
            foreground="#bbbbbb",
            background="#1e1e1e"
        )
        style.configure(
            "TButton",
            font=("Segoe UI", 11),
            padding=6,
            background="#0078d4",
            foreground="#ffffff"
        )
        style.map(
            "TButton",
            background=[("active", "#1490ff")],
        )
        style.configure(
            "Accent.TButton",
            font=("Segoe UI Semibold", 11),
            padding=8,
            background="#0078d4",
            foreground="#ffffff"
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#1490ff")],
        )
        style.configure(
            "Danger.TButton",
            background="#d13438",
            foreground="#ffffff"
        )
        style.map(
            "Danger.TButton",
            background=[("active", "#f1707b")],
        )

        style.configure(
            "Quiz.TLabel",
            background="#252526",
            foreground="#f0f0f0",
            font=("Segoe UI", 13)
        )

        self.store = JSONStorage("data.json")
        self.current_quiz_service: QuizService | None = None

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, TopicSelectPage, QuizPage, ResultPage, ManageQuestionsPage):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    # ---------- Hilfsfunktionen ----------

    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()

    def get_topics(self) -> List[str]:
        questions = self.store.list_questions()
        topics = sorted({q.topic for q in questions})
        return topics

    def start_quiz(self, topics: List[str]):
        if not topics:
            messagebox.showwarning("Hinweis", "Bitte mindestens ein Thema auswählen.")
            return
        try:
            quiz = self.store.assemble_quiz_by_topics("Wirtschaftsquiz", topics, limit_per_topic=None)
        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
            return
        self.current_quiz_service = QuizService(quiz)
        quiz_page: QuizPage = self.frames["QuizPage"]  # type: ignore
        self.show_frame("QuizPage")
        quiz_page.load_next_question()


def run_gui():
    app = QuizApp()
    app.mainloop()


# ---------- Startseite ----------

class StartPage(ttk.Frame):
    def __init__(self, parent, controller: QuizApp):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Wirtschaftsquiz", style="Header.TLabel")
        header.pack(pady=(40, 10))

        sub = ttk.Label(
            self,
            text="Wissen testen, Fragen verwalten und Ergebnisse auswerten.",
            style="SubHeader.TLabel"
        )
        sub.pack(pady=(0, 30))

        card = ttk.Frame(self, style="Card.TFrame")
        card.pack(padx=40, pady=10, fill="x")
        card.columnconfigure(0, weight=1)

        quiz_btn = ttk.Button(
            card,
            text="Quiz starten",
            style="Accent.TButton",
            command=lambda: controller.show_frame("TopicSelectPage")
        )
        quiz_btn.grid(row=0, column=0, padx=20, pady=(25, 10), sticky="ew")

        manage_btn = ttk.Button(
            card,
            text="Fragen verwalten",
            command=lambda: controller.show_frame("ManageQuestionsPage")
        )
        manage_btn.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        exit_btn = ttk.Button(
            card,
            text="Beenden",
            style="Danger.TButton",
            command=controller.destroy
        )
        exit_btn.grid(row=2, column=0, padx=20, pady=(10, 25), sticky="ew")


# ---------- Themenauswahl ----------

class TopicSelectPage(ttk.Frame):
    def __init__(self, parent, controller: QuizApp):
        super().__init__(parent)
        self.controller = controller

        topbar = ttk.Frame(self)
        topbar.pack(fill="x", padx=20, pady=(20, 10))

        title = ttk.Label(topbar, text="Themen auswählen", style="Header.TLabel")
        title.pack(side="left")

        back_btn = ttk.Button(
            topbar,
            text="Zurück",
            command=lambda: controller.show_frame("StartPage")
        )
        back_btn.pack(side="right")

        body = ttk.Frame(self, style="Card.TFrame")
        body.pack(fill="both", expand=True, padx=20, pady=10)

        ttk.Label(
            body,
            text="Bitte wählen Sie ein oder mehrere Themen für das Quiz aus.",
            style="SubHeader.TLabel"
        ).pack(anchor="w", padx=20, pady=(20, 10))

        self.listbox = tk.Listbox(
            body,
            selectmode="multiple",
            activestyle="none",
            bg="#1e1e1e",
            fg="#f0f0f0",
            highlightthickness=0,
            relief="flat",
            font=("Segoe UI", 11)
        )
        self.listbox.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        start_btn = ttk.Button(
            body,
            text="Quiz starten",
            style="Accent.TButton",
            command=self._start_quiz
        )
        start_btn.pack(padx=20, pady=(0, 20), anchor="e")

    def on_show(self):
        self.listbox.delete(0, tk.END)
        topics = self.controller.get_topics()
        if not topics:
            self.listbox.insert(tk.END, "(Keine Themen vorhanden – bitte zuerst Fragen anlegen.)")
            self.listbox.config(state="disabled")
        else:
            self.listbox.config(state="normal")
            for t in topics:
                self.listbox.insert(tk.END, t)

    def _start_quiz(self):
        if self.listbox.cget("state") == "disabled":
            return
        indices = self.listbox.curselection()
        topics = [self.listbox.get(i) for i in indices]
        self.controller.start_quiz(topics)


# ---------- Quiz-Seite ----------

class QuizPage(ttk.Frame):
    def __init__(self, parent, controller: QuizApp):
        super().__init__(parent)
        self.controller = controller
        self.current_widgets: List[tk.Widget] = []
        self.answer_var = tk.StringVar()
        self.tf_var = tk.BooleanVar()

        self.topbar = ttk.Frame(self)
        self.topbar.pack(fill="x", padx=20, pady=(20, 10))

        self.title_lbl = ttk.Label(self.topbar, text="Quiz", style="Header.TLabel")
        self.title_lbl.pack(side="left")

        self.progress_lbl = ttk.Label(self.topbar, text="", style="SubHeader.TLabel")
        self.progress_lbl.pack(side="right")

        self.card = ttk.Frame(self, style="Card.TFrame")
        self.card.pack(fill="both", expand=True, padx=20, pady=10)
        self.card.columnconfigure(0, weight=1)

        self.question_lbl = ttk.Label(self.card, text="", style="Quiz.TLabel", wraplength=800)
        self.question_lbl.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        self.answers_frame = ttk.Frame(self.card, style="Card.TFrame")
        self.answers_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 15))
        self.card.rowconfigure(1, weight=1)

        self.feedback_lbl = ttk.Label(self.card, text="", style="SubHeader.TLabel")
        self.feedback_lbl.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 10))

        bottom = ttk.Frame(self.card, style="Card.TFrame")
        bottom.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 20))
        bottom.columnconfigure(0, weight=1)

        self.submit_btn = ttk.Button(
            bottom,
            text="Antwort bestätigen",
            style="Accent.TButton",
            command=self.submit_answer
        )
        self.submit_btn.grid(row=0, column=0, sticky="e")

    def load_next_question(self):
        svc = self.controller.current_quiz_service
        if not svc:
            return

        if not svc.has_next():
            self.controller.show_frame("ResultPage")
            result_page: ResultPage = self.controller.frames["ResultPage"]  # type: ignore
            result_page.show_result()
            return

        q = svc.current_question()
        index = svc.index + 1
        total = len(svc.quiz.questions)
        self.progress_lbl.config(text=f"Frage {index}/{total} – Thema: {q.topic}")

        self.question_lbl.config(text=q.text)
        self.feedback_lbl.config(text="")
        for w in self.current_widgets:
            w.destroy()
        self.current_widgets.clear()

        self.answer_var.set("")
        self.tf_var.set(False)

        if q.type == "mc":
            self._build_mc(q)
        elif q.type == "tf":
            self._build_tf(q)
        else:
            self._build_text(q)

    def _build_mc(self, q: Question):
        for i, opt in enumerate(q.options or []):
            rb = ttk.Radiobutton(
                self.answers_frame,
                text=opt,
                value=str(i),
                variable=self.answer_var
            )
            rb.pack(anchor="w", pady=4)
            self.current_widgets.append(rb)

    def _build_tf(self, q: Question):
        true_rb = ttk.Radiobutton(
            self.answers_frame,
            text="Richtig",
            value="true",
            variable=self.answer_var
        )
        false_rb = ttk.Radiobutton(
            self.answers_frame,
            text="Falsch",
            value="false",
            variable=self.answer_var
        )
        true_rb.pack(anchor="w", pady=4)
        false_rb.pack(anchor="w", pady=4)
        self.current_widgets.extend([true_rb, false_rb])

    def _build_text(self, q: Question):
        entry = ttk.Entry(self.answers_frame, textvariable=self.answer_var, width=60)
        entry.pack(anchor="w", pady=4)
        entry.focus()
        self.current_widgets.append(entry)

    def submit_answer(self):
        svc = self.controller.current_quiz_service
        if not svc:
            return

        q = svc.current_question()
        raw = self.answer_var.get()

        if q.type == "mc":
            if raw == "":
                messagebox.showinfo("Hinweis", "Bitte eine Antwort auswählen.")
                return
            user_answer = int(raw)
        elif q.type == "tf":
            if raw not in ("true", "false"):
                messagebox.showinfo("Hinweis", "Bitte 'Richtig' oder 'Falsch' wählen.")
                return
            user_answer = (raw == "true")
        else:
            if not raw.strip():
                messagebox.showinfo("Hinweis", "Bitte eine Antwort eingeben.")
                return
            user_answer = raw

        ok = svc.submit_answer(user_answer)
        if ok:
            self.feedback_lbl.config(text="Richtig!", foreground="#4caf50")
        else:
            self.feedback_lbl.config(text="Leider falsch.", foreground="#f44336")

        # kleine Verzögerung wäre nice, aber hier direkt weiter:
        self.load_next_question()


# ---------- Ergebnis-Seite ----------

class ResultPage(ttk.Frame):
    def __init__(self, parent, controller: QuizApp):
        super().__init__(parent)
        self.controller = controller

        topbar = ttk.Frame(self)
        topbar.pack(fill="x", padx=20, pady=(20, 10))

        title = ttk.Label(topbar, text="Ergebnis", style="Header.TLabel")
        title.pack(side="left")

        back_btn = ttk.Button(
            topbar,
            text="Zurück zur Startseite",
            command=lambda: controller.show_frame("StartPage")
        )
        back_btn.pack(side="right")

        card = ttk.Frame(self, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=20, pady=10)

        self.summary_lbl = ttk.Label(card, text="", style="SubHeader.TLabel")
        self.summary_lbl.pack(anchor="w", padx=20, pady=(20, 10))

        columns = ("frage", "richtig", "gegeben")
        self.tree = ttk.Treeview(card, columns=columns, show="headings")
        self.tree.heading("frage", text="Frage")
        self.tree.heading("richtig", text="Richtig?")
        self.tree.heading("gegeben", text="Gegebene Antwort")
        self.tree.column("frage", width=450)
        self.tree.column("richtig", width=80, anchor="center")
        self.tree.column("gegeben", width=250)
        self.tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def show_result(self):
        svc = self.controller.current_quiz_service
        if not svc:
            return
        res = svc.result()
        total = res["total"]
        correct = res["correct"]
        self.summary_lbl.config(
            text=f"Sie haben {correct} von {total} Fragen richtig beantwortet."
        )

        self.tree.delete(*self.tree.get_children())

        solutions_by_id = {}
        for s in res.get("solutions", []):
            solutions_by_id[s["id"]] = s

for a in res["answers"]:
    qid = a["id"]
    ok = a["ok"]
    given = a["given"]
    sol = solutions_by_id.get(qid)

    frage_text = sol["text"] if sol else qid
    korrekt = "Ja" if ok else "Nein"

    if sol and sol["type"] == "mc":
        options = sol.get("options") or []
        
        correct_idx = sol["answer"]
        correct_txt = options[correct_idx] if isinstance(correct_idx, int) and 0 <= correct_idx < len(options) else str(correct_idx)
        
        if isinstance(given, int) and 0 <= given < len(options):
            given_txt = options[given]
        else:
            given_txt = str(given)
    elif sol and sol["type"] == "tf":
        correct_txt = "Richtig" if sol["answer"] else "Falsch"
        given_txt = "Richtig" if bool(given) else "Falsch"
    else:  # Textfrage
        correct_txt = str(sol["answer"]) if sol else ""
        given_txt = str(given)


    self.tree.insert("", "end", values=(frage_text, korrekt, given_txt))


# ---------- Fragenverwaltung ----------

class ManageQuestionsPage(ttk.Frame):
    def __init__(self, parent, controller: QuizApp):
        super().__init__(parent)
        self.controller = controller

        topbar = ttk.Frame(self)
        topbar.pack(fill="x", padx=20, pady=(20, 10))

        title = ttk.Label(topbar, text="Fragen verwalten", style="Header.TLabel")
        title.pack(side="left")

        back_btn = ttk.Button(
            topbar,
            text="Zurück",
            command=lambda: controller.show_frame("StartPage")
        )
        back_btn.pack(side="right")

        card = ttk.Frame(self, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=20, pady=10)

        btn_bar = ttk.Frame(card, style="Card.TFrame")
        btn_bar.pack(fill="x", padx=20, pady=(20, 10))

        add_btn = ttk.Button(btn_bar, text="Neue Frage", style="Accent.TButton",
                             command=self.add_question)
        add_btn.pack(side="left")

        edit_btn = ttk.Button(btn_bar, text="Bearbeiten",
                              command=self.edit_selected)
        edit_btn.pack(side="left", padx=(10, 0))

        del_btn = ttk.Button(btn_bar, text="Löschen", style="Danger.TButton",
                             command=self.delete_selected)
        del_btn.pack(side="left", padx=(10, 0))

        self.tree = ttk.Treeview(
            card,
            columns=("id", "topic", "type", "text"),
            show="headings"
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("topic", text="Thema")
        self.tree.heading("type", text="Typ")
        self.tree.heading("text", text="Frage")
        self.tree.column("id", width=80)
        self.tree.column("topic", width=120)
        self.tree.column("type", width=80)
        self.tree.column("text", width=450)
        self.tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def on_show(self):
        self.refresh()

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for q in self.controller.store.list_questions():
            self.tree.insert("", "end", iid=q.id,
                             values=(q.id, q.topic, q.type, q.text))

    def _get_selected_id(self) -> str | None:
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Hinweis", "Bitte zuerst eine Frage auswählen.")
            return None
        return sel[0]

    def add_question(self):
        QuestionDialog.create_new(self.controller, self)
        self.refresh()

    def edit_selected(self):
        qid = self._get_selected_id()
        if not qid:
            return
        QuestionDialog.edit_existing(self.controller, self, qid)
        self.refresh()

    def delete_selected(self):
        qid = self._get_selected_id()
        if not qid:
            return
        if messagebox.askyesno("Bestätigen", "Frage wirklich löschen?"):
            self.controller.store.delete_question(qid)
            self.refresh()


# ---------- Dialog zum Fragen bearbeiten ----------

class QuestionDialog(tk.Toplevel):
    def __init__(self, controller: QuizApp, parent: ManageQuestionsPage, question: Question | None):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.question = question

        self.title("Frage bearbeiten" if question else "Neue Frage")
        self.configure(bg="#252526")
        self.resizable(False, False)

        self.topic_var = tk.StringVar(value=question.topic if question else "")
        self.type_var = tk.StringVar(value=question.type if question else "mc")
        self.text_var = tk.StringVar(value=question.text if question else "")
        self.options_var = tk.StringVar(
            value="; ".join(question.options) if question and question.options else ""
        )
        self.answer_var = tk.StringVar(
            value=str(question.answer) if question and question.answer is not None else ""
        )

        frame = ttk.Frame(self, style="Card.TFrame")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Thema
        ttk.Label(frame, text="Thema:").grid(row=0, column=0, sticky="w")
        topic_entry = ttk.Entry(frame, textvariable=self.topic_var, width=40)
        topic_entry.grid(row=0, column=1, sticky="we", pady=3)

        # Typ
        ttk.Label(frame, text="Fragetyp:").grid(row=1, column=0, sticky="w")
        type_combo = ttk.Combobox(
            frame,
            textvariable=self.type_var,
            values=["mc", "tf", "text"],
            state="readonly",
            width=10
        )
        type_combo.grid(row=1, column=1, sticky="w", pady=3)

        # Text
        ttk.Label(frame, text="Fragetext:").grid(row=2, column=0, sticky="nw")
        text_entry = ttk.Entry(frame, textvariable=self.text_var, width=60)
        text_entry.grid(row=2, column=1, sticky="we", pady=3)

        # Optionen (für MC)
        ttk.Label(frame, text="Optionen (bei MC, mit ';' trennen):").grid(row=3, column=0, sticky="nw")
        opt_entry = ttk.Entry(frame, textvariable=self.options_var, width=60)
        opt_entry.grid(row=3, column=1, sticky="we", pady=3)

        # Antwort
        ttk.Label(frame, text="Korrekte Antwort:").grid(row=4, column=0, sticky="w")
        ans_entry = ttk.Entry(frame, textvariable=self.answer_var, width=20)
        ans_entry.grid(row=4, column=1, sticky="w", pady=3)

        # Buttons
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.grid(row=5, column=0, columnspan=2, sticky="e", pady=(10, 0))

        save_btn = ttk.Button(btn_frame, text="Speichern", style="Accent.TButton",
                              command=self.on_save)
        save_btn.pack(side="right", padx=(0, 5))

        cancel_btn = ttk.Button(btn_frame, text="Abbrechen",
                                command=self.destroy)
        cancel_btn.pack(side="right")

        frame.columnconfigure(1, weight=1)
        topic_entry.focus()

    @classmethod
    def create_new(cls, controller: QuizApp, parent: ManageQuestionsPage):
        dlg = cls(controller, parent, None)
        parent.wait_window(dlg)

    @classmethod
    def edit_existing(cls, controller: QuizApp, parent: ManageQuestionsPage, qid: str):
        q = controller.store.get_question(qid)
        if not q:
            messagebox.showerror("Fehler", "Frage nicht gefunden.")
            return
        dlg = cls(controller, parent, q)
        parent.wait_window(dlg)

    def on_save(self):
        topic = self.topic_var.get().strip()
        qtype = self.type_var.get()
        text = self.text_var.get().strip()
        options_text = self.options_var.get().strip()
        answer_text = self.answer_var.get().strip()

        if not topic or not text:
            messagebox.showwarning("Hinweis", "Thema und Fragetext dürfen nicht leer sein.")
            return

        options: List[str] | None = None
        answer = None

        try:
       if qtype == "mc":
    options = [o.strip() for o in options_text.split(";") if o.strip()]
    if len(options) < 2:
        raise ValueError("Für MC-Fragen sind mindestens 2 Optionen nötig.")

    
    if answer_text.isdigit():
        answer = int(answer_text)
        if not (0 <= answer < len(options)):
            raise ValueError("Antwortindex liegt außerhalb des gültigen Bereichs.")
    else:
        
        try:
            answer = options.index(answer_text.strip())
        except ValueError:
            raise ValueError("Die korrekte Antwort muss entweder ein gültiger Index "
                             "oder exakt eine der angegebenen Optionen sein.")

            elif qtype == "tf":
                if answer_text.lower() not in ("t", "f", "true", "false", "wahr", "falsch"):
                    raise ValueError("Für TF-Fragen bitte 't'/'f' oder 'true'/'false' angeben.")
                answer = answer_text.lower() in ("t", "true", "wahr")
                else:  # text
        if not answer_text:
            raise ValueError("Für Textfragen wird eine Musterlösung benötigt.")
        answer = answer_text
        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
            return

        store = self.controller.store

        if self.question is None:
            q = Question(
                id=uid(),
                topic=topic,
                text=text,
                type=qtype,  # type: ignore
                options=options,
                answer=answer
            )
            store.add_question(q)
        else:
            store.update_question(
                self.question.id,
                topic=topic,
                text=text,
                type=qtype,
                options=options,
                answer=answer
            )

        self.destroy()
