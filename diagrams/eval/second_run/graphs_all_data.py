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
# np_one_digit_10_pre_run = numpy.array(one_digit_10_pre_run)
# np_one_digit_10_zkp_calc= numpy.array(one_digit_10_zkp_calc)
# np_one_digit_10_proof_gen= numpy.array(one_digit_10_proof_gen)
# np_one_digit_10_verify_save= numpy.array(one_digit_10_verify_save)

# data = [np_one_digit_10_pre_run, np_one_digit_10_zkp_calc, np_one_digit_10_proof_gen, np_one_digit_10_verify_save]
# 
# fig = plt.figure(figsize =(10, 7))
 
# # Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])
 
# # Creating plot
# bp = ax.boxplot(data)
 
# # show plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

sizes = pd.read_csv(r'sizes.csv')
df1_10_exe = pd.read_csv (r'10/exe_times.csv') 
df1_10_check = pd.read_csv (r'10/check_times.csv') 
df1_20_exe = pd.read_csv (r'20/exe_times.csv') 
df1_20_check = pd.read_csv (r'20/check_times.csv') 
df1_30_exe = pd.read_csv (r'30/exe_times.csv') 
df1_30_check = pd.read_csv (r'30/check_times.csv') 
df1_40_exe = pd.read_csv (r'40/exe_times.csv') 
df1_40_check = pd.read_csv (r'40/check_times.csv') 
df1_50_exe = pd.read_csv (r'50/exe_times.csv') 
df1_50_check = pd.read_csv (r'50/check_times.csv') 
df1_60_exe = pd.read_csv (r'60/exe_times.csv') 
df1_60_check = pd.read_csv (r'60/check_times.csv') 
df1_70_exe = pd.read_csv (r'70/exe_times.csv') 
df1_70_check = pd.read_csv (r'70/check_times.csv') 
df1_80_exe = pd.read_csv (r'80/exe_times.csv') 
df1_80_check = pd.read_csv (r'80/check_times.csv') 
df1_90_exe = pd.read_csv (r'90/exe_times.csv') 
df1_90_check = pd.read_csv (r'90/check_times.csv') 
df1_100_exe = pd.read_csv (r'100/exe_times.csv') 
df1_100_check = pd.read_csv (r'100/check_times.csv') 



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

mean_df1_40_exe_pre_run = df1_40_exe['pre-run']
mean_df1_40_exe_zkp_calc = df1_40_exe['zkp-calc']
mean_df1_40_exe_proof_gen = df1_40_exe['proof_gen']
mean_df1_40_exe_verify_save = df1_40_exe['verify_save']
mean_df1_40_check = df1_40_check['check_Proof']

mean_df1_50_exe_pre_run = df1_50_exe['pre-run']
mean_df1_50_exe_zkp_calc = df1_50_exe['zkp-calc']
mean_df1_50_exe_proof_gen = df1_50_exe['proof_gen']
mean_df1_50_exe_verify_save = df1_50_exe['verify_save']
mean_df1_50_check = df1_50_check['check_Proof']

mean_df1_60_exe_pre_run = df1_60_exe['pre-run']
mean_df1_60_exe_zkp_calc = df1_60_exe['zkp-calc']
mean_df1_60_exe_proof_gen = df1_60_exe['proof_gen']
mean_df1_60_exe_verify_save = df1_60_exe['verify_save']
mean_df1_60_check = df1_60_check['check_Proof']

mean_df1_70_exe_pre_run = df1_70_exe['pre-run']
mean_df1_70_exe_zkp_calc = df1_70_exe['zkp-calc']
mean_df1_70_exe_proof_gen = df1_70_exe['proof_gen']
mean_df1_70_exe_verify_save = df1_70_exe['verify_save']
mean_df1_70_check = df1_70_check['check_Proof']

mean_df1_80_exe_pre_run = df1_80_exe['pre-run']
mean_df1_80_exe_zkp_calc = df1_80_exe['zkp-calc']
mean_df1_80_exe_proof_gen = df1_80_exe['proof_gen']
mean_df1_80_exe_verify_save = df1_80_exe['verify_save']
mean_df1_80_check = df1_80_check['check_Proof']

mean_df1_90_exe_pre_run = df1_90_exe['pre-run']
mean_df1_90_exe_zkp_calc = df1_90_exe['zkp-calc']
mean_df1_90_exe_proof_gen = df1_90_exe['proof_gen']
mean_df1_90_exe_verify_save = df1_90_exe['verify_save']
mean_df1_90_check = df1_90_check['check_Proof']


mean_df1_100_exe_pre_run = df1_100_exe['pre-run']
mean_df1_100_exe_zkp_calc = df1_100_exe['zkp-calc']
mean_df1_100_exe_proof_gen = df1_100_exe['proof_gen']
mean_df1_100_exe_verify_save = df1_100_exe['verify_save']
mean_df1_100_check =df1_100_check['check_Proof']




verikey = sizes["veri_key"]

provingKey = sizes["proving_key"]
out = sizes["out"]
proof = sizes["proof"]
witness = sizes["witness"]



plt.ylabel("Execution Times [Seconds]")
plt.xlabel("Amount of Inputed Values")

plt.plot([10, 20, 30,40,50,60,70,80,90, 100], out )
#plt.plot([10, 20, 30,40,50,60,70,80,90, 100], provingKey)
#plt.plot([10, 20, 30,40,50,60,70,80,90, 100], verikey)
#plt.plot([10, 20, 30,40,50,60,70,80,90, 100], proof)
#plt.plot([10, 20, 30,40,50,60,70,80,90, 100], check_10_pre_run)
#plt.legend(['Pre-Run Calculation', 'Zokrates Calculation', "Proof Generation", "Verify and Save", "Check Proof"])

plt.show()


