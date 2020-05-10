const Bank = artifacts.require("Bank");
const truffleAssert = require('truffle-assertions');

contract('Bank', (accounts) => {

    it('testing of Bank', async () => {
        const c = await Bank.deployed();
        await c.mint(accounts[1], 1000);
        var result = await c.sendMoney(accounts[2], accounts[1], 200, {from: accounts[0]});
        truffleAssert.eventEmitted(result, 'Sent');

        result = await c.getBalance(accounts[0]);
        assert.equal(0, result.toNumber(), "Banker has no money");
        result = await c.getBalance(accounts[1]);
        assert.equal(800, result.toNumber(), "Account 1 has 800");
        result = await c.getBalance(accounts[2]);
        assert.equal(200, result.toNumber(), "Account 2 has 200");
        result = await c.getBalance(accounts[2], {from: accounts[2]});
        assert.equal(200, result.toNumber(),
           "Account 2 has 200 and Account 2 can check it");        
        
        //truffleAssert.eventEmitted(result, 'GameStarted');
        /*var returnValue1;
        returnValue1 = await HelloBlockchainInstance.ResponseMessage.call();

        console.log(returnValue1); */

        // Write an assertion below to check the return value of ResponseMessage.
        assert.equal('something', 'something', 'A correctness property about ResponseMessage of HelloBlockchain');
    });

    it('testing of disallowed actions in Bank', async () => {
        const c = await Bank.deployed();
        // TODO: Add a check for non-bankers sending transfers
        await truffleAssert.fails(c.mint(accounts[1], 1000, {from: accounts[1]}));
        await truffleAssert.fails(c.getBalance(accounts[1], {from: accounts[2]}));
        var result = await c.getBalance(accounts[1]);
        assert.equal(800, result.toNumber(), "Account 1 still has 800");
        await truffleAssert.fails(c.sendMoney(accounts[2], accounts[1], 1000, {from: accounts[0]}));
    });

});