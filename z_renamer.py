import re
import os
import sys

# Fist argument for path to directory
# All others are starting point to removing, anything after those symbols will be removed
# Uses regex

path_to = sys.argv[1]

z = re.compile('|'.join(sys.argv[2:]))

for root, _, files in os.walk(path_to):
    for file in files:
        print(file)
        if (ending_dot: = file.rfind('.')) > 0:
            ending = file[ending_dot:]
            if ending.lower() not in ['.epub', '.pdf']:
                continue
            name = z.split(file)[0].strip().lower()
            name = '_'.join(name.split(' '))
            os.rename(f'{root}/{file}', f'{root}/{name}{ending}')
        else:
            continue
