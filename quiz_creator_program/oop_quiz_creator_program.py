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

    def save(self):
        with open(self.filename, "a") as file:
            for question in self.questions:
                file.write(question.format_for_file() + "\n")

class UI:
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def banner():
        UI.clear_screen()
        print("=" * 50)
        print("|" + " " * 48 + "|")
        print("|" + " " * 8 +
            f"{Fore.YELLOW}{Style.BRIGHT}🧠 WELCOME TO THE QUIZ CREATOR 🧠{Fore.RESET}" + " " * 7 + "|")
        print("|" + " " * 48 + "|")
        print("|" + " " * 17 +
            f"Press {Fore.GREEN}{Style.BRIGHT}1{Fore.RESET} to {Fore.GREEN}{Style.BRIGHT}START{Fore.RESET}" + " " * 15 + "|")
        print("|" + " " * 17 +
            f"Press {Fore.RED}{Style.BRIGHT}2{Fore.RESET} to {Fore.RED}{Style.BRIGHT}EXIT{Fore.RESET}" + " " * 16 + "|")
        print("|" + " " * 48 + "|")
        print("=" * 50)