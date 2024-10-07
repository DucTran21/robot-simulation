from .tray import Tray
from .gripper import Gripper
from .camera import Camera

class Robot:
    def __init__(self):
        self.tray1 = Tray(24)  # Tray with items
        self.tray2 = Tray(24)  # Tray to fill holes
        self.gripper = Gripper()
        self.camera = Camera()

    def scan_and_detect(self):
        detected_items = self.camera.scan(self.tray1)
        return detected_items

    def pick_item(self, hole):
        self.gripper.pick(hole)

    def fill_holes(self):
        for index, hole in enumerate(self.tray2.holes):
            if not hole.is_filled() and self.gripper.has_item():
                # Fill the hole in tray2
                hole.fill()  
                print(f"Filled a hole at position ({index // 6}, {index % 6})")  # Position calculation
                self.gripper.release()  # Release the item after filling

    def run(self):
        attempts = 0
        while attempts < 8:
            detected_items = self.scan_and_detect()
            if detected_items:
                print(f"Detected {len(detected_items)} items: {[color for _, color in detected_items]}")
                for hole, color in detected_items:
                    self.pick_item(hole)  # Pick the item from the detected hole
                    print(f"Picked {color} item.")  # Print item picked
                    
                    # Fill holes after picking each item
                    self.fill_holes()  # Fill holes based on detected items
                
                print("Filling progress finished.")
                break
            else:
                attempts += 1
                print("Detection failed, shaking tray 1...")
        else:
            print("Please add more items into tray 1.")