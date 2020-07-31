# Part 6. Deploying to Azure Blockchain Service

### Goal
In addition to providing tools to help developers have fun and be succesful, Microsoft has built a cloud platform based upon Ethereum. [Azure Blockchain Service](https://azure.microsoft.com/services/blockchain-service/) can host your contracts and allow you to interact with your data, other services, and more.

The main difference is that you will need to have an Azure account and go through the process to use the Azure Blockchain Service.

### Steps
1. Create your [Azure Blockchain Service member](https://docs.microsoft.com/azure/blockchain/service/create-member).
2. Install the [Azure Blockchain Development Kit](https://marketplace.visualstudio.com/items?itemName=AzBlockchain.azure-blockchain) if you have not already done so.
3. Connect your Azure Blockchain Development Kit to your [Azure Blockchain Service Consortium](https://docs.microsoft.com/azure/blockchain/service/connect-vscode).
4. You should be able to select your Azure Blockchain Service Consortium from the list of targets when you try to deploy them (vs. locally to Truffle or Ganache as you have done so far). Deploy the Blockopoly contracts that you've completed from the [Completed_Solutions directory](../Completed_Solutions/). 
*Note:* This may take longer than deploying locally but you should receive an indication when it is done.
5. Connect to a contract that you have tested locally from the Smart Contract Interaction page. Now, however, you will be connecting to the version in the Azure cloud. 
*Note:* As cool as this is, please be aware you will start consuming resources. The free Azure account includes credits so you will not be charged anything, but you may use up your credits if you leave the resources running indefinitely.
6. To explore the deployment of your contracts, visit the [Azure Portal](https://portal.azure.com/) and select Azure Blockchain Service.
7. We are not going to cover all of the great things you can do with Azure Blockchain Services and the Azure Blockchain Workbench, but there are plenty of [cool tutorials](https://github.com/Azure-Samples/blockchain-devkit) to explore on your own.

