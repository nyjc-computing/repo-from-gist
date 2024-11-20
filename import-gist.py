import os
import shutil
import subprocess

TEMP = "repo"
MANIFEST = [".gitignore", "LICENSE", "README.md", __file__]

def remove(path):
    """Remove a file or directory (recursively), without raising errors"""
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except Exception:
        print(f"Failed to remove {path}")

def extinguish():
    """Cloning successful: remove repo files and replace with gist"""
    for file in MANIFEST:
        remove(file)
    remove(".git")
    try:
        subprocess.run(f"mv {TEMP}/* .", shell=True)
    except Exception:
        print("Error moving cloned files, time to call for help")
    else:
        # Clean up remaining contents of cloned dir e.g. .git
        remove(TEMP)


url = input("Enter gist url: ")

# Clone gist into temporary directory
remove(TEMP)
os.mkdir(TEMP)
print(f"Cloning {url} ...")
try:
    subprocess.run(["git", "clone", url, TEMP])
except Exception as err:
    print(err)
    print("Error cloning {url}, cleaning up ...")
    remove(TEMP)
else:
    extinguish()
