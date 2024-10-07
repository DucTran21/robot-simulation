from .hole import Hole

class Tray:
    def __init__(self, total_holes):
        self.hole = [Hole() for _ in range(total_holes)]

    def fill_holes(self, items):
        for item in items:
            for hole in self.hole:
                if not hole.is_filled():
                    hole.fill(item)
                    break  # Exit after filling one hole