const AssetManager = artifacts.require("AssetManager");
const truffleAssert = require('truffle-assertions');

contract('AssetManager', (accounts) => {

    it('testing of AssetManager', async () => {
        const c = await AssetManager.deployed();
        var available = await c.isAvailable("Redmond Reactor", "Property");
        assert.equal(false, available, "Unassigned Property doesn't exist");

        var result = await c.addAsset("Redmond Reactor", "Property", 100, accounts[0]);
        truffleAssert.eventEmitted(result, 'AssetAdded');

        var price = await c.getPrice("Redmond Reactor", "Property");
        assert.equal(100, price.toNumber(), "Price for the Redmond Reactor is 100");

        available = await c.isAvailable("Redmond Reactor", "Property");
        assert.equal(true, available, "Added Property exists");
        available = await c.isAvailable("Redmond Reactor", "Piece");
        assert.equal(false, available, 
            "Asset with the same name but different type doesn't exist");

        // Write an assertion below to check the return value of ResponseMessage.
        assert.equal('something', 'something', 'A correctness property about ResponseMessage of HelloBlockchain');
    });

    it('testing asset transfer of AssetManager', async() => {
        const c = await AssetManager.deployed();

        // Cannot add assets if you are not the asset manager (in this case
        // accounts[0]).

        await truffleAssert.fails(c.addAsset("San Francisco Reactor", "Property", 
           100, {from: accounts[1]}));

        // Cannot transfer assets if they don't exist.

        await truffleAssert.fails(c.transferAsset(accounts[0], accounts[1], 
            "Tel Aviv Reactor", "Property"));

        // Cannot transfer assets if you are not the asset manager (in this case
        // accounts[0]).

        await truffleAssert.fails(c.transferAsset(accounts[0], accounts[1],
            "Redmond Reactor", "Property", {from: accounts[1]}));
    });
});