var Banker = artifacts.require("Banker");
module.exports = deployer => {
    deployer.deploy(Banker);
};