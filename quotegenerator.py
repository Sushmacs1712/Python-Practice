mood = input("How are you feeling today? ").lower()

quotes = {
    "happy": "Keep shining!",
    "sad": "Tough times don't last.",
    "tired": "Rest if you must, but don't quit.",
    "confused": "One step at a time."
}

print(quotes.get(mood, "Every day is a new beginning."))