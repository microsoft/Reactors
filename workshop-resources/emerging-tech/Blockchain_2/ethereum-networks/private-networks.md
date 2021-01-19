# Learn about private Ethereum networks

An Ethereum network is private if its nodes are isolated and not connected to a public network such as mainnet or a testnet. Private networks include development networks, or consortium networks.

## Development networks

When developing an Ethereum application, you'll start by running it on a private network to see how it works before deploying it. Similar to how you create a local server on your computer for web development, you can create a local blockchain instance to test your blockchain solution.

On your development network, you can create, test, and iterate changes to your solution very quickly. You can make changes to your solution in development much more seamlessly and quickly than with a public testnet. Tools such as [Ganache](https://www.trufflesuite.com/ganache) and [Hardhat](https://hardhat.org/) are most commonly used to run personal Ethereum development networks.

## Solutions for consortium networks

There are multiple options for consortiums. Consortiums are permissioned and require an invite to participate. They ensure security, privacy, compliance, and performance. There are many options for consortium blockchains, including Hyperledger Besu, R3 Corda and Quorum. Let's explore two popular options for consortium blockchains.

### Hyperledger Besu

[Hyperledger Besu](https://besu.hyperledger.org/en/stable/?azure-portal=true) is an open-source Ethereum client developed under the Apache 2.0 license and written in Java.

Besu is used to develop enterprise applications requiring secure, high-performance transaction processing in a private network. Besu has a command line interface and JSON-RPC API for running, maintaining, debugging, and monitoring nodes in an Ethereum network. The API supports typical Ethereum functionalities such as:

- Ether mining
- Smart contract development
- Decentralized application (Dapp) development.

Hyperledger Besu is a popular Ethereum client that is unique in that it offers a client that can be used in either public networks, as well as private, consortium based networks. It can be deployed a variety of [ways](https://besu.hyperledger.org/en/stable/HowTo/Get-Started/Installation-Options/Install-Binaries/), and recently a preview has been made available in [Azure](https://azuremarketplace.microsoft.com/marketplace/apps/consensys.hyperledger-besu-quickstart?tab=Overview).

More information about configuring and deploying can be found on the [Hyperledger Besu website.](https://besu.hyperledger.org/en/latest/Tutorials/Examples/Private-Network-Example/)

### R3 Corda

The [Corda Platform](https://www.r3.com/corda-platform/?azure-portal=true) is a private, permissioned blockchain focused on supporting trusted communication, interactions and transactions between entities. [**Corda Enterprise**](https://www.r3.com/corda-enterprise/) offers the core attributes of **Corda** open source along with additional business requirements enterprises expect when licensing software. The **Corda** protocol is built on a strong identity model, where every node's identity must be proven to have been properly on boarded.

Signing identities only exist on the **Corda** nodes. Client applications in a **Corda** based solution are simply triggering the workflow that has already been registered on the target **Corda** node, and monitoring the progression of the flow. This is very different from Ethereum, where client applications play a critical role in the transaction lifecycle, by holding the signing keys and signing transactions before they are submitted to the nodes. Essentially, **Corda** applications, or [**CorDapps**](https://docs.corda.net/docs/corda-os/4.7/cordapp-overview.html) for short, completely live on the **Corda** nodes.

There is a [Corda VSCode extension](https://github.com/corda/vscode-corda) which supports **Corda** development. From **VSCode**, go to the extensions icon, click on the icon and enter “Corda” to install the extension.
