import os
import subprocess

debs_directory = "./debs"
for filename in os.listdir(debs_directory):
    if filename.endswith(".deb"):
        prefix, extension = os.path.splitext(filename)
        parts = prefix.split(".")
        if len(parts) >= 3:
            # Keep the tweak name unchanged
            tweak_name = ".".join(parts[2:])
            new_filename = "xyz.roc4et." + tweak_name + extension
            old_path = os.path.join(debs_directory, filename)
            new_path = os.path.join(debs_directory, new_filename)
            os.rename(old_path, new_path)

# Step 2: Update Packages file and compress it
subprocess.run("rm Packages Packages.bz2", shell=True)
subprocess.run("dpkg-scanpackages -m ./debs > Packages", shell=True)
subprocess.run("bzip2 -fks Packages", shell=True)
print("Packages file updated and compressed.")
