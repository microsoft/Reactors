Technologies for building an Ethereum Decentralized Application
---------------------------------------------------------------

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

> Drizzle includes the following components:

-   **[@drizzle/store](https://github.com/trufflesuite/drizzle/blob/develop/packages/store/README.md):**-
    is the state manager of Drizzle. It handles the boilerplate for web3
    connection as synchronizing Smart Contract state and events.

    -   Fully reactive contract data, including state, events and
        > transactions.

    -   Declarative so as not to waste valuable cycles on unneeded data.

    -   Maintains access to underlying functionality. Web3 and
        > contract\'s methods are still there, untouched.

-   [**@drizzle/react-plugin**](https://github.com/trufflesuite/drizzle/tree/master/packages/react-plugin):-
    defines the Drizzle Provider for a React project.

    -   Abstracts away the boilerplate of creating a dapp front-end

    -   Handles instantiating web3 and contracts, fetching accounts, and
        > keeping all of this data in sync with the blockchain.

-   [**@drizzle/react-components**](https://github.com/trufflesuite/drizzle/tree/master/packages/react-components):-
    is a collection of primitive web controls that transforms Smart
    Contract data types to their appropriate html controls.

    -   Provides a set of useful components for common UI elements.

-   [**@drizzle/vue-plugin**](https://github.com/trufflesuite/drizzle/blob/develop/packages/vue-plugin/README.md):-
    a Vue adaptor and collection of html controls to support developing
    a Vue dapp.

[![](Images\image1.png)](https://www.trufflesuite.com/drizzle)

![](Images\image2.png)
-----------------------------------------------------------------

Below is a good visual representation of how Drizzle works with the dap
and keeps track of the data.

[![](Images\image3.png)](https://www.trufflesuite.com/docs/drizzle/reference/how-data-stays-fresh)