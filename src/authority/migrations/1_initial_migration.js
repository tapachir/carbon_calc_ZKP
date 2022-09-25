const Verifier = artifacts.require("Verifier");
const register = artifacts.require("RegisterAndVerify");

module.exports = function (deployer) {

  deployer.deploy(Verifier).then(function() {
    return deployer.deploy(register, Verifier.address);
  });
};
