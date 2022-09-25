import pandas as pd


df1_10_exe = pd.read_csv (r'1_digit_runs/1_digit_10_exe_times.csv') 
df1_10_check = pd.read_csv (r'1_digit_runs/1_digit_10_check_times.csv') 
df1_20_exe = pd.read_csv (r'1_digit_runs/1_digit_20_exe_times.csv') 
df1_20_check = pd.read_csv (r'1_digit_runs/1_digit_20_check_times.csv') 
df1_30_exe = pd.read_csv (r'1_digit_runs/1_digit_30_exe_times.csv') 
df1_30_check = pd.read_csv (r'1_digit_runs/1_digit_30_check_times.csv') 
df1_100_exe = pd.read_csv (r'1_digit_runs/1_digit_100_exe_times.csv') 
df1_100_check = pd.read_csv (r'1_digit_runs/1_digit_100_check_times.csv') 



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

print("mean_df1_100_check: ", mean_df1_100_check)
print("mean_df1_100_exe_pre_run: " , mean_df1_100_exe_pre_run)
print("mean_df1_100_exe_zkp_calc: " , mean_df1_100_exe_zkp_calc)
print("mean_df1_100_exe_proof_gen: " ,mean_df1_100_exe_proof_gen)
print("mean_df1_100_exe_verify_save: ", mean_df1_100_exe_verify_save)
print("--------------")

df2_10_exe = pd.read_csv (r'2_digits_runs/2_digits_10_exe_times.csv') 
df2_10_check = pd.read_csv (r'2_digits_runs/2_digits_10_check_times.csv') 
df2_20_exe = pd.read_csv (r'2_digits_runs/2_digits_20_exe_times.csv') 
df2_20_check = pd.read_csv (r'2_digits_runs/2_digits_20_check_times.csv') 
df2_30_exe = pd.read_csv (r'2_digits_runs/2_digits_30_exe_times.csv') 
df2_30_check = pd.read_csv (r'2_digits_runs/2_digits_30_check_times.csv') 
df2_100_exe = pd.read_csv (r'2_digits_runs/2_digits_100_exe_times.csv') 
df2_100_check = pd.read_csv (r'2_digits_runs/2_digits_100_check_times.csv') 



# block 1 - simple stats
mean_df2_10_exe_pre_run = df2_10_exe['pre-run'].mean()
mean_df2_10_exe_zkp_calc = df2_10_exe['zkp-calc'].mean()
mean_df2_10_exe_proof_gen = df2_10_exe['proof_gen'].mean()
mean_df2_10_exe_verify_save = df2_10_exe['verify_save'].mean()
mean_df2_10_check = df2_10_check['check_Proof'].mean()



mean_df2_20_exe_pre_run = df2_20_exe['pre-run'].mean()
mean_df2_20_exe_zkp_calc = df2_20_exe['zkp-calc'].mean()
mean_df2_20_exe_proof_gen = df2_20_exe['proof_gen'].mean()
mean_df2_20_exe_verify_save = df2_20_exe['verify_save'].mean()
mean_df2_20_check = df2_20_check['check_Proof'].mean() 


mean_df2_30_exe_pre_run = df2_30_exe['pre-run'].mean()
mean_df2_30_exe_zkp_calc = df2_30_exe['zkp-calc'].mean()
mean_df2_30_exe_proof_gen = df2_30_exe['proof_gen'].mean()
mean_df2_30_exe_verify_save = df2_30_exe['verify_save'].mean()
mean_df2_30_check = df2_30_check['check_Proof'].mean()


mean_df2_100_exe_pre_run = df2_100_exe['pre-run'].mean()
mean_df2_100_exe_zkp_calc = df2_100_exe['zkp-calc'].mean()
mean_df2_100_exe_proof_gen = df2_100_exe['proof_gen'].mean()
mean_df2_100_exe_verify_save = df2_100_exe['verify_save'].mean()
mean_df2_100_check =df2_100_check['check_Proof'].mean()
print("2 DIGIT--------------")

print("mean_df2_10_check:", mean_df2_10_check)
print("mean_df2_10_exe_pre_run: ", mean_df2_10_exe_pre_run)
print("mean_df2_10_exe_zkp_calc: ", mean_df2_10_exe_zkp_calc)
print("mean_df2_10_exe_proof_gen: ", mean_df2_10_exe_proof_gen)
print("mean_df2_10_exe_verify_save: ", mean_df2_10_exe_verify_save)


print("mean_df2_20_check: ",mean_df2_20_check)
print("mean_df2_20_exe_pre_run: ", mean_df2_20_exe_pre_run)
print("mean_df2_20_exe_zkp_calc: ",mean_df2_20_exe_zkp_calc)
print("mean_df2_20_exe_proof_gen: " , mean_df2_20_exe_proof_gen)
print("mean_df2_20_exe_verify_save: " ,mean_df2_20_exe_verify_save)

print("mean_df2_30_check: ", mean_df2_30_check)
print("mean_df2_30_exe_pre_run: ", mean_df2_30_exe_pre_run)
print("mean_df2_30_exe_zkp_calc: ", mean_df2_30_exe_zkp_calc)
print("mean_df2_30_exe_proof_gen: ", mean_df2_30_exe_proof_gen)
print("mean_df2_30_exe_verify_save: " , mean_df2_30_exe_verify_save)

