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
#Horizontal check
for line in lines:
    #Horizontal left to right
    for part in range(len(line)-3):
        word = str(line[part] + line[part + 1] + line[part + 2] + line[part + 3])
        XmasCheck(word)
    #Horizontal right to left
    for part in range(len(line),3,-1):
        word = str(line[part - 1] + line[part - 2] + line[part - 3] + line[part - 4])
        XmasCheck(word)
#Vertical check
for column in range(len(lines[0])-1):
    #Top to bottom
    for row in range(len(lines)-3):        
        word = str(lines[row][column] + lines[row + 1][column] + lines[row + 2][column] + lines[row + 3][column])
        XmasCheck(word)
    #Bottom to top
    for row in range(len(lines), 3, -1):
        word = str(lines[row -1][column] + lines[row - 2][column] + lines[row - 3][column] + lines[row - 4][column])
        XmasCheck(word)
#Diagonal
for line in range(len(lines) - 3):
    #Top left to bottom right
    for column in range(len(lines[0]) - 4):
        word = str(lines[line][column] + lines[line + 1][column + 1] + lines[line + 2][column + 2] + lines[line + 3][column + 3])
        XmasCheck(word)
    #Top right to bottom left
    for column in range(len(lines[0]) - 1, 2, -1):
        word = str(lines[line][column] + lines[line + 1][column - 1] + lines[line + 2][column - 2] + lines[line + 3][column - 3])
        XmasCheck(word)
for line in range(len(lines) - 1, 2, -1):
    #Bottom left to top right
    for column in range(len(lines[0]) - 4):
        word = str(lines[line][column] + lines[line - 1][column + 1] + lines[line - 2][column + 2] + lines[line - 3][column + 3])
        XmasCheck(word)
    #Bottom right to top left
    for column in range(len(lines[0]) - 2, 2, -1): 
        word = str(lines[line][column] + lines[line - 1][column - 1] + lines[line - 2][column - 2] + lines[line - 3][column - 3])   
        XmasCheck(word)
print(result) #2551
