import pandas as pd


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



mean_df1_10_exe_pre_run = df1_10_exe['pre-run'].mean()
mean_df1_10_exe_zkp_calc = df1_10_exe['zkp-calc'].mean()
mean_df1_10_exe_proof_gen = df1_10_exe['proof_gen'].mean()
mean_df1_10_exe_verify_save = df1_10_exe['verify_save'].mean()
mean_df1_10_check = df1_10_check['check_Proof'].mean()



mean_df1_20_exe_pre_run = df1_20_exe['pre-run'].mean()
mean_df1_20_exe_zkp_calc = df1_20_exe['zkp-calc'].mean()
mean_df1_20_exe_proof_gen = df1_20_exe['proof_gen'].mean()
mean_df1_20_exe_verify_save = df1_20_exe['verify_save'].mean()
mean_df1_20_check = df1_20_check['check_Proof'].mean() 


mean_df1_30_exe_pre_run = df1_30_exe['pre-run'].mean()
mean_df1_30_exe_zkp_calc = df1_30_exe['zkp-calc'].mean()
mean_df1_30_exe_proof_gen = df1_30_exe['proof_gen'].mean()
mean_df1_30_exe_verify_save = df1_30_exe['verify_save'].mean()
mean_df1_30_check = df1_30_check['check_Proof'].mean()

mean_df1_40_exe_pre_run = df1_40_exe['pre-run'].mean()
mean_df1_40_exe_zkp_calc = df1_40_exe['zkp-calc'].mean()
mean_df1_40_exe_proof_gen = df1_40_exe['proof_gen'].mean()
mean_df1_40_exe_verify_save = df1_40_exe['verify_save'].mean()
mean_df1_40_check = df1_40_check['check_Proof'].mean()

mean_df1_50_exe_pre_run = df1_50_exe['pre-run'].mean()
mean_df1_50_exe_zkp_calc = df1_50_exe['zkp-calc'].mean()
mean_df1_50_exe_proof_gen = df1_50_exe['proof_gen'].mean()
mean_df1_50_exe_verify_save = df1_50_exe['verify_save'].mean()
mean_df1_50_check = df1_50_check['check_Proof'].mean()

mean_df1_60_exe_pre_run = df1_60_exe['pre-run'].mean()
mean_df1_60_exe_zkp_calc = df1_60_exe['zkp-calc'].mean()
mean_df1_60_exe_proof_gen = df1_60_exe['proof_gen'].mean()
mean_df1_60_exe_verify_save = df1_60_exe['verify_save'].mean()
mean_df1_60_check = df1_60_check['check_Proof'].mean()

mean_df1_70_exe_pre_run = df1_70_exe['pre-run'].mean()
mean_df1_70_exe_zkp_calc = df1_70_exe['zkp-calc'].mean()
mean_df1_70_exe_proof_gen = df1_70_exe['proof_gen'].mean()
mean_df1_70_exe_verify_save = df1_70_exe['verify_save'].mean()
mean_df1_70_check = df1_70_check['check_Proof'].mean()

mean_df1_80_exe_pre_run = df1_80_exe['pre-run'].mean()
mean_df1_80_exe_zkp_calc = df1_80_exe['zkp-calc'].mean()
mean_df1_80_exe_proof_gen = df1_80_exe['proof_gen'].mean()
mean_df1_80_exe_verify_save = df1_80_exe['verify_save'].mean()
mean_df1_80_check = df1_80_check['check_Proof'].mean()

mean_df1_90_exe_pre_run = df1_90_exe['pre-run'].mean()
mean_df1_90_exe_zkp_calc = df1_90_exe['zkp-calc'].mean()
mean_df1_90_exe_proof_gen = df1_90_exe['proof_gen'].mean()
mean_df1_90_exe_verify_save = df1_90_exe['verify_save'].mean()
mean_df1_90_check = df1_90_check['check_Proof'].mean()


mean_df1_100_exe_pre_run = df1_100_exe['pre-run'].mean()
mean_df1_100_exe_zkp_calc = df1_100_exe['zkp-calc'].mean()
mean_df1_100_exe_proof_gen = df1_100_exe['proof_gen'].mean()
mean_df1_100_exe_verify_save = df1_100_exe['verify_save'].mean()
mean_df1_100_check =df1_100_check['check_Proof'].mean()
print("1 DIGIT--------------")
print("mean_df1_10_check:", mean_df1_10_check)
print("mean_df1_10_exe_pre_run: ", mean_df1_10_exe_pre_run)
print("mean_df1_10_exe_zkp_calc: ", mean_df1_10_exe_zkp_calc)
print("mean_df1_10_exe_proof_gen: ", mean_df1_10_exe_proof_gen)
print("mean_df1_10_exe_verify_save: ", mean_df1_10_exe_verify_save)


