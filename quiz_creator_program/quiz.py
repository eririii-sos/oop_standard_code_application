# Will contain quiz creator's data classes (Question, Quiz, etc.)

class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct

class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)