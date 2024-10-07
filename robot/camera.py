class Camera:
    def scan_tray(self, tray):
        # Simulate scanning the tray for items based on color
        detected_items = []  # Replace this with actual detection logic

        # Here you could implement color detection logic
        for hole in tray.holes:
            if hole.is_filled():  # Check if the hole has an item
                detected_items.append(hole.item)

        return detected_items