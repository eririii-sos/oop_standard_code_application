# (Optional) Install library/libraries that you'll use in the program.

# Import dependencies
from colorama import init, Fore, Style, Back
import os

# Initialize colorama
init(autoreset=True)

# Custom prompt format
def user_input(prompt, color=Fore.YELLOW):
    return input(color + prompt + Fore.RESET)

# Quiz creator menu banner
def menu_banner():
    os.system("cls" if os.name == "nt" else "clear")
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

# Ask user for the question
def ask_question():
    print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + "\nAdd a new question")
    question = user_input("Question: ")
    answer_options = {opt: user_input(f"Option {opt}: ") for opt in ['a', 'b', 'c', 'd']}

    # Ask user for the correct answer
    correct = ""
    while correct not in answer_options:
        correct = user_input("\nCorrect answer (a/b/c/d): ").lower()
        if correct not in answer_options: # Error handling for invalid input
            print("Invalid input! Please only enter a, b, c, or d.")
    
    return question, answer_options, correct

# Write and save all the input inside the text file
def save_question(file, question, answer_options, correct):
    file.write(f"Question: {question}\n")
    for key, val in answer_options.items():
        file.write(f"   {key}) {val}\n")
    file.write(f"Correct Answer: {correct}\n")
    file.write("-" * 50 + "\n")

def quiz_creator():
    menu_banner()
    file_name = "quiz_creator_questions.txt" # Assign a text file 

    # Get user's choice 
    option = user_input("\nSelect an option: ").strip()

    if option == "1":
        print("\nStarting the program...")

    else:
        print("\nExiting the program... Goodbye!")
        return
    
    # Open text file and allow input to be saved
    with open(file_name, "a") as file:
        while True:   
            q, opts, ans = ask_question()
            save_question(file, q, opts, ans)

            if user_input("\nAdd another question? (yes/no): ").strip().lower() != "yes":
                print(f"\n 🎉 All done! Your questions are saved in '{file_name}'")
                break

if __name__ == "__main__":
    quiz_creator()