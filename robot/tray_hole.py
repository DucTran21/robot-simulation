class Hole:
    def __init__(self):
        self.filled = False
        self.item_color = None

    def fill(self):
        self.filled = True

    def is_filled(self):
        return self.filled