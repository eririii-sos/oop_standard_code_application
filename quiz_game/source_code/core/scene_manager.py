# core/scene_manager.py

class SceneManager:
    def __init__(self, screen, initial_scene):
        self.screen = screen
        self.current_scene = initial_scene

    def go_to(self, scene):
        self.current_scene = scene

    def handle_event(self, event):
        self.current_scene.handle_event(event)

    def update(self, dt):
        self.current_scene.update(dt)

    def render(self):
        self.current_scene.render()