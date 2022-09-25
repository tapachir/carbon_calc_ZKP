# ZKP Carbon Calculation

This is the prototyp for running off-chain calculations of carbon-emissions using ZoKrates and verifying the result inside a Docker environment. The Docker Containers communicate via their APIs.

## Dependencies:
- Docker (min v20.10.14 confirmed)
- Docker-compose (min v1.29.2 confirmed)

## How to run:
- ```docker-compose up ```
- to end execution -> ```docker-compose down ```

Involved Parties: 
- Trusted Pary (or Authority/Auditor)
- Prover (Party that executes calculation)
- Verifier (Party that verifies result of calculation)
- local Blockchain instance (Ganache)

### Workflow:
- Prover sends Zokrates code (main.zok) to trusted Authority
- Trusted Authority compiles code and initiates Zokrates one-time setup. The setup generates verification- and proving-keys. The verfication-key is used to generate a verifier contract that is deployed on the local blockchain instance. Together with the verifier Contract, the RegisterAndVerify Contract is deployed. This contract is storing the succussful verified Proofs. The proving key is sent to the Prover.
- The prover calculates the result,then exeutes the Zokrates code (main.zok) locally and generates the resulting witness. Using the witness the prover generates a proof. It then verifies the Proof with the deployed Smart Conract. In the case of a successful verification, the proof is stored in RegisterAndVerify Contract. The proof and the result are then sent to the the verifier.
- The verifier verifies the result by calling retrieving the saved Proofs from the RegisterAndVerify Contract. Is the proof present and matching with the prior received proof the calculation and the corresponding result are correct.

## Logic:
Main logic of the different parties is in the client.py files. 

## WiP:
This implemention is currently setup to run a hardcoded one-time calculation that is verifiable. 
Execution Time not accurate due to used sleep-timer.

## Evaluation:
The branch "evaluation" contains the code that was used for running performance experiments. The folder diagram/eval contains the results of the experiments and the corressponding diagrams.