
import os
import time
import requests
import base64
import csv  

AUTHORITY = "http://172.22.0.12:8001"
PROVER = "http://172.22.0.10:8000"
VERIFIER = "http://172.22.0.11:8002"


def get_file_api(filename):
    r = requests.get("172.22.0.12:8001/file/"+filename)
    print(r.content)

    with open(filename, "wb") as f:
        f.write(r.content)
def send_file_api(recipient,filename):
    with open(filename, "rb")  as image_file:
        encoded_string = base64.b64encode(image_file.read())
    if "/" in filename:
        filename = filename.replace("/","_")
    r = requests.post(recipient+"/api/file/"+filename,data=encoded_string ,headers={'User-Agent':'test'})
    print(r.content)


if __name__ == "__main__":
    
    #send existing zokrates code to AUTHORITY
    send_file_api(AUTHORITY,"main.zok")

    time.sleep(10)
    
    #wait till authority responds with information about setup circuit
    while not os.path.exists("out") and not os.path.exists("proving.key"):
        time.sleep(10)
    print("out and proving key exist")

    # compile Zokrates code to use it 
    os.system("zokrates compile -i main.zok")



    command_str = "python3 calculation.py"
    compute_witnes_cmd = "zokrates compute-witness -a"
    for x in range(1,51):
        #command_str = command_str + " " + str(x)+ "0"
        #compute_witnes_cmd = compute_witnes_cmd + " " + str(x)+"0"
        command_str = command_str + " " + str(x)
        compute_witnes_cmd = compute_witnes_cmd + " " + str(x)
    for y in range(1,101):
        command_str = command_str + " " + str(0)
        compute_witnes_cmd = compute_witnes_cmd + " " + str(0)
    for z in range(51,101):
        #command_str = command_str + " " + str(z)+"0"
        #compute_witnes_cmd = compute_witnes_cmd + " " + str(z)+"0"
        command_str = command_str + " " + str(z)
        compute_witnes_cmd = compute_witnes_cmd + " " + str(z)

    # pre-run calculation and export result 
    # 1 2 3 0 0 0 are the factors comming from supplier
    # 0 0 0 4 5 6 are the factors comming from LCA Database
    # st1 = time.time()
    # os.system("python3 calculation.py 1 2 3 0 0 0 0 0 0 4 5 6")
    # et = time.time()
    # elapsed_time = et - st1
    # print('Execution time Pre-Run 6:', elapsed_time, 'seconds')
    # result1 = open("result.txt", "r")

    header = ['run', 'pre-run', 'zkp-calc',"proof_gen" ,'verify_save']
    data = []

    with open('results/exe_times.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)


        for i in range(0,10):
            # write the data
            writer.writerow(data)
            st11 = time.time()
            #os.system("python3 calculation.py 1 2 3 4 5 6 7 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 10 11 12 13 14 15 16")
            #os.system("python3 calculation.py 100 200 300 0 0 0 0 0 0 400 500 600")
            os.system(command_str)
            et11 = time.time()
            elapsed_time11 = et11- st11
            print('Execution time Pre-Run: 8 ', elapsed_time11, 'seconds')
            result = open("result.txt", "r")
            data.append(i)
            data.append(elapsed_time11)

            # st12 = time.time()
            # os.system("python3 calculation.py 1 2 3 4 5 6 7 8 9 10 11 12 14 14 15 16 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32")
            # et12 = time.time()
            # elapsed_time12 = et12 - st12
            # print('Execution time Pre-Run: 32 ', elapsed_time12, 'seconds')
            # result3 = open("result.txt", "r")


            # st13 = time.time()
            # os.system("python3 calculation.py 1 2 3 4 5 6 7 8 9 10 11 12 14 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 57 58 59 60 61 62")
            # et13 = time.time()
            # elapsed_time13 = et13 - st13
            # print('Execution time Pre-Run: 64 ', elapsed_time13, 'seconds')
            # result4 = open("result.txt", "r")





            # st21 = time.time()
            # os.system("zokrates compute-witness -a 1 2 3 0 0 0 0 0 0 4 5 6 " +result2.readline())
            # et21 = time.time()
            # elapsed_time21 = et21 - st21
            # print('Execution time Pre-Run 6:', elapsed_time21, 'seconds')

            st22 = time.time()
            os.system(compute_witnes_cmd+" "+result.readline())
            #os.system("zokrates compute-witness -a 100 200 300 0 0 0 0 0 0 400 500 600 " +result.readline())
            et22 = time.time()
            elapsed_time22 = et22- st22
            print('Execution time zkp calc: 20 ', elapsed_time22, 'seconds')
            data.append(elapsed_time22)

            # st23 = time.time()
            # os.system("zokrates compute-witness -a 1 2 3 4 5 6 7 8 9 10 11 12 14 14 15 16 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 "+result3.readline())
            # et23 = time.time()
            # elapsed_time23 = et23 - st23
            # print('Execution time Pre-Run: 32 ', elapsed_time23, 'seconds')


            # st24 = time.time()
            # os.system("zokrates compute-witness -a 1 2 3 4 5 6 7 8 9 10 11 12 14 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 57 58 59 60 61 62 " +result4.readline())
            # et24 = time.time()
            # elapsed_time24 = et24 - st24
            # print('Execution time Pre-Run: 64 ', elapsed_time24, 'seconds')






            # # run zkp calculation with same inputs (as pre-run) plus the result of the pre-run
            # st2 = time.time()
            # os.system("zokrates compute-witness -a 1 2 3 0 0 0 0 0 0 4 5 6 "+result.readline())
            # et2 = time.time()
            # elapsed_time2 = et2 - st2
            # print('Execution time ZKP Calculation:', elapsed_time2, 'seconds')


            # generate proof
            st3 = time.time()
            os.system("zokrates generate-proof ")
            et3 =  time.time()
            elapsed_time3 = et3 - st3
            print('Execution time Proof Generation:', elapsed_time3, 'seconds')
            data.append(elapsed_time3)


            # wait for Information about Verifier Smart contract
            while not os.path.exists("build_contracts_Verifier.json") and not os.path.exists("build_contracts_RegisterAndVerify.json")  :
                time.sleep(1)
            print("verifier.json exists")

            while not os.path.exists("build_contracts_RegisterAndVerify.json")  :
                    time.sleep(1)
            print("RegisterAndVerify.json exists")


            # move and format received file
            os.system("mkdir -p build/contracts/")
            os.system("cp build_contracts_Verifier.json build/contracts/Verifier.json")
            os.system("cp build_contracts_RegisterAndVerify.json build/contracts/RegisterAndVerify.json")
            os.system("ls build/contracts")


            st4 = time.time()
            # Verify Result with proof using the deployed Verifier Smart contract
            os.system("truffle exec truffle_script.js")
            et4 =  time.time()
            elapsed_time4= et4 - st4
            print('Time to verify and save proof in SC:', elapsed_time4, 'seconds')
            data.append(elapsed_time4)
            writer.writerow(data)
            # send result of pre-run calculation to Verifier
        #send_file_api(VERIFIER,"result.txt")
            data.clear()
            print("size proof ", os.path.getsize("proof.json"))
            print("size witness ", os.path.getsize("witness"))

    
    with open('results/exe_times.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
        # send proof to Verifier
send_file_api(VERIFIER,"result.txt")
send_file_api(VERIFIER,"proof.json")

