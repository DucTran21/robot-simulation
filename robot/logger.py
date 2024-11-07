import os
import csv
from datetime import datetime

class Logger:
    def __init__(self, filename='simulation_results.csv'):
        self.filename = filename
        self.run_id = self.get_next_run_id()  # Initialize run_id by checking the last entry in the file
        self.ensure_file_exists()

    def ensure_file_exists(self):
        # Create the file with headers if it doesn't exist
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Run ID', 'Timestamp', 'Detected Item Positions', 'Tray 2 Empty Holes', 
                                 'Shaking', 'Filling Complete'])
            print(f"Created new log file: {self.filename}")

    def get_next_run_id(self):
        # Determine the next Run ID by reading the last row of the CSV
        if os.path.isfile(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if len(rows) > 1:  # If there are previous runs, get the last Run ID
                    try:
                        last_run_id = int(rows[-1][0])  # First column is the Run ID
                        return last_run_id + 1
                    except ValueError:
                        # If Run ID isn't an integer, reset to 1
                        return 1
        return 1  # Start with Run ID 1 if the file is new or empty

    def log(self, detected_positions, empty_holes, shake_status, filling_complete):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.run_id, timestamp, detected_positions, empty_holes, shake_status, filling_complete])
        # Print log information for debugging
        print(f"Logged data: Run ID {self.run_id}, Detected item positions: {detected_positions}, "
              f"Empty holes: {empty_holes}, Shaking: {shake_status}, Complete: {filling_complete}")