# Instructions

**THIS DIRECTORY IS INTENTIONALLY LEFT BLANK.**

The instructions for this exercise are available in the slides, but
are copied here for your convenience.

* Use either ‘truffle init’ or VS Code to create a new Solidity
  project in this directory

* You can use a text editor and truffle develop or VS Code and Ganache
  to deploy the contracts

* Add the Bank contract from the below in the contracts directory

* Add a migration for the Bank contract to the migrations directory

* Add a test to test this contract in the test directory (you can copy
  the test from the slides if necessary)

* You can use either ’truffle test’ or ‘truffle develop’ (and then run
  ‘test’ from the workspace)

* If you get stuck, you can find a working version in the AssetManager
  directory (or the Completed_Solutions directory) but try to make it
  work before looking in those places.
  
## Contract

``` c
pragma solidity >=0.5.0 <0.7.0;

contract Bank {
    // The keyword "public" makes variables
    // accessible from other contracts
    address public minter;
    mapping (address => uint) public balances;

    // Events allow clients to react to specific
    // contract changes you declare
    event Sent(address from, address to, uint amount);

    // Constructor code is only run when the contract
    // is created
    constructor() public {
        minter = msg.sender;
    }

    // Sends an amount of newly created coins to an address
    // Can only be called by the contract creator
    function mint(address receiver, uint amount) public {
        require(msg.sender == minter, "Sender == Minter");
        require((amount < 1e60), "Amount isn't too big");

        balances[receiver] += amount;
    }

    // Sends an amount of existing coins
    // from any caller to an address
    function sendMoney(address receiver, address sender, uint amount) public {
        require(msg.sender == minter, "Only the banker can authorize transfers");
        require(amount <= balances[sender], "Insufficient balance.");
        balances[sender] -= amount;
        balances[receiver] += amount;
        emit Sent(sender, receiver, amount);
    }

    function getBalance(address account) public view returns (uint) {
        require(msg.sender == account || msg.sender == minter,
           "You cannot get a balance on someone else's account");
        return balances[account];
    }
}
```

## Migration

``` javascript
var Bank = artifacts.require("Bank");
module.exports = deployer => {
    deployer.deploy(Bank);
};
```

## Test

``` javascript
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
```

