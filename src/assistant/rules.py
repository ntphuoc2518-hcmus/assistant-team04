"""Rule-based reply logic for Smart Virtual Assistant."""

import re

# Mapping of known offices to room numbers
OFFICE_LOCATIONS = {
    "training office": "I.101",
    "phòng đào tạo": "B.02",
    "trạm y tế": "E.02",
}

GREETING_KEYWORDS = {"hi", "hello", "hey", "chào"}
HELP_KEYWORDS = {"help", "trợ giúp", "commands"}


def reply(question: str) -> str:
    """Process a user question and return a rule-based response.

    Rules handled:
    - Empty or whitespace query: Prompt user to type a question.
    - Office inquiries: Return office location room code (e.g., I.101).
    - Greetings: Return friendly greeting containing 'Hello'.
    - Help: Return list of available capabilities.
    - Unknown queries: Return fallback message containing 'don't know'.
    """
    if not question or not question.strip():
        return "Please type a question."

    normalized = question.strip().lower()

    # Check for help command
    words = set(re.findall(r"\b\w+\b", normalized))
    if normalized in HELP_KEYWORDS or normalized == "help":
    	return "I can help you lookup office locations and answer general greetings."

    # Check for office lookup
    for office_name, room in OFFICE_LOCATIONS.items():
        if office_name in normalized:
            return f"The {office_name.title()} is in room {room}."

    # Check for greeting
    if words.intersection(GREETING_KEYWORDS):
        return "Hello! How can I assist you today?"

    # Fallback for unrecognized questions: explain supported topics and offer an example.
    return (
        "I am sorry, but I don't know the answer to that. "
        "I can help with office locations. "
        "Try asking 'Where is the Training Office?'"
    )