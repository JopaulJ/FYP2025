import os
import subprocess

cant_angles = range(-120, 121, 4)
sweep_angles = range(-20, 21, 2)

for cant in cant_angles:
    for sweep in sweep_angles:
        folder_name = f"c{cant}s{sweep}"
        os.makedirs(folder_name, exist_ok=True)
        command = f'py geometry_generation.py -c {cant} -s {sweep} -o {folder_name}'
        print(f"Running: {command}")
        subprocess.run(command, shell=True)