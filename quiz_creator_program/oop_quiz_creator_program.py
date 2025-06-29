# Import os module and necessities from coloroma library
import os
from colorama import init, Fore, Style, Back

# Initialize colorama
init(autoreset=True)

class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct

    def format_file(self):
        lines = [f"Question: {self.text}"]
        for key, val in self.options.items():
            lines.append(f" {key}) {val}")
        lines.append(f"Correct Answer: {self.correct}")
        lines.append("-" * 50)
        return "\n".join(lines)

class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)