#!/usr/bin/env python3
"""
Rock Paper Scissors: Lizard Spock — GUI Edition
Built with Tkinter (Python's built-in GUI library).

Rules:
  Scissors cuts Paper       | Paper covers Rock
  Rock crushes Lizard       | Lizard poisons Spock
  Spock smashes Scissors    | Scissors decapitates Lizard
  Lizard eats Paper         | Paper disproves Spock
  Spock vaporizes Rock      | Rock crushes Scissors
"""

import tkinter as tk
from tkinter import font as tkfont
import random

# ── Game logic ────────────────────────────────────────────────────────────

CHOICES = ["✊ Rock", "✋ Paper", "✌️ Scissors", "🦎 Lizard", "🖖 Spock"]

# Maps (winner, loser) → verb describing what winner does to loser
BEATS = {
    ("✊ Rock", "✌️ Scissors"): "crushes",
    ("✊ Rock", "🦎 Lizard"): "crushes",
    ("✋ Paper", "✊ Rock"): "covers",
    ("✋ Paper", "🖖 Spock"): "disproves",
    ("✌️ Scissors", "✋ Paper"): "cuts",
    ("✌️ Scissors", "🦎 Lizard"): "decapitates",
    ("🦎 Lizard", "🖖 Spock"): "poisons",
    ("🦎 Lizard", "✋ Paper"): "eats",
    ("🖖 Spock", "✊ Rock"): "vaporizes",
    ("🖖 Spock", "✌️ Scissors"): "smashes",
}


def resolve(player: str, computer: str) -> tuple[str, str]:
    """Return (outcome, description). outcome is 'win', 'lose', or 'tie'."""
    if player == computer:
        return "tie", "It's a tie!"
    if (player, computer) in BEATS:
        verb = BEATS[(player, computer)]
        return "win", f"{player} {verb} {computer} — You win! 🎉"
    verb = BEATS[(computer, player)]
    return "lose", f"{computer} {verb} {player} — CPU wins! 🤖"


# ── GUI ───────────────────────────────────────────────────────────────────


