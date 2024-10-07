# Robot Simulation Project

## Overview

This project simulates a robot model designed for material filling in an assembly process. The robot scans a tray for items, picks them up, and fills holes in a second tray.

## Goals

- Develop a functioning robot simulation capable of detecting and picking items from a tray.
- Implement a system for filling holes in another tray based on the items detected.
- Enhance the simulation with future capabilities, such as improved detection algorithms and handling multiple item types.

## Project Structure

- main.py: Entry point to run the simulation.
- robot/: Contains all robot-related classes:
    - robot.py: Main logic of the robot.
    - camera.py: Handles item detection.
    - tray.py: Manages the holes in the tray.
    - hole.py: Represents individual holes in the tray.
    - gripper.py: Manages item picking and releasing.
    - vacuum_switch.py: Placeholder for vacuum functionality.
- requirements.txt: List of required packages.

## Extensions and Changes

- The UML diagram has been adjusted to better reflect the relationships and interactions among classes.

## Running the Simulation

To run the simulation, execute the following command:

```bash
python main.py