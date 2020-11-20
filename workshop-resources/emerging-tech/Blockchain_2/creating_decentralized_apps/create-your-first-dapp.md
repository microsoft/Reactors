Build your first dapp using Drizzle and VS Code 
-----------------------------------------------

### Setting up the environment:

-   Pre-requisites:

    -   Git - [git](https://git-scm.com/) or [github](https://github.com/) and create an account

    -   Node.js - 'node -v' returns the version of node which is installed. If it is not installed, it can be installed from the [node.js](https://nodejs.org/en/) website.

    -   Solidity - included with VS Code Solidity Extension, dependency of the Blockchain Development Kit Extension

> ![](Images\image4.png)

-   Truffle and Ganache-cli - included with VS Code Blockchain Development Kit. Truffle and Ganache can be installed using npm install from a terminal window which will also install ganache-cli. If using this:

    -   npm install -g truffle

> ![](Images\image5.png)

-   Web3 1.0+ - check the version using "npm view web3 version"

-   Web Sockets - check if web sockets are installed via the extensions for VS Code

> ![](Images\image6.png)

[**Drizzle-box**](https://www.trufflesuite.com/boxes/drizzle) comes with several out of the box smart contracts to check out and a simplified **truffle-config.js** designed for development and testing. If using a prior **truffle project,** first create a clean and empty folder, **unbox** **Drizzle**, then copy over the current project - smart contracts, migrations, and other project-specific files.

### Using Drizzle to wire smart contacts to a front-end server

Unboxing Drizzle results in essentially two separate projects within a single directory: a **truffle** project and a **drizzle-react client** project**.** If you already have experience with **Truffle**, then directory structure will look familiar in the Smart Contract area. The primary difference will be how you wire it to **Web3** and configurations modification which need to be taken into account.

Step1: Create a clean, empty directory and scaffold out a drizzle-react project using the [Drizzle Truffle Box](https://www.trufflesuite.com/boxes/drizzle) using the following steps:

-   First, create a new empty directory and unbox Drizzle in that directory:

    -   mkdir drizzle_tutorial

    -   cd drizzle_tutorial

    -   truffle unbox drizzle

 ![](Images\image7.png)

-   **Unboxing Drizzle** may take a few minutes and will scaffold out a react app project. . Open **VSCode** and the directory structure will look like this:

> ![](Images\image8.png)

-   Unboxing drizzle has installed the node module for \@drizzle under the ./app/node_modules folder:

> ![](Images\image9.png)
-   In the Terminal, run the Truffle development console which spawns a development blockchain. This is very useful for compiling, deploying and testing locally and creates a list of 10 accounts.

    -   truffle develop

> ![](Images\image10.png)

-   From the development console for truffle, compile and migrate the smart contracts to the development blockchain. If desired, both ganache app and ganache-cli can also be used. Please see documentation for how to use it. The development blockchain will be running at [http://127.0.0.1:8545](http://127.0.0.1:8545). Consequently, **./truffle-config.js** will require this same host and port address.

```javascript
const path = require("path");

module.exports = {

    // See <http://truffleframework.com/docs/advanced/configuration>
    // to customize your Truffle configuration!

    contracts_build_directory: path.join(__dirname, "app/src/contracts"),

    networks: {

        development: { // used to be just develop

        host: "127.0.0.1", // Localhost (default: none)

        port: 8545, // Standard Ethereum port (default: none)

        network_id: "*", // Any network (default: none)
        },
    }
};
```

The **Truffle Drizzle-Box** comes with three contracts that use the drizzle components for connecting to a Dapp. The contracts directory contains the files: **ComplexStorage.sol**, **SimpleStorage.sol** and **TutorialToken.sol** which are used by the **Drizzle** tutorial.

Using the Truffle develop console, compile these smart contracts:

> ![](Images\image11.png)

### Deploying and Migrating Smart Contracts

-   To deploy a smart contract, Truffle requires a migrations file in the migrations folder. The migration files are numbered and executed in the order in which they are numbers. The initial migration file begins with the number "1" and is called "1_initial_migration.js". Additional migration files need a number larger than 1. All of the contacts can be migrated using a single file or multiple files.

-   The migrations folder has JavaScript files that help you deploy contracts to the network. These files are responsible for staging your deployment tasks, and they're written under the assumption that your deployment needs will change over time. A history of previously run migrations is recorded on-chain through a special Migrations contract. (source: [truffle: running-migrations](https://www.trufflesuite.com/docs/truffle/getting-started/running-migrations))

-   Take a look in the file **./migrations/2_deploy_contracts.js** located in the migrations folder.

```javascript
const SimpleStorage = artifacts.require("SimpleStorage");

const TutorialToken = artifacts.require("TutorialToken");

const ComplexStorage = artifacts.require("ComplexStorage");

const Shipping = artifacts.require("Shipping");

module.exports = function(deployer) {

    deployer.deploy(SimpleStorage);

    deployer.deploy(TutorialToken);

    deployer.deploy(ComplexStorage);

    deployer.deploy(Shipping);
};
```

-   From the development console, execute the command migrate to migrate and deploy the smart contracts.

> ![](Images\image12.png)
>
> ![](Images\image13.png)

### Testing the Smart Contracts

Truffle has an automated testing framework to facilitate the testing of contracts. All test files should be located in the test directory. To learn more, go to the Truffle documentation, in the section testing your contracts. The Truffle box comes with the file **simplestorage.js** for testing the smart contract.

In the Truffle console, test the **SimpleStorage** contract using the **test** command:

![](Images\image14.png)

### Explore and run the dapp

The Drizzle Box includes code using the dizzle libraries to connect the smart contracts to the dapp's front-end. That code exists within the \`app\` directory.

> ![](Images\image15.png)

### Wiring up the front-end to the smart contract

The files installed when unboxing drizzle contain templates and tutorial code which demonstrate how to wire up drizzle to several different contracts. The folder **./contracts** contains: **SimpleStorage.sol**, **ComplexStorage.sol** and **TutorialToken.sol**. Using these three solidity smart contract files, the tutorial demonstrates how to connect them using the **drizzle** components to the front-end. All front-end code is in the **./app/src** folder. The files which contain **drizzle** specific instructions are: **app.js**, **drizzleOptions.js** and **MyComponent.js.**

To get an understanding of how this can be extended to other smart contracts, review the components for connecting the contract to the front-end.

The file **MyComponent.js** contains the code for connecting the **SimpleStorage, ComplexStorage** and **TutorialToken** smart contracts with the front-end.

-   To create a drizzle component, import [react](https://reactjs.org/docs/react-api.html) and [@drizzle/react-components](https://github.com/trufflesuite/drizzle/tree/develop/packages/react-components) and create a component with AccountData, ContractData and ContractForm called newContextComponents.

```jsx
import React from "react";

import { newContextComponents } from "@drizzle/react-components";

import logo from "./logo.png";

const { AccountData, ContractData, ContractForm } =
newContextComponents;

export default ({ drizzle, drizzleState }) => {
// destructure drizzle and drizzleState from props

    return (
        <div className="App">
            <div>
                <img src={logo} alt="drizzle-logo" />
                <h1>Drizzle Examples</h1>
                <p>
                Examples of how to get started with Drizzle in various situations.
                </p>
            </div>

            <div className="section">
                <h2>Active Account</h2>

                <AccountData
                    drizzle={drizzle}
                    drizzleState={drizzleState}
                    accountIndex={0}
                    units="ether"
                    precision={3}
                />
            </div>

            <div className="section">
                <h2>SimpleStorage</h2>

                <p>
                This shows a simple ContractData component with no arguments, along with a form to set its value.
                </p>

                <p>
                    <strong>Stored Value: </strong>

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="SimpleStorage"
                        method="storedData"
                    />
                </p>

                <ContractForm drizzle={drizzle} contract="SimpleStorage"
                method="set" />

            </div>

            <div className="section">
                <h2>TutorialToken</h2>

                <p>
                Here we have a form with custom, friendly labels. Also note the token symbol will not display a loading indicator. We\'ve suppressed it with the <code>hideIndicator</code> prop because we know this variable isconstant.
                </p>

                <p>
                    <strong>Total Supply: </strong>

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="TutorialToken"
                        method="totalSupply"
                        methodArgs={[{ from: drizzleState.accounts[0]}]}
                    />{" "}

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="TutorialToken"
                        method="symbol"
                        hideIndicator
                    />
                </p>

                <p>
                    <strong>My Balance: </strong>

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="TutorialToken"
                        method="balanceOf"
                        methodArgs={[drizzleState.accounts[0]]}
                    />
                </p>

                <h3>Send Tokens</h3>
                <ContractForm
                    drizzle={drizzle}
                    contract="TutorialToken"
                    method="transfer"
                    labels={["To Address", "Amount to Send"]}
                />
            </div>

            <div className="section">
                <h2>ComplexStorage</h2>

                <p>
                Finally this contract shows data types with additional considerations.

                Note in the code the strings below are converted from bytes to UTF-8 strings and the device data struct is iterated as a list.
                </p>

                <p>
                    <strong>String 1: </strong>

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="ComplexStorage"
                        method="string1"
                        toUtf8
                    />
                </p>

                <p>
                    <strong>String 2: </strong>

                    <ContractData
                        drizzle={drizzle}
                        drizzleState={drizzleState}
                        contract="ComplexStorage"
                        method="string2"
                        toUtf8
                    />
                </p>

                <strong>Single Device Data: </strong>

                <ContractData
                    drizzle={drizzle}
                    drizzleState={drizzleState}
                    contract="ComplexStorage"
                    method="singleDD"
                />
            </div>
        </div>
    );
};
```

-   **./app/src/drizzleOptions.js** is used to create an **options** object and pass in the desired contract artifacts for **Drizzle** to instantiate. The convention is to name this file **drizzleOptions.js** but it is not necessary. The **options** object sets up and instantiates the Drizzle store. Note: that in this example, Web3 is connecting to localhost port 8545.

```javascript
import Web3 from "web3";

import ComplexStorage from "./contracts/ComplexStorage.json";

import SimpleStorage from "./contracts/SimpleStorage.json";

import TutorialToken from "./contracts/TutorialToken.json";

const options = {
    web3: {            
    block: false,
    customProvider: new Web3("ws://localhost:8545"),
    },

    contracts: [SimpleStorage, ComplexStorage, TutorialToken],
    events: {
        SimpleStorage: ["StorageSet"],        
    },
};

export default options;
```

-   **App.js** contains the code for the main app. It requires importing React and the Drizzle libraries including the [@drizzle/react-plugin](https://github.com/trufflesuite/drizzle/tree/develop/packages/react-plugin), [@drizzle/store](https://github.com/trufflesuite/drizzle/tree/develop/packages/store) and local drizzleOptions file. It must also import the component file which interacts directly with the smart contract. Instantiate a drizzle component called **drizzle:**

    -   **Const drizzle = new Drizzle (drizzleOptions);**

```jsx
import React from "react";
import { DrizzleContext } from "@drizzle/react-plugin";
import { Drizzle } from "@drizzle/store";
import drizzleOptions from "./drizzleOptions";
import MyComponent from "./MyComponent";
import "./App.css";

const drizzle = new Drizzle(drizzleOptions);

const App = () => {
    return (
        <DrizzleContext.Provider drizzle={drizzle}>
            <DrizzleContext.Consumer>
                {drizzleContext => {
                    const { drizzle, drizzleState, initialized } = drizzleContext;
                    
                    if (!initialized) {
                        return "Loading..."
                    }
                    
                    return (
                        <MyComponent drizzle={drizzle} drizzleState={drizzleState} />
                    )
                }}
            </DrizzleContext.Consumer>
        </DrizzleContext.Provider>
    );
}

export default App;
```

### Running the dapp:

The above steps walk through getting started, compiling and migrating the **Drizzle Box** tutorial. Open a new terminal window, and from the **./app** folder start up a local browser using this commands:

-   cd app

-   npm rebuild

-   npm run start

This command starts the web-pack dev server for React and opens up a new browser window for the React project which should result in the image below. Once this has been tested, close it by either closing the terminal window or \<ctrl-c\>. This confirms that react was correctly installed. React starts a web browser on [http://localhost:3000](http://localhost:3000) and automatically opens a browser window.

If you have MetaMask installed, you may need to close and re-open [http://localhost:3000](http://localhost:3000) from an incognito browser window.

You should see the following in your browser window. In this dapp, you can now interact with the contracts directly.

![](Images\image16.png)