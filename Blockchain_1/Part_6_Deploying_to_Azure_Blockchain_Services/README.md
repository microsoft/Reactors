# Part 6. Deploying to Azure Blockchain Services

In addition to providing tools to help developers have fun and be
succesful, Microsoft has built a platform based upon Ethereum in the
cloud. [Azure Blockchain Service](https://azure.microsoft.com/services/blockchain-service/) can host your contracts and allow you
to interact with your data, other services and more.

The main difference is that you will need to have a free Azure account
and have set up a Blockchain Consortium.

1. Start by [Creating your Azure Blockchain Service member](https://docs.microsoft.com/en-us/azure/blockchain/service/create-member).
2. Install the [Azure Blockchain Development Kit](https://marketplace.visualstudio.com/items?itemName=AzBlockchain.azure-blockchain) if you have not already done so.
3. Connect your Azure Blockchain Development Kit to your [Azure Blockchain Service Consortium](https://docs.microsoft.com/en-us/azure/blockchain/service/connect-vscode).
4. At this point you should be able to select your Azure Blockchain Service Consortium from the list of targets when you try to deploy your them (e.g. instead of just locally to Truffle or Ganache as you have done so far). Deploy the Blockopoly contracts. This may take longer than deploying locally but you should be given an indication that it is done.
5. Connect to one of the contracts that you have tested locally via the Smart Contract Interaction Page. Now, however, you will be connecting to the version in the Azure Cloud. (*Note:* As cool as this is, please be aware you will start to be consuming resources. The Free Azure account comes with credits so you will not be charged anything, but you may use up your credits if you leave the resources running indefinitely.)
6. Visit the [Azure Portal](https://portal.azure.com/) and select Azure Blockchain Service to explore the deployment of your contracts.
7. We are not going to cover all of the other cool things you can do with Azure Blockchain Services and the Azure Blockchain Workbench, but there are plenty of [cool tutorials](https://github.com/Azure-Samples/blockchain-devkit) for you to explore on your own.

