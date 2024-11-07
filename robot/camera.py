from .tray_hole import Hole
import random

class Camera:
    def scan(self, tray):
        # Get all filled holes from the tray along with their positions
        items_with_positions = [(index, hole) for index, hole in enumerate(tray.holes) if hole.is_filled()]

        if items_with_positions:
            # Detect up to 6 items; ensure these are Hole objects with positions
            detected_items = random.sample(items_with_positions, min(len(items_with_positions), 6))
            return detected_items  # Return list of (position, Hole object) tuples
        return []