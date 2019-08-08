import re
import sys

for line in sys.stdin:
    print(re.sub(r'(\w)(\1*)', r'\1', line.rstrip()))
