# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from robot.robot_controller import Robot
from robot.tray import Tray
from robot.camera import Camera
from robot.hole import Hole
from robot.gripper import Gripper
from robot.vacuum_switch import VacuumSwitch

def main():
    # Initialize the camera with a color threshold for detection
    camera = Camera(color_thresholds=['gold-yellow'])
    
    # Initialize the gripper and vacuum switch
    gripper = Gripper()
    vacuum_switch = VacuumSwitch()

    # Initialize tray 1 (randomly scattered items)
    tray1 = Tray(total_holes=0)  # Tray 1 has no defined "holes"
    
    # Initialize tray 2 (24 holes to be filled)
    tray2 = Tray(total_holes=24)

    # Initialize the robot
    robot = Robot(camera=camera, gripper=gripper, tray1=tray1, tray2=tray2)

    # Step 1: Scan tray 2 to detect empty holes
    print("Scanning tray 2 for empty holes...")
    empty_holes = robot.scan_tray()  # This returns the list of empty holes
    print(f"Detected {len(empty_holes)} empty holes.")

    # Step 2: Try to scan tray 1 for items
    print("Scanning tray 1 for items...")
    items_detected = robot.scan_tray1_for_items()

    if items_detected:
        # Step 3: If items are detected, pick and place them into tray 2
        print("Picking and filling items into tray 2...")
        robot.pick_and_fill()
    else:
        # If no items detected after multiple attempts
        print("Please add more items into tray 1.")

    # Step 4: Final scan of tray 2 to ensure all holes are filled
    print("Final scan of tray 2...")
    robot.final_scan()

    # Step 5: Finish
    print("Filling progress finished.")

if __name__ == "__main__":
    main()