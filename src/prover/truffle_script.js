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


    const resultVerified = await Verifier.deployed().then(function(instance){return instance.verifyProof(proof.toString(), proof.proof, proof.inputs)})
    console.log("Result and Proof valid: ", resultVerified.logs[0].args.result)


    const savedProof = await Verifier.deployed().then(function(instance){return instance.getProofs.call()})
    console.log("Saved Proof from Smart Contract", savedProof)

    const hashedLocal = web3.utils.keccak256((proof.toString()));
    
    if (savedProof != resultVerified.logs[0].args.hashedProof){
      console.log("PROOFS DONT MATCH")
    }

    if (hashedLocal == resultVerified.logs[0].args.hashedProof && hashedLocal == savedProof){
      console.log("PROOFS MATCH")
    }

    


  }
  catch(error) {
    console.log(error)
  }

  callback()
}


