#!/usr/bin/env python3
"""
Calculator — GUI Edition
Built with Tkinter (Python's built-in GUI library).

Layout:
  [ C  ] [ ±  ] [ %  ] [ ÷  ]
  [ 7  ] [ 8  ] [ 9  ] [ ×  ]
  [ 4  ] [ 5  ] [ 6  ] [ -  ]
  [ 1  ] [ 2  ] [ 3  ] [ +  ]
  [  0     ] [ .  ] [ =  ]
"""

import tkinter as tk
from tkinter import font as tkfont


# ── Constants ─────────────────────────────────────────────────────────────

BG = "#1e1e2e"
DISPLAY_BG = "#2a2a3e"
FG = "#cdd6f4"

BTN_DIGIT = "#313244"
BTN_OP = "#cba6f7"       # purple — operators
BTN_EQUAL = "#a6e3a1"    # green  — equals
BTN_CLEAR = "#f38ba8"    # red    — clear / special
BTN_HOV = "#45475a"

FONT_DISPLAY = ("Helvetica", 28, "bold")
FONT_BTN = ("Helvetica", 16)


# ── Calculator logic ──────────────────────────────────────────────────────

class Calculator:
    """Holds state and evaluates expressions."""

    def __init__(self):
        self.expression = ""
        self.reset_next = False  # clear display after result

    def push(self, value: str) -> str:
        """Append a character and return the updated expression."""
        if self.reset_next and value not in ("C", "="):
            if value in ("+", "-", "×", "÷", "%"):
                pass  # chain operators on the result
            else:
                self.expression = ""
            self.reset_next = False

        if value == "C":
            self.expression = ""
            self.reset_next = False
        elif value == "←":
            self.expression = self.expression[:-1]
        elif value == "±":
            self._toggle_sign()
        elif value == "=":
            self._evaluate()
        else:
            self.expression += value

        return self.expression

    def _toggle_sign(self):
        try:
            result = -float(self._display_expr())
            self.expression = self._fmt(result)
        except (ValueError, SyntaxError):
            pass

    def _evaluate(self):
        try:
            result = eval(self._display_expr())  # noqa: S307
            self.expression = self._fmt(result)
            self.reset_next = True
        except Exception:
            self.expression = "Error"
            self.reset_next = True

    def _display_expr(self) -> str:
        """Replace display symbols with Python operators."""
        return self.expression.replace("×", "*").replace("÷", "/")

    @staticmethod
    def _fmt(value: float) -> str:
        """Format a float: show int when possible."""
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)


# ── GUI ───────────────────────────────────────────────────────────────────


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.calc = Calculator()
        self._build_ui()
        self.eval("tk::PlaceWindow . center")

    # ── UI construction ───────────────────────────────────────────────────

    def _build_ui(self):
        self._build_display()
        self._build_buttons()

    def _build_display(self):
        frame = tk.Frame(self, bg=DISPLAY_BG, pady=16, padx=16)
        frame.pack(fill="x")
        self.display = tk.Label(
            frame, text="0", anchor="e",
            bg=DISPLAY_BG, fg=FG,
            font=FONT_DISPLAY, width=14
        )
        self.display.pack(fill="x")

    def _build_buttons(self):
        grid = tk.Frame(self, bg=BG)
        grid.pack(padx=10, pady=10)

        # (label, row, col, colspan, bg-color)
        layout = [
            ("C",  0, 0, 1, BTN_CLEAR),
            ("±",  0, 1, 1, BTN_CLEAR),
            ("%",  0, 2, 1, BTN_CLEAR),
            ("÷",  0, 3, 1, BTN_OP),
            ("7",  1, 0, 1, BTN_DIGIT),
            ("8",  1, 1, 1, BTN_DIGIT),
            ("9",  1, 2, 1, BTN_DIGIT),
            ("×",  1, 3, 1, BTN_OP),
            ("4",  2, 0, 1, BTN_DIGIT),
            ("5",  2, 1, 1, BTN_DIGIT),
            ("6",  2, 2, 1, BTN_DIGIT),
            ("-",  2, 3, 1, BTN_OP),
            ("1",  3, 0, 1, BTN_DIGIT),
            ("2",  3, 1, 1, BTN_DIGIT),
            ("3",  3, 2, 1, BTN_DIGIT),
            ("+",  3, 3, 1, BTN_OP),
            ("0",  4, 0, 2, BTN_DIGIT),
            (".",  4, 2, 1, BTN_DIGIT),
            ("=",  4, 3, 1, BTN_EQUAL),
        ]

        btn_font = tkfont.Font(family="Helvetica", size=16)

        for text, row, col, span, color in layout:
            fg = BG if color != BTN_DIGIT else FG
            btn = tk.Button(
                grid, text=text,
                bg=color, fg=fg,
                activebackground=BTN_HOV, activeforeground=FG,
                font=btn_font, relief="flat", bd=0,
                width=4 * span, height=2, cursor="hand2",
                command=lambda t=text: self._on_press(t)
            )
            btn.grid(
                row=row, column=col, columnspan=span,
                padx=4, pady=4, sticky="nsew"
            )
            btn.bind(
                "<Enter>",
                lambda e, b=btn: b.config(bg=BTN_HOV)
            )
            btn.bind(
                "<Leave>",
                lambda e, b=btn, c=color: b.config(bg=c)
            )

    # ── Event handler ─────────────────────────────────────────────────────

    def _on_press(self, value: str):
        result = self.calc.push(value)
        self.display.config(text=result if result else "0")


if __name__ == "__main__":
    App().mainloop()
