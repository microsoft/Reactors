
Fundamentals of Blockchain Products and Development
---------------------------------------------------

Blockchain products are useful for a variety of applications ranging
from supply-chain management to decentralized finance. Blockchain
technology cuts across a variety of markets and geographies. As the
utilization of blockchain, distributed ledger and decentralized
technologies has evolved, so has the development of blockchains that
support enterprises, financial institutions and global networks.

The benefits of developing decentralized programs supports building
applications and infrastructures for a variety of use cases. When
architecting blockchain products, it's important to use the best suited
tools and platforms.

The primary reasons for creating blockchain products include:

-   Public verifiability since smart contracts are visible and auditable
    on the blockchain.

-   Transparency-based data and the process of updating the state is a
    requirement for public verifiability.

-   

-   On the other hand, it is possible to obtain a certain level of
    privacy using encryption.

-   Integrity of information ensures that it is protected from
    unauthorized modifications.

-   Redundancy is inherently provided through replication across the
    writers. In centralized systems, redundancy is generally achieved
    through replication on different physical servers and through
    backups.

-   Trust anchor defines who represents the highest authority of a given
    system that is entitled to grant and revoke read and write system
    access.

-   Valid network environments ensure that exchanged information, file
    storage and other transactions among devices are carried out in a
    reliable and transparent manner.

Public, Private and Hybrid/Consortium Blockchain
------------------------------------------------

There are several types of blockchains that manage the way that the
blockchains are accessed and utilized as well as how the blockchains
perform and whether the blockchain will be public, private or a hybrid.

-   **Public blockchains** are broadly available.

    -   Anyone can access transaction history, create new transactions,
        and validate them into new blocks.

    -   No need for trust, everything is recorded on the blockchain.

    -   Higher level of security since the more people using the
        blockchain, the more difficult it is to attack.

    -   Transparency of public blockchain increases potential use cases.

-   **Private/permissioned blockchains** provide infrastructure,
    handling and validating data transactions.

    -   Cost-effective because they don't require mining based consensus
        mechanisms and provide overall management over transactions
        within the chain.

    -   Only allows certain entities to participate.

    -   Participants are granted specific rights and restrictions in the
        network, so someone could have full access or limited access at
        the discretion of the network.

    -   More centralized in nature as only a small group controls the
        network.

    -   Private blockchains have fewer participants and thus are faster
        to achieve consensus.

    -   Private blockchains are more scalable since only a few nodes are
        authorized and responsible for managing data, the network is
        able to process more transactions.

-   **Hybrid/Consortium** blockchains are a combination of private and
    public blockchains.

    -   Used by a group of organizations that work jointly on developing
        different solutions.

    -   Restricted-access blockchain, each organization is able to
        maintain its intellectual property rights within the consortium.

    -   Hybrid between low-trust public blockchains and the
        highly-trusted private blockchains.

    -   The consortium is permissioned for a predetermined group of
        enterprises.

    -   It is semi-decentralized and under the supervision of a limited
        set of members.

    -   Utilizes multi-party consensus in that all operations are
        verified by special pre-approved nodes, not by the world
        community, like in bitcoin blockchain.

Some commonly used blockchains include:

-   [Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/):
    A public blockchain which is shared and utilized across a global
    network.

    -   Each new block is added utilizing the proof of work consensus
        model.

