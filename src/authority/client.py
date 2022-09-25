
import os
import time
import requests
import base64

import csv  

AUTHORITY = "http://172.22.0.12:8001"
PROVER = "http://172.22.0.10:8000"
VERIFIER = "http://172.22.0.11:8002"


def get_file_api(filename):
    r = requests.get("172.22.0.10:8000/file/"+filename)
    print(r.content)

    with open(filename, "wb") as f:
        f.write(r.content)

def send_file_api(recipient,filename):
    
    with open(filename, "rb")  as image_file:
        encoded_string = base64.b64encode(image_file.read())
    if "/" in filename:
        filename = filename.replace("/","_")
    r = requests.post(recipient+"/api/file/"+filename,data=encoded_string, headers={'User-Agent':'test'})
    print(r.content)

if __name__ == "__main__":
    header = ['compile', 'setup',"export_ver" 'truffle_compile', 'truffle_migrate']
    data = []

    with open('results/exe_times.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        #wait for prover to send zokrates code
        while not os.path.exists("main.zok"):

            time.sleep(10)
        print("main.zok exists")

        st1 = time.time()
        #compile zokrates code
        os.system("zokrates compile -i main.zok")
        et1 = time.time()
        elapsed_time1 = et1- st1
        print('Execution time compile:  ', elapsed_time1, 'seconds')
        data.append(elapsed_time1)
        #os.system("zokrates universal-setup")
        #time.sleep(10)
        time.sleep(10)

        st2 = time.time()
        #Setup ZKP Circuit --> generate Keys
        os.system("zokrates setup ")
        et2 = time.time()
        elapsed_time2 = et2- st2
        print('Execution time setup:  ', elapsed_time2, 'seconds')
        data.append(elapsed_time2)
        time.sleep(10)
        os.system("ls")
        #send information of circuit and keys to prover
        #send_file_api(PROVER,"out")
        time.sleep(2)
        #send_file_api(PROVER, "proving.key")

        #generate verifier Smart contract
        st3 = time.time()
        os.system("zokrates export-verifier")
        et3 = time.time()
        elapsed_time3 = et3- st3
        print('Execution time export:  ', elapsed_time3, 'seconds')
        data.append(elapsed_time3)
        time.sleep(5)

        #send verifier smart contract to Prover
        #send_file_api(PROVER, "verifier.sol")

        #deploy verifier smart contract
        os.system("cp verifier.sol ./contracts")

        st4 = time.time()
        os.system("truffle compile")
        et4 = time.time()
        elapsed_time4 = et4- st4
        print('Execution time truffle compile:  ', elapsed_time4, 'seconds')
        data.append(elapsed_time4)
        time.sleep(5)

        st5= time.time()
        os.system("truffle migrate")
        et5 = time.time()
        elapsed_time5 = et5- st5
        print('Execution time truffle migrate:  ', elapsed_time5, 'seconds')
        data.append(elapsed_time5)
        time.sleep(10)
        os.system("ls build/contracts")
        writer.writerow(data)
            # #send information about deployed contract to Verifier
            # send_file_api(VERIFIER, "build/contracts/Verifier.json")
            # time.sleep(10)
            # send_file_api(VERIFIER, "build/contracts/RegisterAndVerify.json")


            # send_file_api(PROVER, "build/contracts/Verifier.json")
            # time.sleep(10)
            # send_file_api(PROVER, "build/contracts/RegisterAndVerify.json")

        print("size verifcation key ", os.path.getsize("verification.key"))
        print("size proving key ", os.path.getsize("proving.key"))
        print("size out ", os.path.getsize("out"))

      
    with open('results/exe_times.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)