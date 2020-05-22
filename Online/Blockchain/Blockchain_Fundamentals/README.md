# Blockchain Fundamentals

This directory has the demo used during the Blockchain foundations livestream on Twitch.

The purpose of this demo is to get started with building and testing your own blockchain for the Ethereum.

## Resources
- [Ethereum website](https://ethereum.org/)
- [Solidity docs](https://solidity.readthedocs.io/en/latest/index.html)  

## Pre-reqs to complete demo
- [VS Code](https://code.visualstudio.com/)
- [npms and Node.js](https://www.npmjs.com/get-npm)
- The example here uses:
  - [truffle](https://www.trufflesuite.com/truffle) as the development framework for Ethereum 
  - [ganache-cli](https://github.com/trufflesuite/ganache-cli) as the Ethereum client for testing and development

## Demo steps
1. Run `truffle init` in the directory where you want to create your new truffle project. Then open up the directory in VS Code.
2. Inspect the directory structure that truffle created. Look for location of:
  - Contracts/
  - Migrations/
  - Tests/
  - truffle-config.js
3. Add a new contract called: **Coin.sol**.
``` c
pragma solidity >= 0.5.0 < 0.7.0;

contract Coin {
  address public minter;
  mapping (address => uint) public balances;

  event Sent(address from, address to, uint amount);

  constructor() public {
    minter = msg.sender;
   }

  function mint(address receiver, uint amount) public {
    require(msg.sender == minter, "Sender must be minter");
    require(amount < 1e60, "Amount must be less");
    balances[receiver] += amount;
  }

  function send(address receiver, address sender, uint amount) public {
    require(amount <= balances[sender], "Not enough money");
    balances[sender] -= amount;
    balances[receiver] += amount;
    emit Sent(msg.sender, receiver, amount);
  }
}
```
4. Add a new migration called: **2_deploy_contracts.js**
``` javascript
var Coin = artifacts.require("Coin");
module.exports = deployer => {
    deployer.deploy(Coin);
};⏎ 
```
5. Add a new test called: **Coin.js**.
``` javascript
const Coin = artifacts.require("Coin");
const truffleAssert = require('truffle-assertions');

contract('Coin', (accounts) => {
  it('should mint and send coins', async() => {
    let c = await Coin.deployed();
    await c.mint(accounts[1], 1000);
    let result = await c.send(accounts[2], accounts[1], 200);
    truffleAssert.eventEmitted(result, 'Sent');
  });
});
```
6. Start up the Ethereum client by running `ganache-cli` in a terminal window.

7. In your editor, open up `truffle-config.js` and replace the contents so it looks like this with the host and port pointing to your ganache-cli client:
``` javascript
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*"
    }
  }
};
```
8. Go back to your terminal, open up a new window, and then compile the contract by running `truffle compile` in the terminal.

9. Then migrate your contract by running `truffle migrate`.

10. Now, it's time to test your contract. First run `npm install truffle-assertions` to install that package for this project. You will see warnings that there is no **package.json** file, but that's okay. Then run the test with `truffle test`.
