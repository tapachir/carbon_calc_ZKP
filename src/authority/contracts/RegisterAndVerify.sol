pragma solidity ^0.8.0;

import "./verifier.sol";

contract RegisterAndVerify is Verifier{
    bytes32[] validProofs;
    address verifierContract;
    event Verification(
        bytes32 hashedProof,
        bool result
    );
 
    constructor(address _verifierContract)  {
     verifierContract = _verifierContract;   
   }

 
   function verifyProof(string calldata _fullProof, Proof calldata proof, uint[2] calldata input) public returns(bool r){
       Verifier verifierInstance = Verifier(verifierContract);
       bool result = verifierInstance.verifyTx(proof,input);
       
       if(result){
           bytes32 hashed = keccak256(abi.encodePacked(_fullProof));
           validProofs.push(hashed);
           emit Verification( hashed, result);
           return true;
       } else {

            bytes32 hashed = keccak256(abi.encodePacked(_fullProof));
            emit Verification( hashed, result);

           return false;
       }
           
       }

    function getProofs() public returns(bytes32){
        return validProofs[0];
    }
   }
 