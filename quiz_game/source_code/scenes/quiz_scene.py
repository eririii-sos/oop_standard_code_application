# scenes/quiz_scene.py

import pygame
import random
import os
from settings import ASSET_PATH, QUIZ_FONT_SIZE, QUESTION_TIMER, WIDTH, HEIGHT

QUIZ_FILE_PATH = os.path.join(ASSET_PATH, "quiz_creator_questions.txt")

class QuizScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, QUIZ_FONT_SIZE)

        self.background = pygame.transform.scale(
            pygame.image.load(ASSET_PATH + "quiz_background.png"), (WIDTH, HEIGHT)
        )

        self.questions = self.load_questions()
        if not self.questions:
            print("ERROR: No quiz questions loaded!")        
        random.shuffle(self.questions)

        self.current_question = 0
        self.score = 0

        self.option_boxes = []
        self.generate_option_boxes()

        self.timer = QUESTION_TIMER
        self.clock = pygame.time.Clock()

    def load_questions(self):
        if not os.path.exists(QUIZ_FILE_PATH):
            print(f"Quiz file not found: {QUIZ_FILE_PATH}")
            return []
        
        with open(QUIZ_FILE_PATH, 'r') as file:
            content = file.read().strip()

        raw_blocks = content.split("--------------------------------------------------")
        questions = []

        for block in raw_blocks:
            lines = block.strip().splitlines()
            if not lines:
                continue

            q_data = {
                "question": "",
                "options": [],
                "answer": ""
            }

            for line in lines:
                line = line.strip()
                if line.startswith("Question:"):
                    q_data["question"] = line.replace("Question:", "").strip()
                elif line.startswith(("a)", "b)", "c)", "d)")):
                    q_data["options"].append(line)
                elif line.startswith("Correct Answer:"):
                    q_data["answer"] = line[-1].lower()

            if len(q_data["options"]) == 4 and q_data["answer"] in ['a', 'b', 'c', 'd']:
                questions.append(q_data)
            else:
                print(f"Skipped malformed question block:\n{block}\n")

        return questions
    
    def generate_option_boxes(self):
        self.option_boxes.clear()
        y_start = 180
        for i in range(4):
            box = pygame.Rect(580, y_start + i * 70, 250, 50)
            self.option_boxes.append(box)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for i, box in enumerate(self.option_boxes):
                if box.collidepoint(pos):
                    self.check_answer(i)

    def check_answer(self, selected_index):
        quiz = self.questions[self.current_question]
        correct_index = ord(quiz["answer"]) - ord('a')

        if selected_index == correct_index:
            self.score += 1

        self.current_question += 1

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.current_question += 1

    def render(self):
        self.screen.blit(self.background, (0, 0))

        if self.current_question < len(self.questions):
            quiz = self.questions[self.current_question]
            question_text = quiz["question"]

            text_surface = self.font.render(question_text, True, (0, 0, 0))
            self.screen.blit(text_surface, (WIDTH - 480, 130))

            for i, option in enumerate(quiz["options"]):
                if i >= len(self.option_boxes):
                    break    
                pygame.draw.rect(self.screen, (80, 180, 80), self.option_boxes[i])
                option_text = self.font.render(option, True, (255, 255, 255))
                self.screen.blit(option_text, (self.option_boxes[i].x + 20, self.option_boxes[i].y + 10))