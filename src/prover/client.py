
import os
import time
import requests
import base64

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

    
    # pre-run calculation and export result 
    # 1 2 3 0 0 0 are the factors comming from supplier
    # 0 0 0 4 5 6 are the factors comming from LCA Database
    os.system("python3 calculation.py 1 2 3 0 0 0 0 0 0 4 5 6")
    result = open("result.txt", "r")

    # run zkp calculation with same inputs (as pre-run) plus the result of the pre-run
    os.system("zokrates compute-witness -a 1 2 3 0 0 0 0 0 0 4 5 6 "+result.readline())

    # generate proof
    os.system("zokrates generate-proof ")

    
  

     # wait for Information about Verifier Smart contract
    while not os.path.exists("build_contracts_Verifier.json") and not os.path.exists("build_contracts_RegisterAndVerify.json")  :
        time.sleep(10)
    print("verifier.json exists")

    while not os.path.exists("build_contracts_RegisterAndVerify.json")  :
            time.sleep(10)
    print("RegisterAndVerify.json exists")


    # move and format received file
    os.system("mkdir -p build/contracts/")
    os.system("cp build_contracts_Verifier.json build/contracts/Verifier.json")
    os.system("cp build_contracts_RegisterAndVerify.json build/contracts/RegisterAndVerify.json")
    os.system("ls build/contracts")


            
    # Verify Result with proof using the deployed Verifier Smart contract
    os.system("truffle exec truffle_script.js")

    # send result of pre-run calculation to Verifier
    send_file_api(VERIFIER,"result.txt")


    # send proof to Verifier
    send_file_api(VERIFIER,"proof.json")