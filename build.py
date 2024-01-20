import subprocess

subprocess.run("rm Packages Packages.bz2", shell=True)
subprocess.run("dpkg-scanpackages -m ./debs > Packages", shell=True)
subprocess.run("bzip2 -fks Packages", shell=True)
print("Packages file updated and compressed.")
