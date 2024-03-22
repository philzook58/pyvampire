import subprocess
import os

def binpath():
    return os.path.join(os.path.dirname(__file__), "vampire")

def run(args, **kwargs):
    cmd = [binpath()] + args
    return subprocess.run(cmd, **kwargs)

    
