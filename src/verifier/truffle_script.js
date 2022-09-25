// Contracts
const Verifier = artifacts.require("RegisterAndVerify")
const fs = require('fs');



module.exports = async function(callback) {
  try {
    // Fetch accounts from wallet - these are unlocked
    const accounts = await web3.eth.getAccounts()
    console.log(accounts[0])
    // Fetch the deployed exchange
    const verifier = await Verifier.deployed()
    console.log('verifier fetched', verifier.address)
    const proof = JSON.parse(fs.readFileSync("proof.json"))


    
    const savedProof = await Verifier.deployed().then(function(instance){return instance.getProofs.call()})
    //console.log("Saved Proof from Smart Contract", savedProof)

    const hashedLocal = web3.utils.keccak256((proof.toString()));
    
    if (savedProof != hashedLocal){
      console.log("PROOFS DONT MATCH")
    }

    if (hashedLocal == savedProof){
      console.log("-------------------------------------------------------------- ")
      console.log("RECEIVED PROOF IS CORRECT AND HAS BEEN VERIFIED BY PROVER. ")
      console.log("-------------------------------------------------------------- ")

    }




  }
  catch(error) {
    console.log(error)
  }

  callback()
}