class App(tk.Tk):
    BG = "#1e1e2e"
    PANEL_BG = "#2a2a3e"
    ACCENT = "#cba6f7"    # purple
    WIN_CLR = "#a6e3a1"   # green
    LOSE_CLR = "#f38ba8"  # red
    TIE_CLR = "#f9e2af"   # yellow
    FG = "#cdd6f4"
    BTN_BG = "#313244"
    BTN_HOV = "#45475a"

    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors: Lizard Spock")
        self.resizable(False, False)
        self.configure(bg=self.BG)

        self.player_score = 0
        self.cpu_score = 0
        self.ties = 0

        self._build_ui()
        self.eval("tk::PlaceWindow . center")  # center on screen

    # ── UI construction ───────────────────────────────────────────────────

    def _build_ui(self):
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        result_font = tkfont.Font(family="Helvetica", size=13)
        score_font = tkfont.Font(family="Helvetica", size=12)
        vs_font = tkfont.Font(family="Helvetica", size=28)

        # Title
        tk.Label(
            self, text="Rock · Paper · Scissors · Lizard · Spock",
            bg=self.BG, fg=self.ACCENT, font=title_font, pady=16
        ).pack()

        # VS display row
        vs_frame = tk.Frame(self, bg=self.BG)
        vs_frame.pack(pady=4)

        lf = tk.Frame(vs_frame, bg=self.PANEL_BG, bd=0, relief="flat",
                      padx=20, pady=12)
        lf.grid(row=0, column=0, padx=10)
        tk.Label(lf, text="You", bg=self.PANEL_BG, fg=self.FG,
                 font=score_font).pack()
        self.player_lbl = tk.Label(
            lf, text="❓", bg=self.PANEL_BG, fg=self.FG, font=vs_font
        )
        self.player_lbl.pack()

        vs_font_small = tkfont.Font(
            family="Helvetica", size=16, weight="bold"
        )
        tk.Label(
            vs_frame, text="VS", bg=self.BG, fg=self.ACCENT,
            font=vs_font_small
        ).grid(row=0, column=1, padx=14)

        rf = tk.Frame(vs_frame, bg=self.PANEL_BG, bd=0, relief="flat",
                      padx=20, pady=12)
        rf.grid(row=0, column=2, padx=10)
        tk.Label(rf, text="CPU", bg=self.PANEL_BG, fg=self.FG,
                 font=score_font).pack()
        self.cpu_lbl = tk.Label(
            rf, text="❓", bg=self.PANEL_BG, fg=self.FG, font=vs_font
        )
        self.cpu_lbl.pack()

        # Result message
        self.result_lbl = tk.Label(
            self, text="Choose your weapon!",
            bg=self.BG, fg=self.FG, font=result_font, pady=10
        )
        self.result_lbl.pack()

        # Choice buttons
        btn_frame = tk.Frame(self, bg=self.BG)
        btn_frame.pack(pady=6)
        btn_font = tkfont.Font(family="Helvetica", size=12)
        for choice in CHOICES:
            btn = tk.Button(
                btn_frame, text=choice, width=14,
                bg=self.BTN_BG, fg=self.FG,
                activebackground=self.BTN_HOV, activeforeground=self.FG,
                relief="flat", bd=0, font=btn_font, cursor="hand2", pady=8,
                command=lambda c=choice: self._play(c)
            )
            btn.pack(side="left", padx=6)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.BTN_HOV))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.BTN_BG))

        # Score board
        score_frame = tk.Frame(self, bg=self.PANEL_BG, padx=20, pady=10)
        score_frame.pack(pady=14, ipadx=10)

        big_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        for col, label in enumerate(["You", "Ties", "CPU"]):
            tk.Label(
                score_frame, text=label, bg=self.PANEL_BG,
                fg=self.ACCENT, font=score_font
            ).grid(row=0, column=col * 2, padx=18)

        self.ps_lbl = tk.Label(
            score_frame, text="0", bg=self.PANEL_BG,
            fg=self.WIN_CLR, font=big_font
        )
        self.ps_lbl.grid(row=1, column=0, padx=18)

        self.ts_lbl = tk.Label(
            score_frame, text="0", bg=self.PANEL_BG,
            fg=self.TIE_CLR, font=big_font
        )
        self.ts_lbl.grid(row=1, column=2, padx=18)

        self.cs_lbl = tk.Label(
            score_frame, text="0", bg=self.PANEL_BG,
            fg=self.LOSE_CLR, font=big_font
        )
        self.cs_lbl.grid(row=1, column=4, padx=18)

        # Reset button
        tk.Button(
            self, text="Reset Scores", bg=self.BTN_BG, fg=self.FG,
            activebackground=self.BTN_HOV, activeforeground=self.FG,
            relief="flat", bd=0, font=score_font, cursor="hand2",
            pady=6, padx=12, command=self._reset
        ).pack(pady=(0, 16))

    # ── Game actions ──────────────────────────────────────────────────────

    @staticmethod
    def _emoji(choice: str) -> str:
        return choice.split()[0]

    def _play(self, player_choice: str):
        cpu_choice = random.choice(CHOICES)
        outcome, message = resolve(player_choice, cpu_choice)

        self.player_lbl.config(text=self._emoji(player_choice))
        self.cpu_lbl.config(text=self._emoji(cpu_choice))

        color_map = {"win": self.WIN_CLR, "lose": self.LOSE_CLR,
                     "tie": self.TIE_CLR}
        self.result_lbl.config(text=message, fg=color_map[outcome])

        if outcome == "win":
            self.player_score += 1
        elif outcome == "lose":
            self.cpu_score += 1
        else:
            self.ties += 1

        self.ps_lbl.config(text=str(self.player_score))
        self.cs_lbl.config(text=str(self.cpu_score))
        self.ts_lbl.config(text=str(self.ties))

    def _reset(self):
        self.player_score = self.cpu_score = self.ties = 0
        self.ps_lbl.config(text="0")
        self.cs_lbl.config(text="0")
        self.ts_lbl.config(text="0")
        self.player_lbl.config(text="❓")
        self.cpu_lbl.config(text="❓")
        self.result_lbl.config(text="Choose your weapon!", fg="#cdd6f4")


if __name__ == "__main__":
    App().mainloop()
