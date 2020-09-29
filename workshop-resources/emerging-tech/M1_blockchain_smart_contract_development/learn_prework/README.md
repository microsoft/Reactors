# Content
* [What is a smart contract?](#What-is-a-smart-contract?) 
* [Solidity Data Structures](#Solidity-Data-Structures)
     * [Enum](#Enum)
     * [Struct](#Struct)
     * [Mappings](#Mappings)
     * [Global vars / Objects](#Global-vars-/-Objects)
* [Using the Truffle Suite](#Using-the-Truffle-Suite)
     * [Using the Blockchain Development Kit from Microsoft](#Using-the-Blockchain-Development-Kit-from-Microsoft)
     * [Set-up](#Set-up)
     * [HelloBlockchain.sol](#HelloBlockchain.sol)
     * [Test the contract](#Test-the-contract)
     * [Deploy the contract](#Deploy-the-contract)
     * [Smart contract UI](#Smart-contract-UI)
     * [Write your first smart contract](#Write-your-first-smart-contract)
     * [Test your first smart contract](#Test-your-first-smart-contract)
     * [Using async/await in our test](#Using-async/await-in-our-test)
     * [Write your own tests](#Write-your-own-tests)
* [Best practices for smart contracts](#Best-practices-for-smart-contracts)
     * [Known attacks](#Known-attacks)
     * [What would have prevented this](#What-would-have-prevented-this)
     * [Having a Circuit Breaker](#Having-a-Circuit-Breaker)
     * [A Bug Bounty Program](#A-Bug-Bounty-Program)
     * [What about upgrades?](#What-about-upgrades?)
     * [Some general principles and gotchas to keep in mind for security](#Some-general-principles-and-gotchas-to-keep-in-mind-for-security)


       


         


# What is a smart contract?

A smart contract is a program stored inside of a blockchain, the code is assigned an address (just like your wallet has an address, addresses look like: `0x8E698aeA7d456d4A8D8d0485BDC390EFCebC56FA`). <br>
Solidity is turing complete so you could express most program logic using solidity. <br>
The world is your oyster. 
<br><br>
Blockchain apps have key properties and advantages of: <br>
**Transparent:** It is publicly readable by others on the blockchain and accessible via APIs i.e. [etherscan](https://etherscan.io/) . <br>
**Immutable:**  Once a smart contract is created it cannot be changed again. <br>
**Distributed:**  Output of the contract is validated / verified by nodes on the network. Contract states can be publicly visible (yes in some cases even “private” variables). Even contract bytecode can be decompiled (in some cases) back into solidity. <br>
<br>
(Note: your solidity code is compiled to opcode and then bytecode.
<br>
OpCodes look like: 
```
PUSH1 0x80
PUSH1 0x40
MSTORE
```
<br>

Bytecode looks like: 
`0x608060405234801561001057600080fd5b50600436106100415760003560e01c80634357855e1461004657806351aa01991461007e578063d7f29c631461009c575b600080fd5b61007c6004803603604081101561005c57600080fd5b8101908080359060200190929190803590602001909291905050506100ba565b005b610086610249565b6040518082815260200191505060405180910390f35b6100a461024f565b6040518082815260200191505060405180910390f35b816005600082815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610172576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401808060200182810382526028815260200180 …` 


Decompilers are still rather niche and immature! But you can see an example [here](https://github.com/palkeo/panoramix)). 
<br><br>
Here is a small example of a smart contract that allows you to save some values in a contract.

```
// We need to set the version of our compiler called pragma
// This prevents security issues / unexpected behavior 
pragma solidity >=0.4.22 <0.7.0;

contract MyFirstContract {
        
    // this contract implements a simple getter / setter pattern for 1 simple state variable “myName”
    string myName; // solidity is strongly typed so vars must have types
    
    function setName(string memory _name) public { 
// public indicates this is a function accessible to all
        myName = _name;
    }
    
    function getName() public view returns(string memory){
        // memory vs storage: memory is cheaper to use, but is cleared between external contract calls
        // view keyword: indicates this function does not cause state changes, view functions can be called in a transaction free (read no gas) manner
        return myName; 
    }
}  
```

# Solidity Data Structures

### Enum
Creates user-defined data types, based on integer values starting from 0. Their values are prespecified. Requires at least one value / selection. An example is status for shipping: “Pending”, “Shipped”, “Delivered”. Think of these as representing “multiple choice answers”, you must choose 1 value and all the values are pre-defined.
<br>


Here is an example of a smart contract that uses Enums. 
It sets the value of the variable “status” to a default value of Status.Pending

```
pragma solidity >=0.4.22 <0.7.0;

contract Shipping {
    
    enum Status { Pending, Shipped, Delivered }
    Status public status;

    constructor() public {
        status = Status.Pending;
    }
}
```
<br>

### Struct
A custom type that the users can custom define to represent real world objects. <br>
Think about how you would represent a “cryptoPuppy” in a “cryptoPuppies” app? <br>
You could make a struct to represent all the attributes / data that is related to each individual / instance of a cryptoPuppy…  <br>
Maybe each cryptoPuppy has a **ID**, a **Name** and favorite **dogPark** etc… <br>
These are typically used as schema or represent “records”.<br>
Here is an example of a struct being defined to represent vehicles.

```
struct Vehicles_Schema {
        uint256 _id; // has a id
        string _maker; // has a maker
        string _owner; // has a owner
     }
 ```
You will see how this is being used in the mappings example below. <br><br>


### Mappings
Mappings are key value pairs that are encapsulated (packaged together) ; these are closest to dictionaries or Objects in JavaScript. We typically use mapping to model real world objects and do faster lookups. The values could take on various types (including complex types like structs) making this flexible and human friendly to work with (i.e you can access values by mapping_instance.key)
<br><br>
Here is a smart contract that uses the struct `Vehicles_Schema` and saves a list of vehicles represented by the `Vehicles_Schema` as a dictionary. This somewhat mimics a database.  <br>
Notice the mapping signature `uint256 => Vehicles_Schema` => this indicates that the keys are of type unsigned integer and the values are `Vechicles_Schema` structs.
 
 ```
    contract Vehicles {
    uint256 vehicle_id = 0;
    
    mapping(uint256 => Vehicles_Schema) public vehicles;
    
    struct Vehicles_Schema {
        uint256 _id;
        string _maker;
        string _owner;
 
     }
     
     function addV(string memory _maker, string memory _owner) public {
         vehicle_id += 1;
         vehicles[vehicle_id] = Vehicles_Schema(vehicle_id, _maker, _owner);
     }
} 
```

<br>

### Global vars / Objects 
Used to provide information about the blockchain, and live in the global scope. Some examples include: `block`, `msg` and `tx` (transactions), and now (aka block.timestamp). <br> 
For example, you could make sure only the contact creator can execute certain functions. Let’s modify our first contract to see how to implement this change:
```
pragma solidity >=0.4.22 <0.7.0;
contract MyFirstContract2 {
        
    string myName;   
    address private owner;
    
    constructor() public {
        owner = msg.sender; 
    }

  
    function setName(string memory _name) public isOwner { 
          myName = _name;
    }
    
    function getName() public view returns(string memory){
        return myName; 
    }

    modifier isOwner() {
        // If the first argument of 'require' evaluates to 'false', execution terminates and all
        // changes to the state and to Ether balances are reverted.
        // This used to consume all gas in old EVM versions, but not anymore.
        // It is often a good idea to use 'require' to check if functions are called correctly.
        // As a second argument, you can also provide an explanation about what went wrong.
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

}  
```
If you call the function with modifier `isOwner` with a different address that deployed the contract you will get the following error: `transact to MyFirstContract.setName errored: VM error: revert. revert The transaction has been reverted to the initial state. Reason provided by the contract: "Caller is not owner". Debug the transaction to get more information.`

The error indicates that when I tried to call `.setName` I could not because I failed the test specified in the “require” statement. The gas has been refunded and no state changes due to this transaction (function call) were persisted. 


# Using the Truffle Suite

### Using the Blockchain Development Kit from Microsoft
Blockchain Development Kit is an extension you can use in Visual Studio Code. Simply go to extensions and search for Blockchain Development Kit and install it. Make sure you have the correct system requirements before installing it.

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Prework/Images/blockhain_kit_azure.png)

 <br>
 
### Set-up
* Add a new empty folder to your computer. `mkdir myproj`
* Open Visual Studio Code.
* Go to View -> Command Palette, or use ctrl+shift+P. 
* In the search box type: Blockchain New Solidity Project
* Use the UI file explorer pop up to find the folder you created in step1
* If you have all the requirements needed you should be able to choose:
* Create basic project

You will now have a boiler plate of Solidity code that you can use. For now we will only focus on the folders contracts and test.

 <br>
 
### HelloBlockchain.sol
We will start by using the HelloBlockchain.sol smart contract inside of the contracts folder.

* Compile the contract
* Go to contracts/HelloBlockchain.sol
* Right click HelloBlockchain.sol
* Click on Build Contracts to compile the smart contract
* In Output you can see information about the compiled contract

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Prework/Images/compiling_contracts.png)

 <br>
 
### Test the contract
You can find the test file in test/HelloBlockchain.js
* Go to Terminal and then New Terminal
* In the terminal type truffle develop
* In the terminal type: truffle test
* In the terminal you will see which tests passed, and if any test failed
```
  Contract: HelloBlockchain
    √ testing ResponseMessage of HelloBlockchain (183ms)
    √ testing Responder of HelloBlockchain (173ms)
    √ testing RequestMessage of HelloBlockchain (146ms)
    √ testing State of HelloBlockchain (206ms)
    √ testing Requestor of HelloBlockchain (139ms)
    √ testing SendRequest of HelloBlockchain (353ms)
    √ testing SendResponse of HelloBlockchain (245ms)


  7 passing (2s)
```

 <br>
 
### Deploy the contract
* Go to contracts/HelloBlockchain.sol
* Right click HelloBlockchain.sol
* Click on Deploy Contracts 
* In the output you can see information about the deployed contract

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Prework/Images/deployed_contract.png)

Here you see some key information / meta data about the contract you just deployed:
* The address of the contract (for you to interact with using a API or a frontend using web3.js … stay tuned for Module2)
* Time stamp of the block that the contract creation tx was a part of
* The account that deployed the contract
* This contract deployment had no msg.value (value sent = 0)
* Gas related settings / data and cost in Eth

 <br>
 
### Smart contract UI
You can interact with your contract through an UI.

* Go to contracts/HelloBlockchain.sol
* Right click HelloBlockchain.sol
* Click Show Smart Contract Interaction Page

A new tab will open called Smart Contract UI. In this UI you can interact with your contract.

 <br>
 
### Write your first smart contract
```
pragma solidity >=0.5.16<=0.7.0;
 
contract Shipping
{
    // Our predefined values for shipping listed as enums
    enum ShippingStatus { Pending, Shipped, Delivered }
    
    // Save enum ShippingStatus in variable status
    ShippingStatus private status;
 
    // Event to launch when package has arrived
    event LogNewAlert(string description);
 
 
    // This initializes our contract state (sets enum to Pending once the program starts)
    constructor() public {
        status = ShippingStatus.Pending;
    }
 
    // Function to change to Shipped
    function Shipped() public {
 
        status = ShippingStatus.Shipped;
    }
    
    // Function to change to Delivered
    function Delivered() public {
        status = ShippingStatus.Delivered;
        emit LogNewAlert("Your package has arrived");
 
    }
    
    
    // Function to get the status of the shipping
    function getStatus(ShippingStatus _status) internal pure returns (string memory) {
        
     // Check the current status and return the correct name
     if (ShippingStatus.Pending == _status) return "Pending";
     if (ShippingStatus.Shipped == _status) return "Shipped";
     if (ShippingStatus.Delivered == _status) return "Delivered";
    
}
 
    // Get status of your shipped item
    function Status() public view returns (string memory) {
         ShippingStatus _status = status;
         return getStatus(_status);
    }
 
}
```

 <br>
 
### Test your first smart contract
To test our smart contract we will use Truffle and Ganache.
Truffle will make it possible to run tests, and Ganache will set up a Blockchain environment for us with test accounts.

**Install Truffle:** In the command prompt type:  `npm install truffle -g` <br>

**Install Ganache:** [Download Ganache](https://www.trufflesuite.com/ganache) <br>
 
 <br>
 
#### Let the testing begin!
* Open the Command Prompt
* cd to the folder you want to start a new projekt 
* Command prompt: mkdir truffle-shipping (or any other name you would like)
* Command prompt: `cd truffle-shipping`
* Command prompt: `truffle init` (initializes truffle in your project)
* Now open the project in Visual Studio Code. You will see the truffle init has created folders with contract, migration, test and a truffle-config.js file as well.
* Add the Shipping Contract by adding this to the command prompt: 
`truffle create contract Shipping`
* Copy the Shipping contract above and paste it in the Shipping.sol file under the contract folder
* Command prompt: `truffle compile` (compiles your added Shipping.sol contract)
* Migration: To be able to deploy our smart contract to the Ethereum network we need to add another Migration file. In the command prompt type truffle create migration shipping_contract
* Go to the Migrations folder and your newly created file. This file will have a set of numbers before the filename you created. Now add this code to the file:
```
const Shipping = artifacts.require("Shipping");
module.exports = function (deployer) {
  deployer.deploy(Shipping);
};
```
Note that we are not adding the filename of the contract, but the contract name itself. In this case it is not that obvious since our contract and file has the same name.
*  Now we will start our test network by opening a new terminal in Visual Studio Code and adding ganache-cli to the terminal. You will see 10 accounts added and also some other information about your test network.
*  In Visual Studio Code go to the truffle-config.js file and add the following code under networks:
  ```
    networks: {
      development:{
      host: '127.0.0.1',
      port: 8545,
      network_id: '*' 
  }
}
```
* In your command prompt type `truffle migrate` which will run all migrations and deploy your smart contract to the test network (in this case our Shipping contract).
* Let’s create our first test by typing this to the command prompt: `truffle create test Shipping`
* In our folder test a Javascript file has been created called Shipping.js. Remove the code in the file and replace it with:
```
const Shipping = artifacts.require("Shipping");
contract('Shipping', () => {
  
  it("should return the status Pending", async ()=> {
    // Instance of our deployed contract
    const instance = await Shipping.deployed();
    // Checking the initial status in our contract
    const status = await instance.Status();
    // Checking if the status is initially Pending as set in the constructor
    assert.equal(status, "Pending");
  });
});
```
* Type `truffle test` in the command prompt to see if the test passes.
* We will start all our tests with it, think of it as writing a sentence describing what you want the test to do. “It should…”
* We will go ahead and write tests to see if the status is changing, when we are calling our functions Shipped() and Delivered(). We also want to test the event we have in the Delivered() function.
* Shipped() test:
```
it("should return the status Shipped", async ()=> {
// Instance of our deployed contract
    const instance = await Shipping.deployed();
 
    // Calling the Shipped() function
    await instance.Shipped();
 
    // Checking the initial status in our contract
    const status = await instance.Status();
 
    // Checking if the status is Shipped
    assert.equal(status, "Shipped");
  });
```
* Delivered() test:

```
   it("should return the status Delivered", async ()=> {
 
    // Instance of our deployed contract
    const instance = await Shipping.deployed();
 
    // Calling the Shipped() function
    await instance.Delivered();
 
    // Checking the initial status in our contract
    const status = await instance.Status();
 
    // Checking if the status is Delivered
    assert.equal(status, "Delivered");
  });
 ```

* Event test
We will use the package truffle-assertions to help us test our events. By using this package we can assert that our events are emitted during the transaction.
* Install: `npm install truffle-assertions`
* Add this to the test file at the top:
```
const Shipping = artifacts.require("Shipping");
const truffleAssert = require('truffle-assertions');
    
    it('should return correct event description', async()=>{
 
    // Instance of our deployed contract
    const instance = await Shipping.deployed();
 
    // Calling the Delivered() function
    const delivered = await instance.Delivered();
 
    // Check event description is correct
    truffleAssert.eventEmitted(delivered, 'LogNewAlert', (event) =>{
      return event.description == 'Your package has arrived';
    });
  });
  ```

<br>

### Using async/await in our test
Because the .deploy returns a promise, we use await in front of this, and also async in front of the test code. This means until the promise if fulfilled (the contract is deployed) we will not move forward with our test. 
 
<br> 
 
### Write your own tests
Can you change the contract and then add a test that makes sure only the owner can use functions in the contract? Hint, you need to use the accounts added to your test net by Ganache, and also use msg.sender and address in your contract.
Can you add to the contract and testing to not being able to ship something when the status is delivered?


# Best practices for smart contracts

## Known attacks 
### A famously expensive example: The DAO Hack
2016 the Decentralized Autonomous Organization (DAO) was hacked and lost around 70 million dollars. A hacker found a loophole in the smart contract, which sent out the amount and then updated the balance. Having a look at the Check-Effect-Interaction below, what happened in the DAO Hack case was that the interact part could be looped several times and the effect happened after this. <br><br>


### What would have prevented this
Make sure to run all your code internally before calling external functions. <br>
An example is a withdrawal from an account by following these steps: <br> 

**Check-Effect-Interaction Pattern** <br>
**Check:** First check the specified amount is available in the account. <br>
**Effect:** Subtract the amount specified from the account. <br>
**Interact:** The amount can be withdrawn <br><br>

In the DAO hack, the contract had a flaw where the withdraw request passes a check (does user have enough balance => true) and then executed the withdraw transaction by sending the requested balance to the attacking contract, but the attacker used a fallback function to call the withdraw function again (aka the re-entrancy attack) before their balance has been decremented / finished. Therefore rapidly and recursively draining the main DAO contract. (Essentially they did Check - Interact - Effect). <br><br>

 
### Having a Circuit Breaker
Now that the immutability of smart contracts is hopefully second nature to you… what do we do? <br>
We can plan for failures! <br>
It’s as simple as setting up a kill switch in our smart contract. If we cannot reverse damage we can at least prevent further damage by turning off our contract.  <br><br>

Here is a simple implementation of the kill switch we can use in `MyFirstContract2`
```
… 
function kill() { if (msg.sender == owner) selfdestruct(owner); }
…
```
You could use the existing modifier for this kill function as well instead of doing the if statement. <br><br>


### A Bug Bounty Program
This is typically a later stage strategy to improve contract security. 
After you have extensively written and tested your contract on a testnet you could reward developers for finding any vulnerabilities on your testnet deployed contract. You could set a per vulnerability reward or a reward that scales with the amount of loss in your testnet contract. 
Remember to make the bounty worthwhile for other blockchain devs. <br>
For more information about known security flaws… feel free to review [here](https://swcregistry.io/). <br><br>


### What about upgrades? 
Smart contracts cannot be changed but could be “upgraded” via a proxy contract that delegates to an implementation contract (which you could change… i.e. delegate to v1 vs v2 of the implementation contract). This is a topic of active debate and research since there exists a trade off between being able to upgrade a contract and the complexity and risk with making a contract upgradable. <br><br>

 
### Some general principles and gotchas to keep in mind for security
- [x] Be Very Paranoid / Assume you will make mistakes: to not assume this is simply arrogant, plus the cost of assuming this and being wrong is much less than the cost of not assuming this and being wrong (in the first case, maybe you wrote more tests, spent more money on the bounty program, spent time writing a redirect / kill switch function etc… in the latter case, you could lose millions of your or other people’s dollars and damage the reputation / adoption of this community). 
- [x] Do not trust external calls or external contracts: it’s better to have a “safelist” and assume anything not on the list is not to be trusted. 
- [x] Be careful with timestamps, randomness, gas on ethereum: these  may act slightly differently than in your usual context and can be manipulated / gamed
- [x] Reuse code where possible. <br>
- [x] KISS (keep it simple). Complexity hides bugs.
