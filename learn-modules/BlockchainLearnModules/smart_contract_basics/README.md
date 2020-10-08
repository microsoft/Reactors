# Content
- [What is a smart contract?](#What-is-a-smart-contract?) 
- [Solidity Data Structures](#Solidity-Data-Structures)
     - [Enum](#Enum)
     - [Struct](#Struct)
     - [Mappings](#Mappings)
     - [Global vars / Objects](#Global-vars-/-Objects)
- [Using the Truffle Suite](#Using-the-Truffle-Suite)
     - [Using the Blockchain Development Kit from Microsoft](#Using-the-Blockchain-Development-Kit-from-Microsoft)
     - [Set-up](#Set-up)
     - [HelloBlockchain.sol](#HelloBlockchain.sol)
     - [Test the contract](#Test-the-contract)
     - [Deploy the contract](#Deploy-the-contract)
     - [Smart contract UI](#Smart-contract-UI)
     - [Write your first smart contract](#Write-your-first-smart-contract)
     - [Test your first smart contract](#Test-your-first-smart-contract)
     - [Using async/await in our test](#Using-async/await-in-our-test)
     - [Write your own tests](#Write-your-own-tests)
- [Best practices for smart contracts](#Best-practices-for-smart-contracts)
     - [Known attacks](#Known-attacks)
     - [What would have prevented this](#What-would-have-prevented-this)
     - [Having a Circuit Breaker](#Having-a-Circuit-Breaker)
     - [A Bug Bounty Program](#A-Bug-Bounty-Program)
     - [What about upgrades?](#What-about-upgrades?)
     - [Some general principles and gotchas to keep in mind for security](#Some-general-principles-and-gotchas-to-keep-in-mind-for-security)


       


         


# What is a smart contract?

A smart contract is a program stored inside of a blockchain, the code is assigned an address (just like your wallet has an address, addresses look like: `0x8E698aeA7d456d4A8D8d0485BDC390EFCebC56FA`). 
Solidity is turing complete so you could express most program logic using solidity. 
The world is your oyster. 

Blockchain apps have key properties and advantages of: 
**Transparent:** It is publicly readable by others on the blockchain and accessible via APIs i.e. [etherscan](https://etherscan.io/) . 
**Immutable:**  Once a smart contract is created it cannot be changed again. 
**Distributed:**  Output of the contract is validated / verified by nodes on the network. Contract states can be publicly visible (yes in some cases even “private” variables). Even contract bytecode can be decompiled (in some cases) back into solidity. 

Here is a small example of a smart contract that allows you to save some values in a contract.

```solidity

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



Here is an example of a smart contract that uses Enums. 
It sets the value of the variable “status” to a default value of Status.Pending

```solidity

pragma solidity >=0.4.22 <0.7.0;

contract Shipping {
    
    enum Status { Pending, Shipped, Delivered }
    Status public status;

    constructor() public {
        status = Status.Pending;
    }
}
```


### Struct
A custom type that the users can custom define to represent real world objects. 
Think about how you would represent a “cryptoPuppy” in a “cryptoPuppies” app? 
You could make a struct to represent all the attributes / data that is related to each individual / instance of a cryptoPuppy…  
Maybe each cryptoPuppy has a **ID**, a **Name** and favorite **dogPark** etc… 
These are typically used as schema or represent “records”.
Here is an example of a struct being defined to represent vehicles.

```solidity

struct Vehicles_Schema {
        uint256 _id; // has a id
        string _maker; // has a maker
        string _owner; // has a owner
     }
 ```
You will see how this is being used in the mappings example below. 


### Mappings
Mappings are key value pairs that are encapsulated (packaged together) ; these are closest to dictionaries or Objects in JavaScript. We typically use mapping to model real world objects and do faster lookups. The values could take on various types (including complex types like structs) making this flexible and human friendly to work with (i.e you can access values by mapping_instance.key)

Here is a smart contract that uses the struct `Vehicles_Schema` and saves a list of vehicles represented by the `Vehicles_Schema` as a dictionary. This somewhat mimics a database.  
Notice the mapping signature `uint256 => Vehicles_Schema` => this indicates that the keys are of type unsigned integer and the values are `Vechicles_Schema` structs.
 
 ```solidity

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



### Global vars / Objects 
Used to provide information about the blockchain, and live in the global scope. Some examples include: `block`, `msg` and `tx` (transactions), and now (aka block.timestamp).  
For example, you could make sure only the contact creator can execute certain functions. Let’s modify our first contract to see how to implement this change:
```solidity

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

 
 
### Set-up
- Add a new empty folder to your computer. `mkdir myproj`
- Open Visual Studio Code.
- Go to View -> Command Palette, or use ctrl+shift+P. 
- In the search box type: Blockchain New Solidity Project
- Use the UI file explorer pop up to find the folder you created in step1
- If you have all the requirements needed you should be able to choose:
- Create basic project

You will now have a boiler plate of Solidity code that you can use. For now we will only focus on the folders contracts and test.

 
 
### HelloBlockchain.sol
We will start by using the HelloBlockchain.sol smart contract inside of the contracts folder.

- Compile the contract
- Go to contracts/HelloBlockchain.sol
- Right click HelloBlockchain.sol
- Click on Build Contracts to compile the smart contract
- In Output you can see information about the compiled contract

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Prework/Images/compiling_contracts.png)

 
 
### Test the contract
You can find the test file in test/HelloBlockchain.js
- Go to Terminal and then New Terminal
- In the terminal type truffle develop
- In the terminal type: truffle test
- In the terminal you will see which tests passed, and if any test failed
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

 
 
### Deploy the contract
- Go to contracts/HelloBlockchain.sol
- Right click HelloBlockchain.sol
- Click on Deploy Contracts 
- In the output you can see information about the deployed contract

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Prework/Images/deployed_contract.png)

Here you see some key information / meta data about the contract you just deployed:
- The address of the contract (for you to interact with using a API or a frontend using web3.js … stay tuned for Module2)
- Time stamp of the block that the contract creation tx was a part of
- The account that deployed the contract
- This contract deployment had no msg.value (value sent = 0)
- Gas related settings / data and cost in Eth

 
 
### Smart contract UI
You can interact with your contract through an UI.

- Go to contracts/HelloBlockchain.sol
- Right click HelloBlockchain.sol
- Click Show Smart Contract Interaction Page

A new tab will open called Smart Contract UI. In this UI you can interact with your contract.

 
 
### Write your first smart contract
```solidity

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

 
 
### Test your first smart contract
To test our smart contract we will use Truffle and Ganache.
Truffle will make it possible to run tests, and Ganache will set up a Blockchain environment for us with test accounts.

**Install Truffle:** In the command prompt type:  `npm install truffle -g` 

**Install Ganache:** [Download Ganache](https://www.trufflesuite.com/ganache) 
 
 
 
#### Let the testing begin!
- Open the Command Prompt
- cd to the folder you want to start a new projekt 
- Command prompt: mkdir truffle-shipping (or any other name you would like)
- Command prompt: `cd truffle-shipping`
- Command prompt: `truffle init` (initializes truffle in your project)
- Now open the project in Visual Studio Code. You will see the truffle init has created folders with contract, migration, test and a truffle-config.js file as well.
- Add the Shipping Contract by adding this to the command prompt: 
`truffle create contract Shipping`
- Copy the Shipping contract above and paste it in the Shipping.sol file under the contract folder
- Command prompt: `truffle compile` (compiles your added Shipping.sol contract)
- Migration: To be able to deploy our smart contract to the Ethereum network we need to add another Migration file. In the command prompt type truffle create migration shipping_contract
- Go to the Migrations folder and your newly created file. This file will have a set of numbers before the filename you created. Now add this code to the file:
```solidity

const Shipping = artifacts.require("Shipping");
module.exports = function (deployer) {
  deployer.deploy(Shipping);
};
```
Note that we are not adding the filename of the contract, but the contract name itself. In this case it is not that obvious since our contract and file has the same name.
-  Now we will start our test network by opening a new terminal in Visual Studio Code and adding ganache-cli to the terminal. You will see 10 accounts added and also some other information about your test network.
-  In Visual Studio Code go to the truffle-config.js file and add the following code under networks:
```solidity

networks: {
     development:{
          host: '127.0.0.1',
          port: 8545,
          network_id: '*' 
     }
}
```
- In your command prompt type `truffle migrate` which will run all migrations and deploy your smart contract to the test network (in this case our Shipping contract).
- Let’s create our first test by typing this to the command prompt: `truffle create test Shipping`
- In our folder test a Javascript file has been created called Shipping.js. Remove the code in the file and replace it with:
```solidity

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
- Type `truffle test` in the command prompt to see if the test passes.
- We will start all our tests with it, think of it as writing a sentence describing what you want the test to do. “It should…”
- We will go ahead and write tests to see if the status is changing, when we are calling our functions Shipped() and Delivered(). We also want to test the event we have in the Delivered() function.
- Shipped() test:
```solidity

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
- Delivered() test:

```solidity

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

- Event test
We will use the package truffle-assertions to help us test our events. By using this package we can assert that our events are emitted during the transaction.
- Install: `npm install truffle-assertions`
- Add this to the test file at the top:
```solidity

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



### Using async/await in our test
Because the .deploy returns a promise, we use await in front of this, and also async in front of the test code. This means until the promise if fulfilled (the contract is deployed) we will not move forward with our test. 
 
 
 
### Write your own tests
Can you change the contract and then add a test that makes sure only the owner can use functions in the contract? Hint, you need to use the accounts added to your test net by Ganache, and also use msg.sender and address in your contract.
Can you add to the contract and testing to not being able to ship something when the status is delivered?


# Best practices for smart contracts

Security is the responsibility of all developers but it’s extra important to blockchain developers. Due to the immutability and the complexity it’s harder to address/fix security problems quickly, and even simple mistakes could lead to massive losses. Educating yourself and vigilance is the best defense. Let’s look at a real and famously expensive example.


## Known attacks 
### A famously expensive example: The DAO Hack
2016 the Decentralized Autonomous Organization (DAO) was hacked and lost around 70 million dollars. A hacker found a loophole in the smart contract, which sent out the amount and then updated the balance. Having a look at the Check-Effect-Interaction below, what happened in the DAO Hack case was that the interact part could be looped several times and the effect happened after this. 


### What would have prevented this
Make sure to run all your code internally before calling external functions. 
An example is a withdrawal from an account by following these steps:  

**Check-Effect-Interaction Pattern** 
**Check:** First check the specified amount is available in the account. 
**Effect:** Subtract the amount specified from the account. 
**Interact:** The amount can be withdrawn 

In the DAO hack, the contract had a flaw where the withdraw request passes a check (does user have enough balance => true) and then executed the withdraw transaction by sending the requested balance to the attacking contract, but the attacker used a fallback function to call the withdraw function again (aka the re-entrancy attack) before their balance has been decremented / finished. Therefore rapidly and recursively draining the main DAO contract. (Essentially they did Check - Interact - Effect). 

 
### Having a Circuit Breaker
Now that the immutability of smart contracts is hopefully second nature to you… what do we do? 
We can plan for failures! 
It’s as simple as setting up a kill switch in our smart contract. If we cannot reverse damage we can at least prevent further damage by turning off our contract.  

Here is a simple implementation of the kill switch we can use in `MyFirstContract2`
```solidity
… 
function kill() { if (msg.sender == owner) selfdestruct(owner); }
…
```
You could use the existing modifier for this kill function as well instead of doing the if statement. 


### A Bug Bounty Program
This is typically a later stage strategy to improve contract security. 
After you have extensively written and tested your contract on a testnet you could reward developers for finding any vulnerabilities on your testnet deployed contract. You could set a per vulnerability reward or a reward that scales with the amount of loss in your testnet contract. 
Remember to make the bounty worthwhile for other blockchain devs. 
For more information about known security flaws… feel free to review [here](https://swcregistry.io/). 


### What about upgrades? 
Smart contracts cannot be changed but could be “upgraded” via a proxy contract that delegates to an implementation contract (which you could change… i.e. delegate to v1 vs v2 of the implementation contract). This is a topic of active debate and research since there exists a trade off between being able to upgrade a contract and the complexity and risk with making a contract upgradable. 

 
### Some general principles and gotchas to keep in mind for security
- [x] Be Very Paranoid / Assume you will make mistakes: to not assume this is simply arrogant, plus the cost of assuming this and being wrong is much less than the cost of not assuming this and being wrong (in the first case, maybe you wrote more tests, spent more money on the bounty program, spent time writing a redirect / kill switch function etc… in the latter case, you could lose millions of your or other people’s dollars and damage the reputation / adoption of this community). 
- [x] Do not trust external calls or external contracts: it’s better to have a “safelist” and assume anything not on the list is not to be trusted. 
- [x] Be careful with timestamps, randomness, gas on ethereum: these  may act slightly differently than in your usual context and can be manipulated / gamed
- [x] Reuse code where possible. 
- [x] KISS (keep it simple). Complexity hides bugs.


### Post Work Prompt:
 

Write a bank contract that will exchange your local currency from your bank account to tokens. 
This is mostly in shape already in the oracle contract that was demontrated in the workshop / lab.

## Some hints and considerations:
- The contract should not make any transactions if there is not enough balance for this on the bank account or the amount to buy tokens for. 
- Take a look at the oracle contract (see above) as you will use an API to get the token price and make the exchange. This contract is discussed in reactor workshops
- You may want to add state variables to keep track of things like the price of the token, how much was the transaction for in bank balance etc...
- A nested mapping may be used to represent the bank balance and token amount
- Use msg.sender wisely to figure out who’s balance we are operating on
- One contract address should use the contract at a time, you may want to use a lock to make sure only one msg.sender uses the contract until the previous transaction already in progress has completed
- You can write functions to get the balance of your deposit, and make a deposit to your bank account
- A function that will make the exchange to decrease bank account balance and increase token balance according to the oracle result on the token prices will be required as well
- In the original oracle contract you can use the same API call to the oracle and fullfill() function. You might want to consider calling the function to exchange in the fullfill() function, as this will be fired at the end of the oracle request when you just updated the latest token price.


## Acceptance criteria / tests you might want to consider

As a user:

When I deposit my local currency to my bank account
I expect: my bank balance to increase accordingly


When I specify an amount to buy tokens. 

I expect:
- If the amount I deposited to buy tokens is less than the price for tokens, I should not be able to do the transaction.
- Otherwise: I expect my bank balance to decrease and my token balance to increase
     
     
 ## Below is a sample Implementation
 You should either produce your own contract first or at least try to improve this smart contract below
 
 ```solidity
 
 pragma solidity ^0.6.6;
import "https://raw.githubusercontent.com/smartcontractkit/chainlink/develop/evm-contracts/src/v0.6/ChainlinkClient.sol";
contract APIConsumer is ChainlinkClient {
    uint256 public tokenPrice;
    uint256 public amountToBuyTokens;
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;
    address public owner;
    address public tx_address;
    bool public lock;
    
    enum BalanceType { bank, token }

    event LogNewAlert(string description, uint256 purchase_amt, bool lk_status);
    
    constructor() public {
        setPublicChainlinkToken();
        oracle = 0x2f90A6D021db21e1B2A077c5a37B3C7E75D15b7e;
        jobId = "29fa9aa13bf1468788b7cc4a500a45b8";
        fee = 0.1 * 10 ** 18;
        owner = msg.sender;
    }

    mapping(address => mapping(BalanceType => uint256)) balances;
    
        // Deposit to bank (local currency)
    function depositToBank(uint256 _deposit) public {
        balances[msg.sender][BalanceType.bank]+=_deposit;
        balances[msg.sender][BalanceType.token]+=0;
    }

    function getBankBalance() public view returns(uint256){
        return balances[msg.sender][BalanceType.bank];
    }
    // Withdraw from bank (local currency)
    function withdrawFromBank(uint256 _amount) private {
        balances[tx_address][BalanceType.bank]-=_amount;

    }
    
    function getTokenBalance() public view returns(uint256){
        return balances[msg.sender][BalanceType.token];
    }
    
    function txBuyTokens(uint256 _amount) public{
    if(balances[msg.sender][BalanceType.bank] >= _amount){
            tx_address = msg.sender;
            amountToBuyTokens = _amount;
            lock = true;
            LogNewAlert("tx init: buying || lock status", _amount , lock);
            go();
        }
    }
// Exchange local currency for tokens
    function exchangeFunction() private {
        if(balances[tx_address][BalanceType.bank] >= amountToBuyTokens && amountToBuyTokens>= tokenPrice) {
            balances[tx_address][BalanceType.token] += amountToBuyTokens/ tokenPrice;
            amountToBuyTokens = (balances[tx_address][BalanceType.token]* tokenPrice);
            withdrawFromBank(amountToBuyTokens);
    }
    }
    function go() private returns (bytes32 requestId) 
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        request.add("get", "https://jsonplaceholder.typicode.com/todos/12");
        request.add("path", "id");
        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }
    /**
     * Receive the response in the form of uint256
     */ 
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId)
    {
        tokenPrice = _price;
        // call exchange function here
        exchangeFunction();
        lock = false;
        tx_address=owner;
        LogNewAlert("tx complete: bought || lock status", amountToBuyTokens , lock);
        amountToBuyTokens = 0;

    }
}

```


### "Extra Credits": Implement your own [ERC721](https://docs.openzeppelin.com/contracts/3.x/erc721) contract 
