# import matplotlib.pyplot as plt
# import numpy
 
# import csv
# one_digit_10_pre_run = []
# one_digit_10_zkp_calc = []
# one_digit_10_proof_gen = []
# one_digit_10_verify_save = []

# with open("3_digits_runs/3_digits_10_exe_times.csv", 'r') as f:
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
# np_one_digit_10_pre_run = numpy.array(one_digit_10_pre_run)
# np_one_digit_10_zkp_calc= numpy.array(one_digit_10_zkp_calc)
# np_one_digit_10_proof_gen= numpy.array(one_digit_10_proof_gen)
# np_one_digit_10_verify_save= numpy.array(one_digit_10_verify_save)

# data = [np_one_digit_10_pre_run, np_one_digit_10_zkp_calc, np_one_digit_10_proof_gen, np_one_digit_10_verify_save]
# data =
# fig = plt.figure(figsize =(10, 7))
 
# # Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])
 
# # Creating plot
# bp = ax.boxplot(data)
 
# # show plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("3_digits_runs/3_digits_10_exe_times.csv")

df1_10_exe = pd.read_csv (r'3_digits_runs/3_digits_10_exe_times.csv') 
df1_10_check = pd.read_csv (r'3_digits_runs/3_digits_10_check_times.csv') 
df1_20_exe = pd.read_csv (r'3_digits_runs/3_digits_20_exe_times.csv') 
df1_20_check = pd.read_csv (r'3_digits_runs/3_digits_20_check_times.csv') 
df1_30_exe = pd.read_csv (r'3_digits_runs/3_digits_30_exe_times.csv') 
df1_30_check = pd.read_csv (r'3_digits_runs/3_digits_30_check_times.csv') 
df1_100_exe = pd.read_csv (r'3_digits_runs/3_digits_100_exe_times.csv') 
df1_100_check = pd.read_csv (r'3_digits_runs/3_digits_100_check_times.csv') 



mean_df1_10_exe_pre_run = df1_10_exe['pre-run']
mean_df1_10_exe_zkp_calc = df1_10_exe['zkp-calc']
mean_df1_10_exe_proof_gen = df1_10_exe['proof_gen']
mean_df1_10_exe_verify_save = df1_10_exe['verify_save']
mean_df1_10_check = df1_10_check['check_Proof']



mean_df1_20_exe_pre_run = df1_20_exe['pre-run']
mean_df1_20_exe_zkp_calc = df1_20_exe['zkp-calc']
mean_df1_20_exe_proof_gen = df1_20_exe['proof_gen']
mean_df1_20_exe_verify_save = df1_20_exe['verify_save']
mean_df1_20_check = df1_20_check['check_Proof'] 


mean_df1_30_exe_pre_run = df1_30_exe['pre-run']
mean_df1_30_exe_zkp_calc = df1_30_exe['zkp-calc']
mean_df1_30_exe_proof_gen = df1_30_exe['proof_gen']
mean_df1_30_exe_verify_save = df1_30_exe['verify_save']
mean_df1_30_check = df1_30_check['check_Proof']


mean_df1_100_exe_pre_run = df1_100_exe['pre-run']
mean_df1_100_exe_zkp_calc = df1_100_exe['zkp-calc']
mean_df1_100_exe_proof_gen = df1_100_exe['proof_gen']
mean_df1_100_exe_verify_save = df1_100_exe['verify_save']
mean_df1_100_check =df1_100_check['check_Proof']






pre_run = dataframe["pre-run"]
zko_calc = dataframe['zkp-calc']
proof_gen = dataframe['proof_gen']
verify_save = dataframe['verify_save']

columns = [mean_df1_10_exe_pre_run, mean_df1_20_exe_pre_run, mean_df1_30_exe_pre_run, mean_df1_100_exe_pre_run]

fig1, ax1 = plt.subplots()
ax1.set_xlabel("Amount of Input Values")
ax1.set_ylabel("Execution Time [Seconds]")
ax1.set_label("Pre-Run")
ax1.boxplot(columns)
ax1.set_xticks([1, 2,3,4], ["10", "20", "30", "100"])


fig2, ax2 = plt.subplots()
columns2 = [mean_df1_10_exe_zkp_calc, mean_df1_20_exe_zkp_calc, mean_df1_30_exe_zkp_calc, mean_df1_100_exe_zkp_calc]
ax2.boxplot(columns2)
ax2.set_xlabel("Amount of Input Values")
ax2.set_ylabel("Execution Time [Seconds]")
ax2.set_label("Zokrates Calculation")
ax2.set_xticks([1, 2,3,4], ["10", "20", "30", "100"])


fig3, ax3 = plt.subplots()
columns3 = [mean_df1_10_exe_proof_gen, mean_df1_20_exe_proof_gen, mean_df1_30_exe_proof_gen, mean_df1_100_exe_proof_gen]
ax3.boxplot(columns3)

ax3.set_xlabel("Amount of Input Values")
ax3.set_ylabel("Execution Time [Seconds]")
ax3.set_label("Proof Generation")
ax3.set_xticks([1, 2,3,4], ["10", "20", "30", "100"])

fig4, ax4 = plt.subplots()
columns4 = [mean_df1_10_exe_verify_save, mean_df1_20_exe_verify_save, mean_df1_30_exe_verify_save, mean_df1_100_exe_verify_save]
ax4.boxplot(columns4)
ax4.set_xlabel("Amount of Input Values")
ax4.set_ylabel("Execution Time [Seconds]")
ax4.set_label("Verify and Save Proof")
ax4.set_xticks([1, 2,3,4], ["10", "20", "30", "100"])

plt.ylabel("Execution Time [Seconds]")
plt.xlabel("Amount of Input Values")
plt.xticks([1, 2,3,4], ["10", "20", "30", "100"])

plt.show()




