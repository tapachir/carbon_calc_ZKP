
import matplotlib.pyplot as plt
import numpy as np
import csv
one_digit_10_pre_run = []
two_digit_10_pre_run = []
three_digit_10_pre_run = []
hundret_10_pre_run = []
## 10 hier unwichtig!!!! er nimmt alle nicht nur 10
with open("results_all.csv", 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv)
    for row in mycsv:
        if not "_check" in row[0]:    
            continue
        print(row)
        if  "10_" in row[0]:
                one_digit_10_pre_run.append(float(row[1].strip()))
        if "20" in row[0]:
                two_digit_10_pre_run.append(float(row[1]))
        if "30" in row[0]:
                three_digit_10_pre_run.append(float(row[1]))
        if "100" in row[0]:
                hundret_10_pre_run.append(float(row[1]))
#labels = ['10', '20', '30', '100']
print(one_digit_10_pre_run)
print(two_digit_10_pre_run)
print(three_digit_10_pre_run)
print(hundret_10_pre_run)
x = np.arange(3)  # the label locations
width = 0.2  # the width of the bars

plt.bar(x-0.2, one_digit_10_pre_run, width, color='cyan')
plt.bar(x, two_digit_10_pre_run, width, color='orange')
plt.bar(x+0.2, three_digit_10_pre_run, width, color='green')
plt.bar(x+0.4, hundret_10_pre_run, width, color='red')

plt.xticks(x, ['0', '1', '2'])
plt.xlabel("Added Digits to Input Values")
plt.ylabel("Execution Times [Seconds]")
plt.legend(["10", "20", "30", "100"])
#plt.margins(y=0.07)
plt.show()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

# fig.tight_layout()

# plt.show()





# import matplotlib.pyplot as plt
# import numpy
 
# import csv
# one_digit_10_pre_run = []
# one_digit_10_zkp_calc = []
# one_digit_10_proof_gen = []
# one_digit_10_verify_save = []

# with open("1_digit_runs/1_digit_10_exe_times.csv", 'r') as f:
#     mycsv = csv.reader(f)
#     next(mycsv)
#     for row in mycsv:
#         if not (row):    
#             continue
#         print(row)
#         one_digit_10_pre_run.append(row[1])
#         one_digit_10_zkp_calc.append(row[2])
#         one_digit_10_proof_gen.append(row[3])
#         one_digit_10_verify_save.append(row[4])
# # np_one_digit_10_pre_run = numpy.array(one_digit_10_pre_run)
# # np_one_digit_10_zkp_calc= numpy.array(one_digit_10_zkp_calc)
# # np_one_digit_10_proof_gen= numpy.array(one_digit_10_proof_gen)
# # np_one_digit_10_verify_save= numpy.array(one_digit_10_verify_save)

# data = [np_one_digit_10_pre_run, np_one_digit_10_zkp_calc, np_one_digit_10_proof_gen, np_one_digit_10_verify_save]

# fig = plt.figure(figsize =(10, 7))
 
# # Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])
 
# # Creating plot
# bp = ax.boxplot(data)
 
# # show plot
# plt.show()
