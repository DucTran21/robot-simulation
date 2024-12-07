import time  # Import the time module for adding delays

class Gripper:
    def __init__(self):
        self.item = None

    def pick(self, hole):
        if hole and hole.is_filled():  # Only pick filled holes
            time.sleep(1)  # Simulate time to pick up the item (e.g., 1 second)
            self.item = hole
            print(f"Picked {hole.item_color} item.")

    def release(self):
        if self.item:
            time.sleep(1)  # Simulate time to release the item (e.g., 1 second)
            print(f"Released {self.item.item_color} item.")
            self.item = None

    def has_item(self):
        return self.item is not None