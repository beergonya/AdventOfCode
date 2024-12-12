import os

#Variables
report = []
modified_report = []
NumOfSafe = 0
NumOfErrors = 0
okay = False

def CheckReport():
    global NumOfErrors
    global NumOfSafe
    if (report[0] < report[1]):
        for level in range(len(report)-1):
            if ((report[level] < report[level + 1]) and (0 < abs(report[level] - report[level + 1]) < 4)):
                okay = True
            else:
                NumOfErrors += 1
                okay = False
                break
    else:
        for level in range(len(report)-1):
            if ((report[level] > report[level + 1]) and (0 < abs(report[level] - report[level + 1]) < 4)):
                okay = True
            else:
                NumOfErrors += 1
                okay = False
                break

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split(' ')
    for part in parts:
        report.append(int(part.strip()))
    CheckReport()
    if (NumOfErrors == 0):
        NumOfSafe += 1
    else:
        og_report = report.copy()
        print("og:", og_report)
        for damped in range(len(report)):
            NumOfErrors = 0
            print(damped)
            report.pop(damped)
            print("remove: ",report)
            CheckReport()
            report = og_report.copy()
            if(NumOfErrors == 0):
                NumOfSafe += 1
                break
    NumOfErrors = 0
    report.clear()
print('Number of safe reports: ' + str(NumOfSafe)) #589
