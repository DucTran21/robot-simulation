from .tray_hole import Hole
import random

class Tray:
    def __init__(self, size):
        self.holes = [Hole() for _ in range(size)]
        self.populate_items(size)

    def populate_items(self, count):
        # Randomly fill some holes with items
        for _ in range(random.randint(1, count)):
            item_index = random.randint(0, count - 1)
            if not self.holes[item_index].is_filled():
                self.holes[item_index].fill()
                self.holes[item_index].item_color = "gold-yellow"  # Example color

    def get_items(self):
        return [hole for hole in self.holes if hole.is_filled()]