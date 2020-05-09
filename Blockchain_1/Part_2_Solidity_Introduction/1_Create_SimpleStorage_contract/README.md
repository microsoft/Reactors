# Instructions

**THIS DIRECTORY IS INTENTIONALLY LEFT BLANK.**

### Goal
This exercise is designed to help you get comfortable with the basics
of building, deploying and testing Ethereum contracts.

### Steps
- Install [Truffle](https://www.trufflesuite.com/truffle) if you have not

- Initialize the 1_Create_SimpleStorage_contract directory as a truffle project using `truffle init`

- Inspect the directory structure. Look for location of
  - Contracts
  -  Migrations
  - Tests

- Add the SimpleStorage contract from down below.

- Add a migration for the contract from down below.

- Use `truffle develop` to compile, deploy and interact with the
  SimpleStorage contract

- Add a test that gets the current value from the SimpleStorage
  contract, changes it to a new value and then fetches the new
  value. Add assertions after the two get calls to ensure you are
  getting what you expect. Feel free to use the test down below.

- Run your tests with `truffle test` from the command line.

## Contract

``` c
pragma solidity >=0.5.0 <0.7.0;

contract SimpleStorage {
    uint storedData;

    constructor() public {
        set(10);
    }

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

## Migration

``` javascript
var SimpleStorage = artifacts.require("SimpleStorage");
module.exports = deployer => {
    deployer.deploy(SimpleStorage);
};⏎ 
```

## Test

``` javascript
const SimpleStorage = artifacts.require("SimpleStorage");
contract('SimpleStorage', (accounts) => {
  it('testing of SimpleStorage', async () => {
    const s = await SimpleStorage.deployed();
    var ret = await s.get();
    assert.equal(10, ret.toNumber(), 'Got the default value back’);
    await s.set(100);
    ret = await s.get();
    assert.equal(100, ret.toNumber(), 'Got the new value back');	
    });
});
```

