
import os
import time


AUTHORITY = "http://172.22.0.12:8001"
PROVER = "http://172.22.0.10:8000"
VERIFIER = "http://172.22.0.11:8002"



if __name__ == "__main__":
    os.system("truffle console")

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

    # wait for result of pre-run calculation
    while not os.path.exists("result.txt") :
            time.sleep(10)
    print("result.txt exists")
    
    # wait for proof of calculation
    while not os.path.exists("proof.json") :
        time.sleep(10)
    print("proof.json exists")

    # check if result of pre-run calculation matches result from proof
    # --> hashes of result are compared (since proof only contains hash-value)
    # --> export result of check
    os.system("python3 check_result_match_proof.py")
    while not os.path.exists("result_validation.txt") :
        time.sleep(10)
    
    # read the result of check 
    result = open("result.txt", "r").readline()
    if result == "false":
        print("received calculation result is not matching the received proof")
        exit

        
    # Verify Result with proof using the deployed Verifier Smart contract
    os.system("truffle exec truffle_script.js")

