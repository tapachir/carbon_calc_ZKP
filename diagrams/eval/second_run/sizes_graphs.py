from cProfile import label
from tabnanny import check
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np
import csv
one_digit_10_pre_run = []
two_digit_10_pre_run = []
three_digit_10_pre_run = []
hundret_10_pre_run = []
check_10_pre_run = []
## 10 hier unwichtig!!!! er nimmt alle nicht nur 10
with open("sizes.csv", 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv)
    for row in mycsv:
        print(row)
        one_digit_10_pre_run.append(float(row[1].strip()))
        two_digit_10_pre_run.append(float(row[2]))
        three_digit_10_pre_run.append(float(row[3]))
        hundret_10_pre_run.append(float(row[4]))
        check_10_pre_run.append(float(row[5]))
#labels = ['10', '20', '30,40,50,60,70,80,90', '100']
print(one_digit_10_pre_run)
print(two_digit_10_pre_run)
print(three_digit_10_pre_run)
print(hundret_10_pre_run)
print(check_10_pre_run)


plt.ylabel("Execution Times [Seconds]")
plt.xlabel("Amount of Inputed Values")

plt.plot([10, 20, 30,40,50,60,70,80,90, 100], one_digit_10_pre_run,label="test" )
plt.plot([10, 20, 30,40,50,60,70,80,90, 100], two_digit_10_pre_run)
plt.plot([10, 20, 30,40,50,60,70,80,90, 100], three_digit_10_pre_run)
plt.plot([10, 20, 30,40,50,60,70,80,90, 100], hundret_10_pre_run)
plt.plot([10, 20, 30,40,50,60,70,80,90, 100], check_10_pre_run)
plt.legend(['Pre-Run Calculation', 'Zokrates Calculation', "Proof Generation", "Verify and Save", "Check Proof"])

plt.show()
