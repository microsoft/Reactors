# Private Blockchain Networks

There are multiple options for deploying private blockchains. Private Blockchains are often referred to as Permissioned or Enterprise Blockchains. Enterprises need to ensure some level of security, privacy, compliance, performance, and many of the properties that a private blockchain can provide. Private blockchains can be open sourced, consortium, or privately developed. There are many options for a private blockchain, and several of the most common ones are Hyperledger Besu, R3 Corda and Quorum.

## Hyperledger Besu

[Hyperledger Besu](https://besu.hyperledger.org/en/stable/) is an open-source Ethereum client developed under the Apache 2.0 license and written in Java. It runs on the Ethereum public network, private networks, and test networks such as Rinkeby, Ropsten, and Görli. Besu implements Proof of Work (Ethash) and Proof of Authority (IBFT 2.0 and Clique) consensus mechanisms.

Besu is used to develop enterprise applications requiring secure, high-performance transaction processing in a private network. Besu has a command line interface and JSON-RPC API for running, maintaining, debugging, and monitoring nodes in an Ethereum network. You can use the API via RPC over HTTP or via WebSockets. Besu also supports Pub/Sub. The API supports typical Ethereum functionalities such as:

- Ether mining
- Smart contract development
- Decentralized application (Dapp) development.

Hyperledger Besu is a popular Ethereum client that is unique in that it offers a client that can be used in either public networks, such as Ethereum mainnet or private, consortium based networks. It can be deployed a variety of [ways](https://besu.hyperledger.org/en/stable/HowTo/Get-Started/Installation-Options/Install-Binaries/), and recently a preview has been made available in [Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/consensys.hyperledger-besu-quickstart?tab=Overview).

Currently, the Hyperledger Besu is fully compatible with the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=AzBlockchain.azure-blockchain), however the provisioning of the nodes is not yet fully integrated. To connect to a running Besu node with the extension, you can do the following:

- Deploy Hyperledger Besu locally or in the cloud.
- Retrieve the JSON rpc endpoint that will be used to communicate with the Besu network. This varies based on the deployment model, for Azure deployments these can be retrieved from the output parameters from the deployment.
- Update the configuration manually. This is shown in the video below. The extension has the ability to use an HD Wallet provider that simply requires a file with a mnemonic to function.

Add the following to the configuration to truffle-config.js:

```javascript
besu: {
   network_id: "*",
   gas: 0,
   gasPrice: 0,
   provider: new HDWalletProvider(
     fs.readFileSync("<path to a file with a mnemonic>", "utf-8"),
     "<besu jsonrpc endpoint>"
   ),
 },
```

More information about configuring and deploying can be found on the [Hyperledger Besu website.](https://besu.hyperledger.org/en/latest/Tutorials/Examples/Private-Network-Example/)

## R3 Corda

The [Corda Platform](https://www.r3.com/corda-platform/) is a private, permissioned blockchain focused on supporting trusted communication, interactions and transactions between entities. [**Corda Enterprise**](https://www.r3.com/corda-enterprise/) offers the core attributes of **Corda** open source along with additional business requirements enterprises expect when licensing software. The **Corda** protocol is built on a strong identity model, where every node's identity must be proven to have been properly on boarded by using an x.509 certificate with a validated trust chain.

Signing identities only exist on the **Corda** nodes. Client applications in a **Corda** based solution are simply triggering the workflow that has already been registered on the target **Corda** node, and monitoring the progression of the flow. This is very different from Ethereum, where client applications play a critical role in the transaction lifecycle, by holding the signing keys and signing transactions before they are submitted to the nodes. Essentially, **Corda** applications, or [**CorDapps**](https://docs.corda.net/docs/corda-os/4.7/cordapp-overview.html) for short, completely live on the **Corda** nodes.

There is a [Corda VSCode extension](https://github.com/corda/vscode-corda) which supports **Corda** development. From **VSCode**, go to the extensions icon, click on the icon and enter “Corda” to install the extension.

![](./Images/VSCode_Corda_Image.png)


