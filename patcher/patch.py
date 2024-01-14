import os
import subprocess

input_directory = "/Users/roc4et/Documents/repo.roc4et.de/patcher/in"
output_directory = "/Users/roc4et/Documents/repo.roc4et.de/patcher/out"

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    input_filepath = os.path.join(input_directory, filename)
    if os.path.isfile(input_filepath):
        output_filepath = os.path.join(output_directory, filename)
        command = f"sudo bash '/Users/roc4et/Documents/repo.roc4et.de/patcher/patch.sh' {input_filepath} {output_filepath}"
        subprocess.run(command, shell=True)
        if filename.endswith(".deb"):
            os.remove(input_filepath)

for folder in os.listdir(input_directory):
    folder_path = os.path.join(input_directory, folder)
    if os.path.isdir(folder_path):
        subprocess.run(f"sudo rm -rf {folder_path}", shell=True)

print("Processing completed.")