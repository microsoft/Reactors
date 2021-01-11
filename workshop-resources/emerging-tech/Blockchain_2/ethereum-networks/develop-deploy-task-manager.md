# Develop a todo list and deploy to the **Ropsten Testnet**

## Dependencies:

- js
- Truffle
- VS code
- MetaMask
- Infura
- HDWalletProvider

**Task:**
Develop a simple task manager and utilize it to connect and deploy on the **Ropsten** Test Networks. For this tutorial, we will deploy to **Ropsten** using **MetaMask** with test-ether. The process for deploying requires setting up an [Infura](http://www.infura.io/) account. We will use the [TruffleSuite](https://www.trufflesuite.com/) development tools and VS Code to create, compile and deploy the smart contract first to a development network and then to the **Ropsten** testnet. Once deployed, we can use [**ropsten.etherscan.io**](https://ropsten.etherscan.io/) to inspect the blocks which have been deployed to the testnet.

The previous modules in this series walk through the entire development and deployment process for creating an Ethereum Dapp, Web front end and deploying it to a Development Network and interacting with it using **MetaMask** , **TruffleSuite** and **Drizzle** from within the **VS Code** development environment.

Rather than focus on front end development and other aspects building a Dapp, this tutorial is focused on the deployment of a smart contract to an ethereum testnet.

The [TruffleSuite](https://github.com/trufflesuite) toolkit provides support for deploying to different networks and the configuration file, truffle-config.js, provides the template for connecting to multiple networks. Previously, we have been using a development network.

**Steps:** 
1. Create a new directory: $ mkdir todolist

2. Navigate to the new directory: $ cd todolist

3. Initialize the directory as a Truffle project. $ truffle init

4. Open the project in Visual Studio Code. Then from within VS CCode, open the folder **todolist**.

The directory structure should look like:

![](./Images/TodoList_Directory_Structure1.png)

5. From within VS Code, create the file in the contracts directory **TodoList.sol** and copy in the following code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;
 
contract TodoList {
 uint public taskCount = 0;
 
 struct Task {
   uint id;
   string taskname;
   bool status;
 }
 
 mapping(uint => Task) public tasks;
 
 event TaskCreated(
   uint id,
   string taskname,
   bool status
 );
 
 event TaskStatus(
   uint id,
   bool status
 );
 
 constructor() public {
   createTask("Todo List Tutorial");
 }
 
 function createTask(string memory _taskname) public {
   taskCount ++;
   tasks[taskCount] = Task(taskCount, _taskname, false);
   emit TaskCreated(taskCount, _taskname, false);
 }
 
 function toggleStatus(uint _id) public {
   Task memory _task = tasks[_id];
   _task.status = !_task.status;
   tasks[_id] = _task;
   emit TaskStatus(_id, _task.status);
 }
 
}
```

6. Create a migration for the todo.sol list in the **./migrations** folder by creating a new file called **2\_deploy\_contracts.js** and copy in the following code into that file to deploy the TodoList smart contract:

```javascript
var TodoList = artifacts.require(&quot;./TodoList.sol&quot;);

module.exports = function(deployer) {
	deployer.deploy(TodoList);
};
```

7. In the main project directory, open **./truffle-config.js** and un-comment the code to deploy on the **development network** which will be deployed to localhost port **8545**. If you prefer to use the ganache app, use port **7545** instead.

```javascript
 networks: {
   development: {
     host: "127.0.0.1",
     port: 8545,
     network_id: "*" // Match any network id
   }
 },
```

8. Open a terminal window and start up a development blockchain using **ganache-cli**: $ ganache-cli

9. In Visual Studio Code, open a terminal window to compile and migrate the TodoList contract to the development network by running: `truffle compile` and then
`truffle migrate --reset`

This will deploy the smart contracts to the development network. At this point, test your contract using the truffle console, inspect and modify the smart contracts. Below we can see that we created a single task when initializing the task list. Using **truffle console**, you can continue to interact with the contract, creating and setting tasks and toggling their status.

## Deploying to a test network

Deploying to a test network requires **test ethers**, which do not have value. Every blockchain interaction with a smart contract costs some fees (gas) and the interaction is known as a **transaction**. To get **test ethers** use an an Ether Faucet. For the **Ropsten** test network, **test ethers** can be acquired from a **Ropsten Ethereum Faucet**.

Dependencies for this section are:

- Metamask
- HDWalletProvider
- Ropsten Test Ether
- Infura

### Metamask
If you haven’t done so already, install and set up **Metamask**.
- Go to the **Metamask** website to install it if you haven’t already at [www.metamask.io](www.metamask.io)

### HDWalletProvider
For this part of the installation, you will need to run the following commands in your project directory from a terminal window:
$ npm init
$ npm install fs
$ npm install @truffle/hdwallet-provider

Wait for the installations of fs and HDWalletProvider to complete. You may see a number of warnings but unless there are errors, they can be ignored.

### Adding Ether to Metatmask Ropsten Test Network Account

Using your **Metamask** account, connect to the **Ropsten Test Network**. If you don’t have any **test ether** already, get some **ether** from the **Ropsten Test Faucet** located at [https://faucet.ropsten.be](https://faucet.ropsten.be).

1. Open MetaMask
2. Connect to Ropsten
3. Copy the address of your account to the clipboard

![](./Images/Metamask_0_Eth_Connect.png)

4. Open a browser window or tab, and navigate to: [https://faucet.ropsten.be/](https://faucet.ropsten.be/)
5. Request ether by entering your testnet account address and clicking on the button “Send me test Ether”.

![](./Images/Ropsten_Test_Faucet_Request_Ether.png)

6. Go back to **Metamask** and verify that you now have **ether** in your account.

![](./Images/Metamask_Ropsten_Test_with_1_Ether.png)


### Setting up Infura account and linking the endpoints to the Ropsten Test Network

[Infura](https://infura.io/) development suite provides instant, scalable **API** access to the **Ethereum** and **IPFS** networks. Setting up an account is easy and has no cost. A quick review of the [step-by-step tutorial](https://blog.infura.io/getting-started-with-infura-28e41844cc89/) is worth reviewing.

- Infura is a hosted Ethereum node cluster which gives users the ability to run an application on a public network. Infura gives users the ability to:
  - Interact with Ethereum networks like Robsten, Rinkeby or the Mainnet.
  - Deploy contracts to Ethereum networks.
  - Interact with contracts on Ethereum networks.
- Sign up and get started with Infura - go to [www.infura.io](http://www.infura.io/)
  - Set up an account and confirm your email address
  - Once you have an account, set up a project and select the endpoints to point to a **Ropsten** test network.
  - It should look similar to the Test Project below.

![](./Images/Infura_Test_Project.png)

In the **Truffle** configuration file, **./truffle-config.js**,  un-comment the lines for **HDWallet Provider**, **InfruaKey**, **fs** and **mnemonic**:

```javascript
 const HDWalletProvider = require('@truffle/hdwallet-provider');
 const infuraKey = "fj4jll3k.....";
 
 const fs = require('fs');
 const mnemonic = fs.readFileSync(".secret").toString().trim();
```

Go to your **infura** account, and copy the **InfuraKey** for the **endpoint** by clicking on the clipboard:

![](./Images/Ropsten_EndPoint.png)

Copy the numeric part of the key to the **./truffle-config.js** - below is a sample, your key will be different:

```javascript
const infuraKey = "4205b62c0a104f1e95d9771a48068d04";
```

Create a file called **.secret** and copy your **mnemonic seed** to that file. The **mneumonic seed phrase** can be found in the settings portion of your **Metamask** account. Do not share this with anyone or they will be able to access your account! If you are using **git**, include **.secret** in your **.gitignore** file.

![](./Images/Reveal_Metamask_Seed_Phrase.png)

The code below will read the seed phrase from the file **.secret** and trim all the white spaces:
```javascript
const mnemonic = fs.readFileSync(".secret").toString().trim();
```

Now define the network by un-commenting the **Ropsten network** settings in **truffle-config.js** and and modifying the line referencing the **provider** to include the **v3/** infura link. It should look like the following:

```javascript
ropsten: {
   provider: () => new HDWalletProvider(mnemonic, `https://ropsten.infura.io/v3/${infuraKey}`),
   network_id: 3,       // Ropsten's id
   gas: 5500000,        // Ropsten has a lower block limit than mainnet
   confirmations: 2,    // # of confs to wait between deployments. (default: 0)
   timeoutBlocks: 200,  // # of blocks before a deployment times out  (minimum/default: 50)
   skipDryRun: true     // Skip dry run before migrations? (default: false for public nets )
 },
```

To deploy our to Ropsten run the following command: $ truffle migrate --network ropsten

You will see the following output:

```output
Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.

Warning: Both truffle-config.js and truffle.js were found. Using truffle-config.js.

Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.


Starting migrations...
======================
> Network name:    'ropsten'
> Network id:      3
> Block gas limit: 8000029 (0x7a121d)


1_initial_migration.js
======================

   Deploying 'Migrations'
   ----------------------
   > transaction hash:    0x2f456acc5f842ddf0eb151742e47dd6e8ec5e48d73b1f150e2908cb56e0bf174
   > Blocks: 1            Seconds: 29
   > contract address:    0x789101d0B0Ffa4f8f87E67AF8ff8F84bD519752D
   > block number:        9398701
   > block timestamp:     1609784599
   > account:             0x896587D82C895F30433cade401068C2791A6936F
   > balance:             0.99616138
   > gas used:            191931 (0x2edbb)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00383862 ETH

   Pausing for 2 confirmations...
   ------------------------------
   > confirmation number: 1 (block: 9398702)
   > confirmation number: 2 (block: 9398703)

   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.00383862 ETH


2_deploy_contracts.js
=====================

   Deploying 'TodoList'
   --------------------
   > transaction hash:    0xad8066308e9cc8503400c86a43674d856a71e02696e2c21b3e55f566df5afc36
   > Blocks: 0            Seconds: 8
   > contract address:    0x48112BE8d0E6e7bA892aFa2d4Ab58e9c43dd37De
   > block number:        9398706
   > block timestamp:     1609784870
   > account:             0x896587D82C895F30433cade401068C2791A6936F
   > balance:             0.98513544
   > gas used:            508959 (0x7c41f)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.01017918 ETH

   Pausing for 2 confirmations...
   ------------------------------
   > confirmation number: 1 (block: 9398707)
   > confirmation number: 2 (block: 9398708)

   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.01017918 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.0140178 ETH
```


### Inspect Metamask to verify that the ether used to deploy the contract

![](./Images/Metamask_balance_after_deploying_to Ropsten.png)

### Verify deployment of contract on Ropsten Etherscan

Go to [ropsten.etherscan.io](ropsten.etherscan.io), enter in the contract address and inspect your contract.

![](./Images/Ropsten_Etherscan_with_deployed_contract.png)

Open a new terminal window within Visual Studio Code and similar to interacting with your contract on the ganache development blockchain, you can interact with your contract with the **truffle console**. The sample code below diplays two networks which are active. Continue to interact with and inspect transactions using **truffle consol**e and **Ropsten Etherscan**.

```output
$ truffle console --network ropsten
truffle(ropsten)> networks

The following networks are configured to match any network id ('*'):

    development

Closely inspect the deployed networks below, and use `truffle networks --clean` to remove any networks that don't match your configuration. You should not use the wildcard configuration ('*') for staging and production networks for which you intend to deploy your application.

Network: develop (id: 5777)
  Migrations: 0x7937f7273a9a00C298A6dA4DE6683660bd816Ae3
  TodoList: 0x1c6fAaab6d2582cb3501E665d0D86F06C51422B9

Network: ropsten (id: 3)
  Migrations: 0x789101d0B0Ffa4f8f87E67AF8ff8F84bD519752D
  TodoList: 0x48112BE8d0E6e7bA892aFa2d4Ab58e9c43dd37De
```

