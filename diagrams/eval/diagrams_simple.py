import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



import matplotlib.pyplot as plt
import numpy as np
import csv
one_digit_10_pre_run = []
two_digit_10_pre_run = []
three_digit_10_pre_run = []
hundret_10_pre_run = []
## 10 hier unwichtig!!!! er nimmt alle nicht nur 10
one_digit_10_pre_run = []
two_digit_10_pre_run = []
three_digit_10_pre_run = []
hundret_10_pre_run = []
check_10_pre_run = []

## 10 hier unwichtig!!!! er nimmt alle nicht nur 10
with open("results_all.csv", 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv)
    for row in mycsv:
        if not "df2" in row[0]:    
            continue
        print(row)
        if  "pre_run" in row[0]:
                one_digit_10_pre_run.append(float(row[1].strip()))
        # if "zkp_calc" in row[0]:
        #         two_digit_10_pre_run.append(float(row[1]))
        # if "proof_gen" in row[0]:
        #         three_digit_10_pre_run.append(float(row[1]))
        # if "verify_save" in row[0]:
        #         hundret_10_pre_run.append(float(row[1]))
        # if "check" in row[0]:
        #         check_10_pre_run.append(float(row[1]))
#labels = ['10', '20', '30', '100']
x = np.arange(4)  # the label locations
width = 0.5  # the width of the bars

plt.bar(x, one_digit_10_pre_run, width, color='orange')

plt.xticks(x, ['10', '20', '30', "100"])
plt.xlabel("Amount of Input Values")
plt.ylabel("Execution Times [Seconds]")
#plt.margins(y=0.07)
plt.show()