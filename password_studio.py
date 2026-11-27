
import tkinter as tk
from tkinter import messagebox
import secrets
import string

# =========================================
# PASSWORD STUDIO
# Modern Password Generator
# =========================================

BG = "#101827"
CARD = "#1C293B"
ACCENT = "#38D6B0"
WHITE = "#F1F5F9"
GRAY = "#94A3B8"

root = tk.Tk()
root.title("Password Studio")
root.geometry("650x650")
root.configure(bg=BG)
root.resizable(False, False)

# ---------- FUNCTIONS ----------

def generate_password():
    length = length_var.get()

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += "!@#$%^&*()-_=+?"

    if not characters:
        messagebox.showwarning(
            "Ескерту",
            "Кем дегенде бір таңдау жасаңыз!"
        )
        return

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    update_strength(password)


def update_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+?" for c in password):
        score += 1

    if score <= 2:
        text = "Әлсіз"
        color = "#EF4444"
    elif score <= 4:
        text = "Орташа"
        color = "#F59E0B"
    else:
        text = "Күшті"
        color = ACCENT

    strength_label.config(
        text=f"Қауіпсіздік деңгейі: {text}",
        fg=color
    )


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Ескерту",
            "Алдымен құпиясөз жасаңыз!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Сәтті!",
        "Құпиясөз көшірілді!"
    )


def update_length(value):
    length_value.config(text=str(int(float(value))))


# ---------- HEADER ----------

header = tk.Frame(root, bg=BG)
header.pack(pady=(30, 10))

tk.Label(
    header,
    text="PASSWORD STUDIO",
    font=("Arial", 25, "bold"),
    fg=ACCENT,
    bg=BG
).pack()

tk.Label(
    header,
    text="Қауіпсіз құпиясөз генераторы",
    font=("Arial", 11),
    fg=GRAY,
    bg=BG
).pack(pady=7)


# ---------- MAIN CARD ----------

card = tk.Frame(
    root,
    bg=CARD,
    padx=30,
    pady=25
)
card.pack(padx=35, fill="both", expand=True)

tk.Label(
    card,
    text="Сіздің құпиясөзіңіз",
    font=("Arial", 14, "bold"),
    fg=WHITE,
    bg=CARD
).pack(anchor="w", pady=(0, 12))

password_entry = tk.Entry(
    card,
    font=("Consolas", 16),
    justify="center",
    bg="#26364B",
    fg=ACCENT,
    insertbackground=WHITE,
    relief="flat",
    readonlybackground="#26364B",
    state="readonly"
)
password_entry.pack(fill="x", ipady=13)

# ---------- STRENGTH ----------

strength_label = tk.Label(
    card,
    text="Қауіпсіздік деңгейі: Әлі жасалмады",
    font=("Arial", 10, "bold"),
    fg=GRAY,
    bg=CARD
)
strength_label.pack(anchor="w", pady=15)

# ---------- LENGTH ----------

tk.Label(
    card,
    text="Құпиясөз ұзындығы",
    font=("Arial", 12, "bold"),
    fg=WHITE,
    bg=CARD
).pack(anchor="w", pady=(8, 5))

length_var = tk.IntVar(value=16)

length_value = tk.Label(
    card,
    text="16",
    font=("Arial", 13, "bold"),
    fg=ACCENT,
    bg=CARD
)
length_value.pack(anchor="e")

length_slider = tk.Scale(
    card,
    from_=6,
    to=40,
    orient="horizontal",
    variable=length_var,
    command=update_length,
    bg=CARD,
    fg=WHITE,
    troughcolor="#334155",
    activebackground=ACCENT,
    highlightthickness=0,
    showvalue=False
)
length_slider.pack(fill="x")

# ---------- OPTIONS ----------

tk.Label(
    card,
    text="Құпиясөз параметрлері",
    font=("Arial", 12, "bold"),
    fg=WHITE,
    bg=CARD
).pack(anchor="w", pady=(18, 10))

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

options = [
    ("Бас әріптер (A-Z)", upper_var),
    ("Кіші әріптер (a-z)", lower_var),
    ("Сандар (0-9)", number_var),
    ("Арнайы символдар (!@#)", symbol_var)
]

for text, variable in options:
    tk.Checkbutton(
        card,
        text=text,
        variable=variable,
        font=("Arial", 10),
        fg=WHITE,
        bg=CARD,
        activebackground=CARD,
        activeforeground=ACCENT,
        selectcolor="#26364B",
        cursor="hand2"
    ).pack(anchor="w", pady=3)

# ---------- BUTTONS ----------

button_frame = tk.Frame(card, bg=CARD)
button_frame.pack(fill="x", pady=(22, 5))

tk.Button(
    button_frame,
    text="✦  Құпиясөз жасау",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    activebackground="#24B895",
    relief="flat",
    cursor="hand2"
).pack(fill="x", ipady=12, pady=5)

tk.Button(
    button_frame,
    text="▣  Көшіру",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#334155",
    fg=WHITE,
    activebackground="#475569",
    relief="flat",
    cursor="hand2"
).pack(fill="x", ipady=10, pady=5)

# ---------- FOOTER ----------

tk.Label(
    root,
    text="PASSWORD STUDIO  •  PYTHON PROJECT",
    font=("Arial", 9),
    fg=GRAY,
    bg=BG
).pack(pady=15)

root.mainloop()
