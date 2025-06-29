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