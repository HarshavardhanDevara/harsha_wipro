# 15. Command Line Arguments
import sys
if len(sys.argv) == 3:
    print(f"Contestant: {sys.argv[1]}, Task: {sys.argv[2]}")
else:
    print("Provide contestant name and task as arguments.")