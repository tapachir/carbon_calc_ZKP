
import json
import hashlib

#get calculated Result from received result file
result = open("result.txt", "r")

# hash result with same algorithm as in zokrates
temp_result = (hex(int(result.readline())))[2:]
while len(temp_result) < 128:
    temp_result = "0"+ temp_result

prepared_result = bytes.fromhex(temp_result)
result_hash = hashlib.sha256(prepared_result).hexdigest()


#get hash of result from received proof 
jsonFile = open('proof.json', 'r')
values = json.load(jsonFile)
jsonFile.close()


#clean leading zeros from inputs
input1 = values["inputs"][0][34:]
input2 = values["inputs"][1][34:]

#concanate full Hash from input
concanated_inputs = input1+input2


print("Received Result valid and matching the proof: ", (result_hash==concanated_inputs))

with open("result_validation.txt", "w") as f:
    f.write(str((result_hash==concanated_inputs)))

# print("779d99147b3605d185eb5f9d017ef1aee1c0538dd9730a859f8f2c8ca2001e04")

# s = "779d99147b3605d185eb5f9d017ef1aee1c0538dd9730a859f8f2c8ca2001e04"
# s1 = s[:len(s)//2]
# s2 = s[len(s)//2:]
# print(s1)

# print("next")
# print(s2)


# print("formated")
# print(int(s1,16))

# print("next")
# print(int(s2,16))