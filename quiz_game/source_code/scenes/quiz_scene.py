# scenes/quiz_scene.py

import os
from settings import ASSET_PATH

QUIZ_FILE_PATH = os.path.join(ASSET_PATH, "quiz_creator_questions.txt")

class QuizScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen