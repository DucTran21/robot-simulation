from robot.tray import Tray  # Ensure correct imports
from robot.gripper import Gripper
from robot.camera import Camera
from robot.logger import Logger  # Import Logger properly

class Robot:
    def __init__(self):
        # Initialize trays, gripper, camera, and logger with specified sizes
        self.tray1 = Tray(30)  # Tray 1 with scattered items, assumed to have 30 positions
        self.tray2 = Tray(24)  # Tray 2 with 24 positions to fill
        self.gripper = Gripper()
        self.camera = Camera()
        self.logger = Logger()  # Initialize logger with a new run ID for each robot instance

    def scan_and_detect(self):
        # Scan tray 1 and get detected items with their positions
        detected_items = self.camera.scan(self.tray1)
        return detected_items

    def pick_and_release_items(self, detected_items):
        # For each detected item (position, hole), pick and release into tray 2
        for position, item in detected_items:
            self.gripper.pick(item)
            print(f"Picked item from tray 1 at position {position}.")
            
            # Find the next available hole in tray 2 and fill it
            for hole in self.tray2.holes:
                if not hole.is_filled() and self.gripper.has_item():
                    hole.fill()
                    self.gripper.release()
                    print("Released item to tray 2.")
                    break  # Move on after releasing one item

    def run(self):
        # Main simulation logic
        while not self.tray2.is_full():
            detected_items = self.scan_and_detect()

            if detected_items:
                # Extract item positions for logging
                detected_positions = [pos for pos, _ in detected_items]
                self.pick_and_release_items(detected_items)
                
                # Log the state after picking and releasing items
                empty_holes = sum(1 for hole in self.tray2.holes if not hole.is_filled())
                print(f"Scanning tray 2: {empty_holes} holes need filling.")
                
                self.logger.log(detected_positions, f"{empty_holes} holes need filling", "No", 
                                "No" if empty_holes > 0 else "Yes")
                
                if self.tray2.is_full():
                    print("Filling progress finished.")
                    break

            else:
                print("Detection failed, shaking tray 1...")
                self.tray1.shake()
                self.logger.log([], "Shaking tray 1", "Yes", "No")
        
        if not self.tray2.is_full():
            print("Please add more items into tray 1.")
            self.logger.log([], f"{sum(1 for hole in self.tray2.holes if not hole.is_filled())} holes need filling", "No", "No")