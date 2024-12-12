import os

#Variables
left = []
right = []
distance = []
result = 0

def ReadInputs():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split('   ')
        left.append(int(parts[0].strip()))
        right.append(int(parts[1].strip()))

def BubbleSorting(numbers):
    n = len(numbers)
    for x in range(n):
        for y in range(0, n-x-1):
            if (numbers[y] > numbers[y+1]):
                temp = numbers[y]
                numbers[y] = numbers[y+1]
                numbers[y+1] = temp


ReadInputs()
BubbleSorting(left)
BubbleSorting(right)

#Calculate the distances
for i in range(len(left)):
    distance.append(abs(left[i]-right[i]))

#Sum of the distances
for i in range(len(distance)):
    result += distance[i]

print(result) # 2 375 403
