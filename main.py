import csv
import sys
import os
import random

print('\n'*5)
questions = []
answers = []

if len(sys.argv)<2:
    sys.exit()

for path in sys.argv[1:]:
    files=[path] if os.path.isfile(path) else [os.path.join(path,f) for f in os.listdir(path)]

    for file in files:
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(row[0])
                answers.append(row[1])



a=[]

for i in range(10):
    k=random.randint(0,len(questions)-1)

    print(i+1, questions[k],end='\n'*3)

    input()
    a.append(answers[k])

for i,j in enumerate(a):
    print(i+1,j)