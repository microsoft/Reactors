var Bank = artifacts.require("Bank");
var AssetManager = artifacts.require("AssetManager");
var Banker = artifacts.require("Banker");

module.exports = deployer => {
    deployer.deploy(Bank);
    deployer.deploy(AssetManager);
    deployer.deploy(Banker);
};