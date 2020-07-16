const AssetManager = artifacts.require("AssetManager");
const truffleAssert = require('truffle-assertions');

contract('AssetManager', (accounts) => {

    it('testing of AssetManager', async () => {
        const c = await AssetManager.deployed();

        var add = await c.addAsset("Redmond Reactor", "Property", 100, accounts[0]);
        truffleAssert.eventEmitted(add, 'AssetAdded');

        var transfer = await c.transferAsset(accounts[0], accounts[1], "Redmond Reactor", "Property");
        truffleAssert.eventEmitted(transfer, 'AssetTransfer');
    });
});