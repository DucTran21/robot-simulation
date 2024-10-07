from .tray_hole import Hole
import random

class Camera:
    def scan(self, tray):
        # Simulate item detection; randomly return items from tray
        items = tray.get_items()
        if items:
            # Detect up to 4 items and their positions
            detected_items = [(hole, hole.item_color) for hole in items]
            detected_items = random.sample(detected_items, min(len(detected_items), 4))
            return detected_items  # Return tuples of (hole, item_color)
        return []