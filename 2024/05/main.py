import os
import re

rule = []
rules = []
pagenumbers = []
pages = []
incorrects = []
problem = False
result = 0
#---part 2---
NumberOfErrors = 0
resultOfPart2 = 0

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines:
    if (None != re.search("\\d{2}\\|\\d{2}", line)):
        rules.append([int(line[0:2]),int(line[3:5])])
    elif (None != re.search("\\d{2}\\,\\d{2}", line)):
        pagenumbers = [int(num) for num in line.split(',')]
        pages.append(pagenumbers)
#Check all the elements in a rule
for page in pages:
    for element in page:
        #Check all the rules for the element
        for rulez in rules:
            #Check the second part of the rule
            if (element == rulez[1]):  
                for nextelement in range(page.index(element), len(page)):
                    if page[nextelement] == rulez[0]:
                        problem = True
                        incorrects.append(page)
                        break
            if(problem==True):
                break
        if(problem==True):
            break
    if problem == False:
        result += page[int((len(page)-1)/2)]
    problem = False
print("Result of part 1: ", result) #7365

#----part 2----
NumberOfErrors = 1
while(NumberOfErrors != 0):
    for incorrect in incorrects:
        NumberOfErrors = 0
        for element in incorrect:
            for rulez in rules:
                #Check the second part of the rule
                if (element == rulez[1]):  
                    for nextelement in range(incorrect.index(element), len(incorrect)):
                        if incorrect[nextelement] == rulez[0]:
                            incorrect[nextelement] = rulez[1]
                            incorrect[incorrect.index(element)] = rulez[0]
                            NumberOfErrors += 1
for incorrect in incorrects:
    resultOfPart2 += incorrect[int((len(incorrect)-1)/2)]
print("Result of part 2: ", resultOfPart2) #5770