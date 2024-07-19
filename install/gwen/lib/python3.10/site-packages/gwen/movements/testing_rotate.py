import subprocess
import time
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Paths to the scripts
clockwise_script_path = os.path.join(current_directory, 'clockwiseturn.py')
stand_script_path = os.path.join(current_directory, 'stand.py')

# Call the clockwiseturn.py script five times with a 0.3-second delay
for _ in range(3):
    subprocess.run(['python3', clockwise_script_path])

# Call the stand.py script once after the rotations are complete
subprocess.run(['python3', stand_script_path])

