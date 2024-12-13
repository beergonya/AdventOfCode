import os

result = 0
asdasd = False
def XmasCheck(word):
    global result
    if ("XMAS" == word):
        result += 1
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()

for line in range(len(lines) - 2):
    for column in range(len(lines[0])-3):
        rightdown = str(lines[line][column] + lines[line + 1][column + 1] + lines[line + 2][column + 2])
        rightup   = str(lines[line + 2][column] + lines[line + 1][column + 1] + lines[line][column + 2])
        if (rightdown == "MAS" or rightdown == "SAM"):
            if (rightup == "MAS" or rightup == "SAM"):
                result += 1
print(result) #1 985
