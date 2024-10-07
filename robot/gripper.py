class Gripper:
    def __init__(self):
        self.item = None

    def pick(self, hole):
        if hole and not hole.is_filled():
            self.item = hole
            print(f"Picked {hole.item_color} item.")

    def release(self):
        if self.item:
            print(f"Released {self.item.item_color} item.")
            self.item = None

    def has_item(self):
        return self.item is not None