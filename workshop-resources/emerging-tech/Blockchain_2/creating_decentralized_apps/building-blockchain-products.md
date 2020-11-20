Building Blockchain Products
----------------------------

[Decentralized applications](https://ethereum.org/en/developers/docs/dapps/) differ from traditional applications in that they do not rely on a centralized server network, but instead operate on a decentralized network consisting of a series of nodes which are connected but not managed by a single entity called a [blockchain](https://ethereum.org/en/developers/docs/intro-to-ethereum/).

A [Dapp](https://ethereum.org/en/developers/docs/dapps/), or a decentralized application, is designed utilizing smart contracts which execute on a blockchain network and users interact with the application using a front-end application either through a web browser or mobile application.

Traditional applications consist of a front-end application which interacts with a back-end program running on a centralized server that manages all the back-end data. Traditional web application architecture consists of a frontend client and a backend server. The front and backend interact with each other by sending special messages generally using a protocol called [JSON-RPC](https://www.jsonrpc.org/specification) (although others can be used).

The benefits of Dapps over traditional applications include:

-   Decentralized means that they execute independently on a decentralized network and not controlled by a centralized authority.

-   Deterministic in that they perform the same function independent of which node on the network executes the code.

-   Blocks on the [Ethereum blockchain](https://ethereum.org/en/) contain [smart contracts](https://ethereum.org/en/developers/docs/smart-contracts/), which are [Turing [complete](https://en.wikipedia.org/wiki/Turing_completeness), meaning that they can perform any action which can be executed by a series of commands.

-   Smart contracts are executed in a virtual environment known as [Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/). If a smart contract has a bug, it won't affect other blocks or the normal functioning of the blockchain network.

[Smart contracts](https://ethereum.org/en/developers/docs/smart-contracts/) are pieces of code which are executed by the blockchain. Using the [Solidity](https://solidity.readthedocs.io/en/v0.7.4/) coding language, developers can create programs which are executed by the Ethereum Virtual Machine (EVM) and build decentralized applications which execute independently across nodes spread around the world, autonomously.

Note, in Ethereum smart-contracts are accessible and transparent. A Dapp has its backend code running on a decentralized peer-to-peer network. Contrast this with an app where the backend code is running on centralized servers. A Dapp can have frontend code and user interfaces written in any language (just like an app) that can make calls to its backend. Furthermore, its frontend can be hosted on decentralized storage such as [IPFS](https://ipfs.io/) or [Swarm](https://swarm-guide.readthedocs.io/).