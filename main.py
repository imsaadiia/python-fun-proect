import tkinter as tk
from tkinter import messagebox
import random

# ------------------ Mood Data ------------------
moods = {
    "happy": {
        "color": "#FFF3B0",
        "emoji": "😊",
        "quotes": [
            "Happiness looks good on you.",
            "Stay light, stay kind.",
            "Joy is a quiet strength."
        ],
        "advice": "Celebrate the moment and spread the positivity."
    },
    "sad": {
        "color": "#D6E4F0",
        "emoji": "😔",
        "quotes": [
            "Even the sky cries sometimes.",
            "This too shall pass.",
            "Soft hearts feel deeply."
        ],
        "advice": "Take a deep breath. You are not alone."
    },
    "stressed": {
        "color": "#FADADD",
        "emoji": "😣",
        "quotes": [
            "Pause. You are doing your best.",
            "Calm is a superpower.",
            "Breathe in peace, breathe out worry."
        ],
        "advice": "Slow down. One thing at a time."
    },
    "confident": {
        "color": "#D5F5E3",
        "emoji": "😎",
        "quotes": [
            "Confidence is silent power.",
            "You belong where you stand.",
            "Grace follows self-belief."
        ],
        "advice": "Use your confidence wisely and kindly."
    },
    "love": {
        "color": "#FFE4E1",
        "emoji": "❤️",
        "quotes": [
            "Love is calm, not loud.",
            "Where there is love, there is warmth.",
            "Love begins within."
        ],
        "advice": "Appreciate the feeling and express it gently."
    },
    "lonely": {
        "color": "#E8EAF6",
        "emoji": "🥺",
        "quotes": [
            "Loneliness teaches self-connection.",
            "You are more seen than you think.",
            "Quiet moments shape strong souls."
        ],
        "advice": "Reach out or spend time doing something you love."
    }
}

# ------------------ AI-like Mood Detection ------------------
def detect_mood_from_text(text):
    text = text.lower()

    mood_keywords = {
        "happy": ["happy", "joy", "smile", "excited", "good"],
        "sad": ["sad", "down", "cry", "hurt", "upset"],
        "stressed": ["stress", "tired", "pressure", "anxious", "overwhelmed"],
        "confident": ["confident", "strong", "proud", "bold"],
        "love": ["love", "affection", "care", "crush", "romantic"],
        "lonely": ["lonely", "alone", "empty", "isolated"]
    }

    for mood, keywords in mood_keywords.items():
        for word in keywords:
            if word in text:
                return mood

    return None

# ------------------ Main Logic ------------------
def analyze_mood():
    user_input = mood_entry.get().strip()

    if not user_input:
        messagebox.showwarning("Empty Input", "Please express how you are feeling.")
        return

    detected_mood = detect_mood_from_text(user_input)

    if detected_mood and detected_mood in moods:
        data = moods[detected_mood]
        window.configure(bg=data["color"])
        title.config(bg=data["color"])
        subtitle.config(bg=data["color"])
        result_label.config(
            text=f"{data['emoji']}  {random.choice(data['quotes'])}\n\nAdvice: {data['advice']}",
            bg=data["color"]
        )
    else:
        messagebox.showinfo(
            "Mood Unclear",
            "I couldn't clearly detect your mood.\nTry expressing it differently."
        )

# ------------------ GUI Setup ------------------
window = tk.Tk()
window.title("MoodMirror")
window.geometry("420x320")
window.configure(bg="#F7F7F7")
window.resizable(False, False)

title = tk.Label(
    window,
    text="MoodMirror",
    font=("Segoe UI", 18, "bold"),
    bg="#F7F7F7"
)
title.pack(pady=10)

subtitle = tk.Label(
    window,
    text="Express freely. I'll understand.",
    font=("Segoe UI", 10),
    bg="#F7F7F7"
)
subtitle.pack()

mood_entry = tk.Entry(
    window,
    font=("Segoe UI", 12),
    justify="center",
    width=35
)
mood_entry.pack(pady=15)

analyze_btn = tk.Button(
    window,
    text="Analyze Mood",
    font=("Segoe UI", 11),
    command=analyze_mood,
    bg="#333333",
    fg="white",
    padx=10,
    pady=5
)
analyze_btn.pack()

result_label = tk.Label(
    window,
    text="",
    font=("Segoe UI", 11),
    wraplength=350,
    justify="center",
    bg="#F7F7F7"
)
result_label.pack(pady=20)

window.mainloop()
