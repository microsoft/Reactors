# Build smart contracts
Use the code in this directory to build multiple smart contracts, test and deploy them.


## Pre-reqs to complete demo

- To write and run code:
  - [VS Code](https://code.visualstudio.com/)
  - [npms and Node.js](https://www.npmjs.com/get-npm)

- To develop,test and deploy the contracts:
  - [Truffle](https://www.trufflesuite.com/truffle) as the development framework for Ethereum 
  - [Ganache](https://www.trufflesuite.com/ganache)
  - [Blockchain Development Kit for Ethereum]()
    - **Note:** Additional dependencies for the development kit include: Python, Git

## Other helpful tools
- To write and deploy secure contracts:
  - [OpenZeppelin](https://openzeppelin.com/)  
- Tools to manage your blockchain:
  - Build, govern, and expand consortium blockchain networks with [Azure Blockchain Service](https://azure.microsoft.com/services/blockchain-service/)
  - Easily prototype blockchain apps in the cloud with [Azure Blockchain Workbench](https://azure.microsoft.com/features/blockchain-workbench/)

## Demo steps

### Local development and deployment
The code to the demo has been completed. To use the smart contracts:
1. Download or clone the Reactors repository.
2. Navigate to this directory.
3. Start the Ganache UI client and create a new workspace. Select **Add Project** and link the `truffle-config.js` file to the workspace. The **Save Project**.
4. Update the `truffle-config.js` file if needed to set the port to `7545` to point to the Ganache client.
5. From the terminal, run:
  - `truffle compile`
  - `truffle migrate`
  - `truffle test`
6. From VSCode, right-click on a contract and select `Deploy contracts`. Deploy to the local server.
7. Inspect the Ganache UI to see the transactions, blocks, and more.

### Cloud deployment
1. You can choose to deploy the contracts to services like:
- [Azure Blockchain Service](https://channel9.msdn.com/Shows/Blocktalk/Getting-started-with-Azure-Blockchain-Service-Part-I-Deploy-and-configure-your-network)
- [Infura](https://channel9.msdn.com/Shows/Blocktalk/Deploying-smart-contracts-to-Infura-with-VS-Code)