print("mean_df1_20_check: ",mean_df1_20_check)
print("mean_df1_20_exe_pre_run: ", mean_df1_20_exe_pre_run)
print("mean_df1_20_exe_zkp_calc: ",mean_df1_20_exe_zkp_calc)
print("mean_df1_20_exe_proof_gen: " , mean_df1_20_exe_proof_gen)
print("mean_df1_20_exe_verify_save: " ,mean_df1_20_exe_verify_save)

print("mean_df1_30_check: ", mean_df1_30_check)
print("mean_df1_30_exe_pre_run: ", mean_df1_30_exe_pre_run)
print("mean_df1_30_exe_zkp_calc: ", mean_df1_30_exe_zkp_calc)
print("mean_df1_30_exe_proof_gen: ", mean_df1_30_exe_proof_gen)
print("mean_df1_30_exe_verify_save: " , mean_df1_30_exe_verify_save)

print("mean_df1_40_check: ", mean_df1_40_check)
print("mean_df1_40_exe_pre_run: ", mean_df1_40_exe_pre_run)
print("mean_df1_40_exe_zkp_calc: ", mean_df1_40_exe_zkp_calc)
print("mean_df1_40_exe_proof_gen: ", mean_df1_40_exe_proof_gen)
print("mean_df1_40_exe_verify_save: " , mean_df1_40_exe_verify_save)

print("mean_df1_50_check: ", mean_df1_50_check)
print("mean_df1_50_exe_pre_run: ", mean_df1_50_exe_pre_run)
print("mean_df1_50_exe_zkp_calc: ", mean_df1_50_exe_zkp_calc)
print("mean_df1_50_exe_proof_gen: ", mean_df1_50_exe_proof_gen)
print("mean_df1_50_exe_verify_save: " , mean_df1_50_exe_verify_save)

print("mean_df1_60_check: ", mean_df1_60_check)
print("mean_df1_60_exe_pre_run: ", mean_df1_60_exe_pre_run)
print("mean_df1_60_exe_zkp_calc: ", mean_df1_60_exe_zkp_calc)
print("mean_df1_60_exe_proof_gen: ", mean_df1_60_exe_proof_gen)
print("mean_df1_60_exe_verify_save: " , mean_df1_60_exe_verify_save)

print("mean_df1_70_check: ", mean_df1_70_check)
print("mean_df1_70_exe_pre_run: ", mean_df1_70_exe_pre_run)
print("mean_df1_70_exe_zkp_calc: ", mean_df1_70_exe_zkp_calc)
print("mean_df1_70_exe_proof_gen: ", mean_df1_70_exe_proof_gen)
print("mean_df1_70_exe_verify_save: " , mean_df1_70_exe_verify_save)

print("mean_df1_80_check: ", mean_df1_80_check)
print("mean_df1_80_exe_pre_run: ", mean_df1_80_exe_pre_run)
print("mean_df1_80_exe_zkp_calc: ", mean_df1_80_exe_zkp_calc)
print("mean_df1_80_exe_proof_gen: ", mean_df1_80_exe_proof_gen)
print("mean_df1_80_exe_verify_save: " , mean_df1_80_exe_verify_save)

print("mean_df1_90_check: ", mean_df1_90_check)
print("mean_df1_90_exe_pre_run: ", mean_df1_90_exe_pre_run)
print("mean_df1_90_exe_zkp_calc: ", mean_df1_90_exe_zkp_calc)
print("mean_df1_90_exe_proof_gen: ", mean_df1_90_exe_proof_gen)
print("mean_df1_90_exe_verify_save: " , mean_df1_90_exe_verify_save)

print("mean_df1_100_check: ", mean_df1_100_check)
print("mean_df1_100_exe_pre_run: " , mean_df1_100_exe_pre_run)
print("mean_df1_100_exe_zkp_calc: " , mean_df1_100_exe_zkp_calc)
print("mean_df1_100_exe_proof_gen: " ,mean_df1_100_exe_proof_gen)
print("mean_df1_100_exe_verify_save: ", mean_df1_100_exe_verify_save)
print("--------------")


