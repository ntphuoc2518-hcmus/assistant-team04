# src/assistant/rules.py
import re

offices = {
    "training": {"name": "Training Office", "room": "1.101", "hours": "08:00-17:00"},
    "it": {"name": "IT Support Office", "room": "2.202", "hours": "08:30-16:30"},
}

def reply(text: str) -> str:
    tokens = set(re.findall(r"\w+", text.lower()))
    for key, row in offices.items():
        # khớp nguyên từ, hoặc gõ dở tên (vd "train" -> "training", tối thiểu 4 ký tự)
        if key in tokens or any(key.startswith(t) for t in tokens if len(t) >= 4):
            return f"{row['name']}: room {row['room']}, open {row['hours']}."
    return "Sorry, I couldn't find that office."