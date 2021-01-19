# Exercise - Develop a todo list and deploy to development

In this exercise, you'll be developing a simple task manager and utilize it to connect and deploy on the **Ropsten** test networks.

In the first part of this exercise, let's focus on creating the project, adding a smart contract, and then deploying to a development network.

For this tutorial, we'll use:

- Visual Studio Code to create our project.
- [Truffle](https://www.trufflesuite.com/truffle) to compile and deploy.
- [Ganache CLI](https://github.com/trufflesuite/ganache-cli) as the blockchain development server.

## Create a new Truffle project

1. Open a terminal or command prompt window and create a new directory called *todolist* by typing: **mkdir todolist**.

2. Navigate to the newly created directory by typing: **cd todolist**.

3. Initialize the directory as a Truffle project by typing: **truffle init**.

4. Open the *todolist* folder in Visual Studio Code.

5. From within VS Code, create a file in the contracts directory named **TodoList.sol** and copy in the following code:

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

## Migrate and deploy to development

1. Create a migration for *TodoList.sol* in the **migrations/** folder by creating a new file called **2_deploy_contracts.js** and copy in the following code into that file to deploy the TodoList smart contract:

```javascript
var TodoList = artifacts.require("./TodoList.sol";);

module.exports = function(deployer) {
    deployer.deploy(TodoList);
};
```

2. In the main project directory, open **./truffle-config.js** and un-comment the code to deploy on the development network which will be deployed to localhost port **8545**. Your code should look as follows:

```javascript
 networks: {
   development: {
     host: "127.0.0.1",
     port: 8545,
     network_id: "*" // Match any network id
   }
 },
```

3. Open a terminal window within VS COde and start up a development blockchain using ganache-cli by typing: **ganache-cli**.

4. In Visual Studio Code, open a terminal window to compile and migrate the TodoList contract to the development network by running the following:

- `truffle compile`
- `truffle migrate --reset`

This will deploy the smart contracts to the development network. At this point, test your contract using the truffle console, inspect and modify the smart contracts. Below we can see that we created a single task when initializing the task list. Using **truffle console**, you can continue to interact with the contract, creating and setting tasks and toggling their status.
