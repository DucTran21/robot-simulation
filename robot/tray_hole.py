class Hole:
    def __init__(self):
        self.filled = False
        self.item_color = None

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = True
        self.item_color = "gold-yellow"

    def empty(self):
        self.filled = False
        self.item_color = None