import os

#Variables
report = []
NumOfSafe = 0
okay = False

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split(' ')
    for part in parts:
        report.append(int(part.strip()))
    if (report[0] < report[1]):
        for level in range(len(report)-1):
            if ((report[level] < report[level + 1]) and (0 < abs(report[level] - report[level + 1]) < 4)):
                okay = True
            else:
                okay = False
                break
        if (okay == True):
            NumOfSafe += 1
    elif (report[0] > report[1]):
        for level in range(len(report)-1):
            if ((report[level] > report[level + 1]) and (0 < abs(report[level] - report[level + 1]) < 4)):
                okay = True
            else:
                okay = False
                break
        if (okay == True):
            NumOfSafe += 1
    report.clear()
print('Number of safe reports: ' + str(NumOfSafe)) #549
