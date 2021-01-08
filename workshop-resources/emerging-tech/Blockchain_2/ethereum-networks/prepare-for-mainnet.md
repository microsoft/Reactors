# Preparing for and Deploying to **Mainnet**

Prior to deploying to the Ethereum **mainnet** , it&#39;s imperative to fully test and audit your code. Adding blocks to the mainnet requires real ETH which costs real money! In addition, security flaws can be devastating. There have been several very well documented hacks including the famous [DAO Attack](https://www.coindesk.com/understanding-dao-hack-journalists) but there have been many others.

The process for preparing for mainnet and deploying to mainnet requires a series of steps. For further reference, please review [Preparing for mainnet](https://docs.openzeppelin.com/learn/preparing-for-mainnet).

After developing, testing and auditing your code and running the project on at least one testnet without any problems, most projects follow a substantial auditing, testing, security and governance process before actually deploying to mainnet.

There are many organizations and consulting groups which provide smart contract audits and other types of security audits. In addition, it&#39;s not uncommon for projects to run [**bounty programs**](https://bounty.ethereum.org/) which call upon the community to earn rewards for finding vulnerabilities and identify bugs.

The basic steps for deploying to the **Ethereum mainnet** include:

- [Smart Contract Audit](https://docs.openzeppelin.com/learn/preparing-for-mainnet#auditing-and-security)
	- Auditing and assessing the security of smart contracts is imperative prior to deploying to a public network. Once a smart contract is deployed, anyone on the network can send a transaction directly to the contracts with any payload. All of the code and the state of the contract is publicly available. Since transactions on blockchains are immutable, once committed, the transactions are permanent and can result in funds being stolen and other malicious activity. It is imperative to audit smart contracts prior to deployment.
- [Verifying Source Code](https://docs.openzeppelin.com/learn/preparing-for-mainnet#verify-source-code)
	- Subsequent to deployment to mainnet, the smart contract source code should be verified by submitting the Solidity code to a third-party. Public services, which as [Etherscan](https://etherscan.io/verifyContract), will compile it and verify that it matches the deployed assembly. This allows any user to view your contract code in a block explorer, and know that it corresponds to the assembly actually running at that address.
	- Steps for Verifying and Publishing your Solidity Source Code:
		- Enter Contract Source Code.
		- If the Bytecode generated matches the existing Creation Address Bytecode, the contract is then Verified.
		- Contract Source Code is published and publicly verifiable by anyone.
- [Managing Keys Securely](https://docs.openzeppelin.com/learn/preparing-for-mainnet#key-management)
	- It’s imperative to securely manage private keys when deploying to the **mainnet**. Securing private keys and managing them so they cannot be compromised, lost or stolen requires heavy precautions. There have been several major thefts and losses as a result of keys being mismanaged, lost or stolen. The accounts used to deploy and interact with smart contracts hold real Ether and are targets for hackers. [Hardware wallets](https://docs.ethhub.io/using-ethereum/wallets/hardware/) and [cold storage](https://www.investopedia.com/terms/c/cold-storage.asp#:~:text=Key%20Takeaways&text=Cold%20storage%20is%20a%20way,their%20holdings%20via%20traditional%20means.) (computers never connected to any network) are common ways to store private keys securely.

- [Handling Project Governance](https://docs.openzeppelin.com/learn/preparing-for-mainnet#project-governance)
	- There are different ways that decentralized projects are managed depending on community and user base. Often organizations are created to determine how updates, and other aspects of the running decentralized system are managed.

Remember that, while managing your contracts in a **testnet** and in **mainnet** is basically the same, there are important differences when on **mainnet**, since the project is using real **eth** and is available to the public.

