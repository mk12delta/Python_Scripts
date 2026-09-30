#!/usr/bin/env python3
#script to analyze Odin usage by username

import sys
import subprocess
import re

if len(sys.argv) != 2:
    print(sys.argv[0] + " username")
    sys.exit(1)
else:
    username = sys.argv[1]

raw = subprocess.run(['last'], stdout=subprocess.PIPE)
output = raw.stdout.decode('utf-8')

lines = output.splitlines()
search_name = username[:8]
pattern = '^' + search_name + r'\s'
duration = r'\((\d\d):(\d\d)\)'
count = 0
total_hours = 0
total_minutes = 0

print(f'Here is a summary of the logins for {username}:\n')
for line in lines:
    if re.search(pattern, line):
        count += 1
        print(f"{count}. {line}")
        if re.search(duration, line):
            total_hours += int(re.search(duration, line).group(1))
            total_minutes += int(re.search(duration, line).group(2))

total_hours = total_hours + (total_minutes // 60)
total_minutes = total_minutes % 60

print()
print(f'Account: {username}')
print(f'Total logins: {count}')
print(f'{total_hours:02d} hours and {total_minutes:02d} minutes')