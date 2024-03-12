import os
import time
from datetime import datetime

# Task list
tasks = ['ST1', 'ST2', 'DTAN', 'DTF', 'DTV', 'DTS1', 'DTS7', 'DTCT']


class Test:
    @staticmethod
    def generate_files(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

        for i, task in enumerate(tasks):
            for j in range(2):  # Create two .csv files for each task
                file_name = f"sensor_22ffeddf_ewdw_aas_{i*3+j}.csv"
                file_path = os.path.join(folder, file_name)
                with open(file_path, 'w') as f:
                    f.write(f"Test file {file_name}")
                time.sleep(1)  # Wait a second between each file

            # Create a .mp4 file for each task
            file_name = f"sensor_22ffeddf_ewdw_aas_{i*3+2}.mp4"
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'w') as f:
                f.write(f"Test file {file_name}")
            time.sleep(1)  # Wait a second between each file


if __name__ == "__main__":
    Test.generate_files("test_folder")
