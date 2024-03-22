import subprocess
import os

def binpath():
    return os.path.join(os.path.dirname(__file__), "vampire_z3_rel_master_7397")

def vampire(args, **kwargs):
    cmd = [binpath()] + args
    return subprocess.run(cmd, **kwargs)

    
