import re
import os

result = 0

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines:
    x = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", line)
    for mul in x:
        pair = re.findall("\\d{1,3}", mul)
        print(pair)
        result += int(pair[0]) * int(pair[1])

print(len(x))
print(result) #188 192 787