-   [Azure Blockchain
    Service](https://docs.microsoft.com/en-us/azure/blockchain/):
    A fully managed ledger service that enables users the ability to
    grow and operate blockchain networks at scale in Azure.

-   [Multichain](https://www.multichain.com/): MultiChain helps
    organizations to build and deploy blockchain applications.

-   [Hyperledger Besu](https://www.hyperledger.org/use/besu):
    Designed to be enterprise-friendly for both public and private
    permissioned network use cases.

Refer to the documentation for the [Microsoft Blockchain development
kit](https://marketplace.visualstudio.com/items?itemName=AzBlockchain.azure-blockchain)
for building, testing and deploying blockchain applications.

Building, Deploying and Managing Blockchain Products
----------------------------------------------------

[Decentralized
applications](https://ethereum.org/en/developers/docs/dapps/)
differ from traditional applications in that they do not rely on a
centralized server network, but instead operate on a decentralized
network consisting of a series of nodes which are connected but not
managed by a single entity called a
[blockchain](https://ethereum.org/en/developers/docs/intro-to-ethereum/).

A [Dapp](https://ethereum.org/en/developers/docs/dapps/), or a
decentralized application, is designed utilizing smart contracts which
execute on a blockchain network and users interact with the application
using a front-end application either through a web browser or mobile
application.

Traditional applications consist of a front-end application which
interacts with a back-end program running on a centralized server that
manages all the back-end data. Traditional web application architecture
consists of a frontend client and a backend server. The front and
backend interact with each other by sending special messages generally
using a protocol called
[JSON-RPC](https://www.jsonrpc.org/specification) (although
others can be used).

The benefits of Dapps over traditional applications include:

-   Decentralized means that they execute independently on a
    decentralized network and not controlled by a centralized authority.

-   Deterministic in that they perform the same function independent of
    which node on the network executes the code.

-   Blocks on the [Ethereum blockchain](https://ethereum.org/en/)
    contain [smart
    contracts](https://ethereum.org/en/developers/docs/smart-contracts/),
    which are [Turing]{.ul}
    [complete](https://en.wikipedia.org/wiki/Turing_completeness),
    meaning that they can perform any action which can be executed by a
    series of commands.

-   Smart contracts are executed in a virtual environment known as
    [Ethereum Virtual
    Machine](https://ethereum.org/en/developers/docs/evm/). If a
    smart contract has a bug, it won't affect other blocks or the normal
    functioning of the blockchain network.

[Smart
contracts](https://ethereum.org/en/developers/docs/smart-contracts/)
are pieces of code which are executed by the blockchain. Using the
[Solidity](https://solidity.readthedocs.io/en/v0.7.4/) coding
language, developers can create programs which are executed by the
Ethereum Virtual Machine (EVM) and build decentralized applications
which execute independently across nodes spread around the world,
autonomously.

Note, in Ethereum smart-contracts are accessible and transparent. A Dapp
has its backend code running on a decentralized peer-to-peer network.
Contrast this with an app where the backend code is running on
centralized servers. A Dapp can have frontend code and user interfaces
written in any language (just like an app) that can make calls to its
backend. Furthermore, its frontend can be hosted on decentralized
storage such as [IPFS](https://ipfs.io/) or
[Swarm](https://swarm-guide.readthedocs.io/).

Building an Ethereum Decentralized Application
----------------------------------------------

Underlying Technologies for managing the frontend apps which interact
with the smart contacts can communicate via an API using a JSON-RPC
layer called the Web3 API.

-   [JSON-RPC](https://www.jsonrpc.org/specification) is a
    stateless, light-weight remote procedure call (RPC) protocol using
    JSON for the payload.

-   [Web3](http://web3) is the Ethereum compatible javascript API
    and bindings which is built using the JSON-RPC spec. Any
    decentralized app can use this s Web3.js for browser based DApps.

-   [Redux](https://redux.js.org/) is a predictable state
    container for JavaScript apps.

-   [React.js](https://reactjs.org/) is a JavaScript library for
    building user interfaces.

Tutorial for Building an Ethereum Dapp with VS Code and the Truffle Suite
-------------------------------------------------------------------------

The [Truffle Framework](https://www.trufflesuite.com/), which
provides a set of tools and boilerplate code for developing Ethereum
DApps and is integrated with [Microsoft's VS
Code](https://code.visualstudio.com/) [Blockchain development
extension](https://marketplace.visualstudio.com/items?itemName=AzBlockchain.azure-blockchain).

-   [Truffle](https://www.trufflesuite.com/docs/truffle/overview)
    is a development environment, testing framework and asset pipeline
    for blockchains using the Ethereum Virtual Machine (EVM). Truffle
    provides:

    -   Built-in smart contract compilation, linking, deployment and
        binary management.

    -   Automated contract testing for rapid development.

    -   Scriptable, extensible deployment & migrations framework.

    -   Network management for deploying to any number of public &
        private networks.

    -   Package management with EthPM & NPM, using the ERC190 standard.

    -   Interactive console for direct contract communication.

    -   Configurable build pipeline with support for tight integration.

    -   External script runner that executes scripts within a Truffle
        environment.

-   [Truffle Boxes](https://www.trufflesuite.com/boxes) are
    boilerplates that can contain helpful modules, Solidity contracts &
    libraries, front-end views and more; all the way up to complete
    example dapps.

-   [Ganache](https://www.trufflesuite.com/docs/ganache/overview)
    provides a personal blockchain that can be used for developing and
    testing Dapps. This tutorial will be using the ganache CLI (Command
    Line Interface) personal blockchain for testing and deploying smart
    contracts, but you can feel free to use
    [Ganache](https://www.trufflesuite.com/ganache) app as an
    alternate option.

-   [Drizzle](https://www.trufflesuite.com/docs/drizzle/overview)
    is a collection of front-end libraries that simplifies the process
    of writing smart contracts to Dapp front-ends. Drizzle provides the
    mechanisms for synchronizing and managing contract data and is based
    on a [Redux](https://redux.js.org/) store.

-   [Truffle Suite Drizzle
    Box](https://www.trufflesuite.com/boxes/drizzle) comes with
    the drizzle components required to start using smart contracts from
    a react app. Unboxing Drizzle will install all necessary
    dependencies and a **Create-React-App** is generated in the
    **./app** folder. **Drizzle** extends **web3 1.0**'s contacts and is
    a collection of libraries to simplify development of your Dapps in
    Plain JavaScript, React and Vue.

    -   **[\@drizzle/store](https://github.com/trufflesuite/drizzle/blob/develop/packages/store/README.md):**-
        is the state manager of Drizzle. It handles the boilerplate for
        web3 connection as synchronizing Smart Contract state and
        events.

        -   Fully reactive contract data, including state, events and
            > transactions.

        -   Declarative so as not to waste valuable cycles on unneeded
            > data.

        -   Maintains access to underlying functionality. Web3 and
            > contract\'s methods are still there, untouched.

    -   [**\@drizzle/react-plugin**](https://github.com/trufflesuite/drizzle/tree/master/packages/react-plugin):-
        defines the Drizzle Provider for a React project.

        -   Abstracts away the boilerplate of creating a dapp front-end

        -   Handles instantiating web3 and contracts, fetching accounts,
            > and keeping all of this data in sync with the blockchain.

    -   [**\@drizzle/react-components**](https://github.com/trufflesuite/drizzle/tree/master/packages/react-components):-
        is a collection of primitive web controls that transforms Smart
        Contract data types to their appropriate html controls.

        -   Provides a set of useful components for common UI elements.

    -   [**\@drizzle/vue-plugin**](https://github.com/trufflesuite/drizzle/blob/develop/packages/vue-plugin/README.md):-
        a Vue adaptor and collection of html controls to support
        developing a Vue dapp.

![](media\image1.png)

![](media\image2.png)
-----------------------------------------------------------------

Below is a good visual representation of how Drizzle works with the dap and keeps track of the data.
----------------------------------------------------------------------------------------------------

![](media\image3.png)

Configuring and wiring a simple smart storage smart contract using Drizzle Box and VS Code
------------------------------------------------------------------------------------------

### Setting up the environment:

-   Pre-requisites:

    -   Git - [git](https://git-scm.com/) or
        [github](https://github.com/) and create an account

    -   Node.js - 'node -v' returns the version of node which is
        installed. If it is not installed, it can be installed from the
        [node.js](https://nodejs.org/en/) website.

    -   Solidity - included with VS Code Solidity Extension, dependency
        of the Blockchain Development Kit Extension

> ![](media\image4.png)

-   Truffle and Ganache-cli - included with VS Code Blockchain
    Development Kit. Truffle and Ganache can be installed using npm
    install from a terminal window which will also install ganache-cli.
    If using this:

    -   npm install -g truffle

    -   truffle version

> ![](media\image5.png)

-   Web3 1.0+ - check the version using "npm view web3 version"

-   Web Sockets - check if web sockets are installed via the extensions
    for VS Code

> ![](media\image6.png)

[**Drizzle-box**](https://www.trufflesuite.com/boxes/drizzle)
comes with several out of the box smart contracts to check out and a
simplified **truffle-config.js** designed for development and testing.
If using a prior **truffle project,** first create a clean and empty
folder, **unbox** **Drizzle**, then copy over the current project -
smart contracts, migrations, and other project-specific files.

Using Drizzle to wire smart contacts to a front-end server
----------------------------------------------------------

Unboxing Drizzle results in essentially two separate projects within a
single directory: a **truffle** project and a **drizzle-react client**
project**.** If you already have experience with **Truffle**, then
directory structure will look familiar in the Smart Contract area. The
primary difference will be how you wire it to **Web3** and
configurations modification which need to be taken into account.

Step1: Create a clean, empty directory and scaffold out a drizzle-react
project using the [Truffle Drizzle
Box](https://www.trufflesuite.com/boxes/drizzle) using the
following steps:

-   First, create a new empty directory and unbox Drizzle in that
    directory:

    -   mkdir drizzle_tutorial

    -   cd drizzle_tutorial

    -   truffle unbox drizzle

> ![](media\image7.png)

-   **Unboxing Drizzle** may take a few minutes and will scaffold out a
    react app project. There is no need to run "**create-react-app**".
    Open **VSCode** and the directory structure will look like this:

> ![](media\image8.png)

-   Unboxing drizzle has installed the node module for \@drizzle under
    the ./app/node_modules folder:

> ![](media\image9.png)

-   In the Terminal, run the Truffle development console which spawns a
    development blockchain. This is very useful for compiling, deploying
    and testing locally and creates a list of 10 accounts.

    -   truffle develop

> ![](media\image10.png)

-   From the development console for truffle, compile and migrate the
    smart contracts to the development blockchain. If desired, both
    ganache app and ganache-cli can also be used. Please see
    documentation for how to use it. The development blockchain will be
    running at [http://127.0.0.1:8545](http://127.0.0.1:8545).
    Consequently, ./truffle-config.js will require this same host and
    port address.

> ![](media\image11.png)

The **Truffle Drizzle-Box** comes with three contracts that use the
drizzle components for connecting to a Dapp. The contracts directory
contains the files: **ComplexStorage.sol**, **SimpleStorage.sol** and
**TutorialToken.sol** which are used by the **Drizzle** tutorial.

Using the Truffle develop console, compile these smart contracts:

> ![](media\image12.png)

Deploying and Migrating Smart Contracts
---------------------------------------

-   To deploy a smart contract, Truffle requires a migrations file in
    the migrations folder. The migration files are numbered and executed
    in the order in which they are numbers. The initial migration file
    begins with the number "1" and is called "1_initial_migration.js".
    Additional migration files need a number larger than 1. All of the
    contacts can be migrated using a single file or multiple files.

-   The migrations folder has JavaScript files that help you deploy
    contracts to the network. These files are responsible for staging
    your deployment tasks, and they're written under the assumption that
    your deployment needs will change over time. A history of previously
    run migrations is recorded on-chain through a special Migrations
    contract. (source: [truffle:
    running-migrations](https://www.trufflesuite.com/docs/truffle/getting-started/running-migrations))

-   Take a look in the file **2_deploy_contracts.js** located in the
    migrations folder.

> ![](media\image13.png)

-   From the development console, execute the command migrate to migrate
    and deploy the smart contracts.

> ![](media\image14.png)
>
> ![](media\image15.png)

Testing the Smart Contracts
---------------------------

Truffle has an automated testing framework to facilitate the testing of
contracts. All test files should be located in the test directory. To
learn more, go to the Truffle documentation, in the section testing your
contracts. The Truffle box comes with the file **simplestorage.js** for
testing the smart contract.

In the Truffle console, test the **SimpleStorage** contract using the
**test** command:

![](media\image16.png)

The dApp
--------

The Drizzle Box includes code using the dizzle libraries to connect the
smart contracts to the dapp's front-end. That code exists within the
\`app\` directory.

> ![](media\image17.png)

Wiring up the front-end to the smart contract
---------------------------------------------

The files in the **/app** folder which are of interest for connecting
the smart contract to the Dapp are: **app.js**, **drizzleOptions.js**
and **MyComponent.js.** Using the SimpleStorage contract, below are the
steps for connecting the contract to the front-end:

-   The file **MyComponent.js** creates the component for connecting the
    SimpleStorage smart contract with the front-end.

> ![](media\image18.png)
>
> ![](media\image19.png)

-   **drizzleOptions.js** is used to create an **options** object and
    pass in the desired contract artifacts for **Drizzle** to
    instantiate. The **options** object sets up and instantiates the
    Drizzle store. Note that in this example, Web3 is connecting to
    localhost port
    8545.![](media\image20.png)

-   **App.js** contains the code for the main app. It requires importing
    React and the Drizzle libraries. It must also import the component
    file which interacts directly with the smart contract.

> ![](media\image21.png)

In another terminal:

Open a new terminal window, and from the **./app** folder start up a
local browser using this commands:

-   cd app

-   npm rebuild

-   npm run start

> ![](media\image22.png)

This command starts the web-pack dev server for React and opens up a new
browser window for the React project which should result in the image
below. Once this has been tested, close it by either closing the
terminal window or \<ctrl-c\>. This confirms that react was correctly
installed. React starts a web browser on
[http://localhost:3000](http://localhost:3000) and automatically
opens a browser window.

![](media\image23.png)

Shipping Contract from M1 to develop Shipping Dapp and interact with it in a web browser.
-----------------------------------------------------------------------------------------

In the module Smart Contract Basics, the tutorial worked through a Smart
Contract for a Shipping with three states: Pending, Shipped, Delivered.
In this section, we will walk through creating a simple front-end which
utilizes Shipping.sol to provide the following functionality:

-   Create a request to ship an item

-   Check on whether the item was shipped

-   Check on whether the item was delivered

For this example, we will use the same framework described above using
the **Truffle Drizzle Box**.  Using the project created above, modify the project to develop a Shipping Dapp by adding the Shipping smart contract, updating the migration and wiring it up to the front end using Drizzle.

-   **Shipping.sol** - use the Shipping contract below.

> ![](media\image24.png)

 
-   **2_deploy_contracts.js** - add the Shipping contract to the migrations file.

> ![](media\image27.png)

- Start a development server using **truffle develop**. Compile and migrate the shipping contract.

Wire up the Front-End of the Shipping Conract:
-----------------------------------------------------------------------------------------

-   Create a component file called ShipComponent.js by copying then modifying MyComponent.js.
-   Replace the code for the three tutorial contracts with the with the Shipping contract.

> ![](media\image25.png)
-   **drizzleOptions.js** also remains largely unchanged, but needs to
    **import Shipping.json.**

> ![](media\image26.png)

-   **App.js** file remains largely unchanged except for adding the new
    component file which needs to be imported.

> ![](media\image27.png)

Note: For reference on what a Learn module looks like, check out this
[Introduction to Blockchain
module](https://docs.microsoft.com/en-us/learn/modules/intro-to-blockchain/).

Post Workshop Challenge - Create a Crypto GameItem using ERC-721 Non-Fungible Tokens:
-----------------------------------------------------------------------------------------

Create a non-fungible ERC-721 to represent a Crypto [GameItem](https://docs.openzeppelin.com/contracts/2.x/erc721) using the OpenZeppelin ERC721. A fungible token represents an asset that can be exchanged for any other asset of equal value in its class.

- A currency is an example of a fungible asset. A $100 bill is equal to any other $100 bill, you can freely exchange these bills with one another because they have the same value, no matter the serial number on the specific $100 bill. They are fungible bills.
- A Non-Fungible Token (NFT) is a unique token. So collectible items are non-fungible assets and can be represented by NFTs using [ERC721](http://erc721.org/) token, VS Code and the TruffleSuite.
- Create a directory and unbox drizzle.
- Create a simple Dapp using the GameItem sample code with the Open Zeppelin 721 libraries and Drizzle.

ERC-721 was the first standard, and currently still the most popular standard, for representing non-fungible digital assets. The most important properties for this kind of asset is to have a way to check who owns what and a way to move things around.

> ![](media\image29.png)
