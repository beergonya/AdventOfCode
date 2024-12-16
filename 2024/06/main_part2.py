import os
import copy

map = []
visited_cells = 0
NumOfLoops = 0
current_location = [] # 0-x, 1-y

def printMap():
    for row in map:
        print(row)

def stepForward():
    global current_location
    global map
    if '^' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = 'X'
        current_location[0] = current_location[0]-1
        map[current_location[0]][current_location[1]] = '^'
    elif '>' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = 'X'
        current_location[1] = current_location[1]+1
        map[current_location[0]][current_location[1]] = '>'
    elif 'v' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = 'X'
        current_location[0] = current_location[0]+1
        map[current_location[0]][current_location[1]] = 'v'
    elif '<' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = 'X'
        current_location[1] = current_location[1]-1
        map[current_location[0]][current_location[1]] = '<'

def TurnRight():
    global map
    if '^' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = '>'
    elif '>' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = 'v'
    elif 'v' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = '<'
    elif '<' == map[current_location[0]][current_location[1]]:
        map[current_location[0]][current_location[1]] = '^'

def stillOnMap():
    if '^' == map[current_location[0]][current_location[1]]:
        if 0 == current_location[0]:
            return False
        else:
            return True
    elif '>' == map[current_location[0]][current_location[1]]:
        if len(map[0]) - 1 == current_location[1]:
            return False
        else:
            return True    
    elif 'v' == map[current_location[0]][current_location[1]]:
        if len(map) - 1 == current_location[0]:
            return False
        else:
            return True 
    elif '<' == map[current_location[0]][current_location[1]]:
        if 0 == current_location[1]:
            return False
        else:
            return True
def checkNextStep():
    if '^' == map[current_location[0]][current_location[1]]:
        if "#" == map[current_location[0]-1][current_location[1]]:
            return False
        else:
            return True
    elif '>' == map[current_location[0]][current_location[1]]:
        if "#" == map[current_location[0]][current_location[1]+1]:
            return False
        else:
            return True    
    elif 'v' == map[current_location[0]][current_location[1]]:
        if "#" == map[current_location[0]+1][current_location[1]]:
            return False
        else:
            return True 
    elif '<' == map[current_location[0]][current_location[1]]:
        if "#" == map[current_location[0]][current_location[1]-1]:
            return False
        else:
            return True

def calculateCells():
    global visited_cells
    visited_cells = 1
    for row in map:
        for cell in row:
            if 'X' == cell:
                visited_cells += 1
        

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines:
    row = []
    for cell in range(len(line)-1):
        row.append(line[cell])
    map.append(row)


og_map = copy.deepcopy(map)
for row in range(len(og_map)):
    for col in range(len(og_map[0])):
        map = copy.deepcopy(og_map)
        #Find the starting location of the guard
        for rowx in range(len(map)):
            for cellx in range(len(map[0])):
                if ('^' == map[rowx][cellx]):
                    current_location = [rowx, cellx]

        if '.' == map[row][col]:
            map[row][col] = '#'
        
        for x in range(10001):
            if stillOnMap():
                if checkNextStep():
                    stepForward()
                else:
                    TurnRight()
            else:
                calculateCells()
                break
            if x == 10000:
                NumOfLoops += 1
                break
        visited_cells = 0
        map.clear()
print("NumOfLoops: ", NumOfLoops) #1443