print("mean_df2_100_check: ", mean_df2_100_check)
print("mean_df2_100_exe_pre_run: " , mean_df2_100_exe_pre_run)
print("mean_df2_100_exe_zkp_calc: " , mean_df2_100_exe_zkp_calc)
print("mean_df2_100_exe_proof_gen: " ,mean_df2_100_exe_proof_gen)
print("mean_df2_100_exe_verify_save: ", mean_df2_100_exe_verify_save)

print("--------------")



df3_10_exe = pd.read_csv (r'3_digits_runs/3_digits_10_exe_times.csv') 
df3_10_check = pd.read_csv (r'3_digits_runs/3_digits_10_check_times.csv') 
df3_20_exe = pd.read_csv (r'3_digits_runs/3_digits_20_exe_times.csv') 
df3_20_check = pd.read_csv (r'3_digits_runs/3_digits_20_check_times.csv') 
df3_30_exe = pd.read_csv (r'3_digits_runs/3_digits_30_exe_times.csv') 
df3_30_check = pd.read_csv (r'3_digits_runs/3_digits_30_check_times.csv') 
df3_100_exe = pd.read_csv (r'3_digits_runs/3_digits_100_exe_times.csv') 
df3_100_check = pd.read_csv (r'3_digits_runs/3_digits_100_check_times.csv') 



# block 1 - simple stats
mean_df3_10_exe_pre_run = df3_10_exe['pre-run'].mean()
mean_df3_10_exe_zkp_calc = df3_10_exe['zkp-calc'].mean()
mean_df3_10_exe_proof_gen = df3_10_exe['proof_gen'].mean()
mean_df3_10_exe_verify_save = df3_10_exe['verify_save'].mean()
mean_df3_10_check = df3_10_check['check_Proof'].mean()



mean_df3_20_exe_pre_run = df3_20_exe['pre-run'].mean()
mean_df3_20_exe_zkp_calc = df3_20_exe['zkp-calc'].mean()
mean_df3_20_exe_proof_gen = df3_20_exe['proof_gen'].mean()
mean_df3_20_exe_verify_save = df3_20_exe['verify_save'].mean()
mean_df3_20_check = df3_20_check['check_Proof'].mean() 


mean_df3_30_exe_pre_run = df3_30_exe['pre-run'].mean()
mean_df3_30_exe_zkp_calc = df3_30_exe['zkp-calc'].mean()
mean_df3_30_exe_proof_gen = df3_30_exe['proof_gen'].mean()
mean_df3_30_exe_verify_save = df3_30_exe['verify_save'].mean()
mean_df3_30_check = df3_30_check['check_Proof'].mean()


mean_df3_100_exe_pre_run = df3_100_exe['pre-run'].mean()
mean_df3_100_exe_zkp_calc = df3_100_exe['zkp-calc'].mean()
mean_df3_100_exe_proof_gen = df3_100_exe['proof_gen'].mean()
mean_df3_100_exe_verify_save = df3_100_exe['verify_save'].mean()
mean_df3_100_check =df3_100_check['check_Proof'].mean()
print("3 DIGIT--------------")

print("mean_df3_10_check:", mean_df3_10_check)
print("mean_df3_10_exe_pre_run: ", mean_df3_10_exe_pre_run)
print("mean_df3_10_exe_zkp_calc: ", mean_df3_10_exe_zkp_calc)
print("mean_df3_10_exe_proof_gen: ", mean_df3_10_exe_proof_gen)
print("mean_df3_10_exe_verify_save: ", mean_df3_10_exe_verify_save)


print("mean_df3_20_check: ",mean_df3_20_check)
print("mean_df3_20_exe_pre_run: ", mean_df3_20_exe_pre_run)
print("mean_df3_20_exe_zkp_calc: ",mean_df3_20_exe_zkp_calc)
print("mean_df3_20_exe_proof_gen: " , mean_df3_20_exe_proof_gen)
print("mean_df3_20_exe_verify_save: " ,mean_df3_20_exe_verify_save)

print("mean_df3_30_check: ", mean_df3_30_check)
print("mean_df3_30_exe_pre_run: ", mean_df3_30_exe_pre_run)
print("mean_df3_30_exe_zkp_calc: ", mean_df3_30_exe_zkp_calc)
print("mean_df3_30_exe_proof_gen: ", mean_df3_30_exe_proof_gen)
print("mean_df3_30_exe_verify_save: " , mean_df3_30_exe_verify_save)

print("mean_df3_100_check: ", mean_df3_100_check)
print("mean_df3_100_exe_pre_run: " , mean_df3_100_exe_pre_run)
print("mean_df3_100_exe_zkp_calc: " , mean_df3_100_exe_zkp_calc)
print("mean_df3_100_exe_proof_gen: " ,mean_df3_100_exe_proof_gen)
print("mean_df3_100_exe_verify_save: ", mean_df3_100_exe_verify_save)

print("--------------")







