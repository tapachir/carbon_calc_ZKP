# import matplotlib.pyplot as plt
# import pandas


# # x-coordinates of left sides of bars 
# left = [1, 2, 3, 4]
  
# # heights of bars
# height = [2.031825966835022, 2.3654853224754335, 2.043650224208832, 2.0539584827423094]
  
# # labels for bars
# tick_label = ['10', '20', '30', '100', ]
  
# # plotting a bar chart
# plt.bar(left, height, tick_label = tick_label,
#         width = 0.8, color = ['red', 'green'])
  
# # naming the x-axis
# plt.xlabel('x - axis')
# # naming the y-axis
# plt.ylabel('y - axis')
# # plot title
# plt.title('My bar chart!')
  
# # function to show the plot
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import csv
one_digit_10_pre_run = []
two_digit_10_pre_run = []
three_digit_10_pre_run = []
## 10 hier unwichtig!!!! er nimmt alle nicht nur 10
with open("results_all.csv", 'r') as f:
    mycsv = csv.reader(f)
    next(mycsv)
    for row in mycsv:
        if not "_check" in row[0]:    
            continue
        print(row)
        if  "df1" in row[0]:
                one_digit_10_pre_run.append(float(row[1].strip()))
        if "df2" in row[0]:
                two_digit_10_pre_run.append(float(row[1]))
        if "df3" in row[0]:
                three_digit_10_pre_run.append(float(row[1]))
#labels = ['10', '20', '30', '100']
print(one_digit_10_pre_run)
print(two_digit_10_pre_run)
print(three_digit_10_pre_run)
x = np.arange(4)  # the label locations
width = 0.2  # the width of the bars

plt.bar(x-0.2, one_digit_10_pre_run, width, color='cyan')
plt.bar(x, two_digit_10_pre_run, width, color='orange')
plt.bar(x+0.2, three_digit_10_pre_run,width,color='green')

plt.xticks(x, ['10', '20', '30', "100"])
plt.xlabel("Amount of Input Values")
plt.ylabel("Execution Times [Seconds]")
plt.legend(["0 Digit extra", "1 Digit Extra", "2 Digits Extra"])
#plt.ylim(0.021)
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
