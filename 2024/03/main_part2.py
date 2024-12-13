import re
import os

result = 0
enabling = True
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines:
    x = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)", line)
    for command in x:
        if ("do()" == command):
            enabling = True
        elif ("don't()" == command):
            enabling = False
        else:
            if(enabling):
                pair = re.findall("\\d{1,3}", command)
                result += int(pair[0]) * int(pair[1])
print(result) #113 965 544
