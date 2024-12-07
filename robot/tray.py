import time  # Import the time module for adding delays
import random
from robot.tray_hole import Hole
class Tray:
    def __init__(self, size, filled=True):
        self.holes = [Hole() for _ in range(size)]
        if filled:
            self.populate_items(size)

    def populate_items(self, count):
        # Randomly fill some holes with items
        for _ in range(random.randint(1, count)):
            item_index = random.randint(0, count - 1)
            if not self.holes[item_index].is_filled():
                self.holes[item_index].fill()
                self.holes[item_index].item_color = "gold-yellow"

    def shake(self):
        # Simulate the time taken to shake the tray
        print("Shaking tray...")
        time.sleep(2)  # Add a delay to represent the shaking action
        random.shuffle(self.holes)
        print("Shaking complete.")

    def is_full(self):
        return all(hole.is_filled() for hole in self.holes)

    def get_items(self):
        return [hole for hole in self.holes if hole.is_filled()]

    def remove_item(self, index):
        # Set hole at index as empty to simulate item removal
        if index < len(self.holes) and self.holes[index].is_filled():
            self.holes[index].empty()  # Define empty() in Hole to clear it