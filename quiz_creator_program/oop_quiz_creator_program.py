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
                file.write(question.format_file() + "\n")

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

    @staticmethod
    def prompt(text, color=Fore.YELLOW):
        return input(color + text + Fore.RESET)

    @staticmethod
    def error(message):
        print(Fore.RED + message)

    @staticmethod
    def highlight(message):
        print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + message)

def main():
    UI.banner()
    filename = "quiz_creator_questions.txt"

    choice = UI.prompt("\nSelect an option: ").strip()
    if choice != "1":
        print("\nExiting the program... Goodbye!")
        return
    
    print("\nStarting the program...")

    quiz = Quiz(filename)

    while True:
        UI.highlight("\nAdd a new question")
        question_text = UI.prompt("Question: ")

        options = {}
        for key in ['a', 'b', 'c', 'd']:
            options[key] = UI.prompt(f"Option {key}: ")

        correct = ""
        while correct not in options:
            correct = UI.prompt("\nCorrect answer (a/b/c/d): ").lower()
            if correct not in options:
                UI.error("Invalid input! Please only enter a, b, c, or d.")

        quiz.add_question(Question(question_text, options, correct))

        again = UI.prompt("\nAdd another question? (yes/no): ").strip().lower()
        if again != "yes":
            break

        quiz.save()
        print(f"\n 🎉 All done! Your questions are saved in '{filename}'")

if __name__ == "__main__":
    main()