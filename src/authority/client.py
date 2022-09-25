
import os
import time
import requests
import base64


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

    #wait for prover to send zokrates code
    while not os.path.exists("main.zok"):

        time.sleep(10)
    print("main.zok exists")


    #compile zokrates code
    os.system("zokrates compile -i main.zok")
    time.sleep(10)

    #os.system("zokrates universal-setup")
    #time.sleep(10)

    #Setup ZKP Circuit --> generate Keys
    os.system("zokrates setup ")
    time.sleep(10)

    #send information of circuit and keys to prover
    send_file_api(PROVER,"out")
    time.sleep(2)
    send_file_api(PROVER, "proving.key")

    #generate verifier Smart contract
    os.system("zokrates export-verifier")
    time.sleep(5)

    #send verifier smart contract to Prover
    send_file_api(PROVER, "verifier.sol")

    #deploy verifier smart contract
    os.system("cp verifier.sol ./contracts")
    os.system("truffle compile")
    time.sleep(10)
    os.system("truffle migrate")
    time.sleep(10)
    os.system("ls build/contracts")
    
    #send information about deployed contract to Verifier
    send_file_api(VERIFIER, "build/contracts/Verifier.json")
    time.sleep(10)
    send_file_api(VERIFIER, "build/contracts/RegisterAndVerify.json")


    send_file_api(PROVER, "build/contracts/Verifier.json")
    time.sleep(10)
    send_file_api(PROVER, "build/contracts/RegisterAndVerify.json")
