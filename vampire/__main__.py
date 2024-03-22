import sys, vampire, subprocess
sys.exit(subprocess.call([
    vampire.binpath(),
    *sys.argv[1:]
]))