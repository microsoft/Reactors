var AssetManager = artifacts.require("AssetManager");
module.exports = deployer => {
    deployer.deploy(AssetManager);
};