# Prepare for deployment to mainnet

Prior to deploying to the Ethereum mainnet, it's necessary to fully test and audit your code. Working mainnet requires real Ether which costs real money and can add up quickly!

After developing, testing and auditing your code and running the project on at least one testnet without any problems, most projects follow a substantial auditing, testing, security and governance process before deploying to mainnet. This is done to minimize the risks and costs of things going wrong in mainnet.

The process for preparing for mainnet and deploying to mainnet requires a series of steps. The basic steps for deploying to the Ethereum mainnet include: auditing smart contracts, verifying source code, managing keys, and handling project governance. The sections below describes these steps in more detail.

## [Perform a smart contract audit](https://docs.openzeppelin.com/learn/preparing-for-mainnet#auditing-and-security)

Auditing and assessing the security of smart contracts is imperative prior to deploying to a public network. Once a smart contract is deployed, anyone on the network can send a transaction directly to the contracts with any payload. All of the code and the state of the contract is publicly available. Since transactions on blockchains are immutable, once committed, the transactions are permanent and can result in funds being stolen and other malicious activity. It is imperative to audit smart contracts prior to deployment.

## [Verify source code](https://docs.openzeppelin.com/learn/preparing-for-mainnet#verify-source-code)

Before deploying to mainnet, the smart contract source code should be verified by submitting the Solidity code to a third-party. Public services, which as [Etherscan](https://etherscan.io/verifyContract), will compile it and verify that it matches the deployed assembly. This allows any user to view your contract code in a block explorer, and know that it corresponds to the assembly actually running at that address.

Steps for Verifying and Publishing your Solidity Source Code:

- Enter Contract Source Code.
- If the Bytecode generated matches the existing Creation Address Bytecode, the contract is then verified.
- Contract Source Code is published and publicly verifiable by anyone.

## [Manage keys securely](https://docs.openzeppelin.com/learn/preparing-for-mainnet#key-management)

It’s imperative to securely manage private keys when deploying to the **mainnet**. Securing private keys and managing them so they cannot be compromised, lost or stolen requires heavy precautions. There have been several major thefts and losses as a result of keys being mismanaged, lost or stolen. The accounts used to deploy and interact with smart contracts hold real Ether and are targets for hackers. [Hardware wallets](https://docs.ethhub.io/using-ethereum/wallets/hardware/) and [cold storage](https://www.investopedia.com/terms/c/cold-storage.asp#:~:text=Key%20Takeaways&text=Cold%20storage%20is%20a%20way,their%20holdings%20via%20traditional%20means.) (computers never connected to any network) are common ways to store private keys securely.

## [Handle project governance](https://docs.openzeppelin.com/learn/preparing-for-mainnet#project-governance)

There are different ways that decentralized projects are managed depending on community and user base. Often organizations are created to determine how updates, and other aspects of the running decentralized system are managed. There are a number of options of how project governance can be managed, from a small group of trusted administrators, to public voting of all project stakeholders. There is no right answer here, it comes down to what solution you're building and who your community and users are.
