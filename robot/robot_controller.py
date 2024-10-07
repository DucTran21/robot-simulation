# robot/robot_controller.py
from .camera import Camera
from .gripper import Gripper
from .tray import Tray

class Robot:
    def __init__(self, tray1, tray2):
        self.tray1 = tray1
        self.tray2 = tray2
        self.camera = Camera()
        self.gripper = Gripper()

    def process_trays(self):
        detected_items = self.camera.scan_tray(self.tray1)
        
        if detected_items:
            self.gripper.pick_items(detected_items)
            self.tray2.fill_holes(detected_items)
            print("Filling progress finished.")
        else:
            print("Please add more items into tray 1.")