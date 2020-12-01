2.3 Post workshop challenge:
----------------------------

[For Reactors repository:](https://github.com/microsoft/Reactors/tree/main/workshop-resources/emerging-tech)

Create a GameToken using an ERC-721 Non-Fungible Token
------------------------------------------------------

### Fungible vs. Non-Fungible Tokens

A fungible token ([ERC-20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20)) represents an asset that can be exchanged for any other asset of equal value in its class.

-   A currency is an example of a fungible asset. A \$100 bill is equal to any other \$100 bill, you can freely exchange these bills with one another because they have the same value, no matter the serial number on the specific \$100 bill.

-   A Non-Fungible Token (NFT) is a unique token. Collectible items are non-fungible assets because each item can have a different value. Things like art, trading cards and other types of collectibles can be represented by NFT's using [ERC721](http://erc721.org/) tokens.

**ERC-721** was the first non-fungible token standard and currently still the most popular standard for representing **non-fungible digital assets**. The most important properties for this kind of asset is to have a way to check who owns what and a way to move things around.

Create a Crypto GameToken using ERC-721
---------------------------------------

Create a non-fungible GameToken using the [OpenZeppelin ERC-721](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721) libraries. To simplify the exercise, create a token that provides functions where an administrator can **mint** tokens and users can **transfer** tokens from one user to another.

The functions required will include the **address of the administrator**, **owner** of the token and **balance** for the different users. Because ERC-721 tokens are not interchangeable, each token has a unique token identifier.

To keep it simple, the GameToken requires the following functionality:

-   The Administrator can mint tokens.

-   Each User, including the administrator, has a balance which is initially 0.

-   Administrator can transfer a minted token to another user.

-   Users can transfer tokens to other users.

To create this project, use VS Code, Truffle and Drizzle to create a simple front end to interact with the GameToken smart contract.

This project assumes that **node.js** and **truffle** are already installed. In addition, for this project, we will be using the **MetaMask Chrome Extension**. If it isn't installed, go to https://metamask.io/ to download and install it. Once installed, walk through the steps to set up a user id and password. Use the ganache test network for localhost port **127.0.0.1:8545**. If it's not pre-configured, click on MetaMask icon, then scroll on the networks button, add a **Custom RPC**. For more information regarding getting set up with **MetaMask**, refer to: [Reactors/workshop-resources/emerging-tech/Blockchain_2/building_better_smart_contracts/getting-setup.md](https://github.com/microsoft/Reactors/blob/main/workshop-resources/emerging-tech/Blockchain_2/building_better_smart_contracts/getting-setup.md)

From the terminal command line, do the following:

\$ mkdir GameToken

\$ cd GameToken

\$ truffle unbox drizzle

For this tutorial, use **ganache-cli** which listens on 127.0.0.1:8545. If using the ganache application, adjust **truffle-config.js** accordingly.

Open the **GameToken** project in **VS Code**. This example will not be using the pre-installed contracts, they can be removed. The file structure looks like this:

![](Images\image30.png)

Next, to create the game token, create a file in the **./contracts** folder called **GameToken.sol** which uses Open Zeppelin libraries to create the ERC-721 token.

```
pragma solidity ^0.5.0;

import "@openzeppelin/contracts/token/ERC721/ERC721Full.sol";

import "@openzeppelin/contracts/token/ERC721/ERC721Mintable.sol";

contract GameToken is ERC721Full, ERC721Mintable {

    address public admin;

    constructor() ERC721Full("ERC721Token", "ERC721Token") public {

        admin = msg.sender;

    }

}
```

Then build the contract and confirm it compiles successfully. This will create the file: ./contracts/GameToken.json.

In the migration, 2_deploy_contracts.js, modify the migration to look like the following:

```javascript
const GameToken = artifacts.require("GameToken");

module.exports = function(deployer) {

    deployer.deploy(GameToken);

};
```

Next, using the templates for Drizzle, we are going to connect the Game Token to the front end similar to what was done previously. For this example, replace **./app/src/drizzleOptions.js** with the code below:

```javascript
import GameToken from './contracts/GameToken.json';

const options = {

    contracts: [GameToken],

    events: {

        GameToken: ['Transfer', 'Approval'],

    },

};

export default options;
```
Create three files in ./app/src for the ERC-721 functionality split between admin functionality, metadata functionality and Wallet Functionality: **Admin.js,** **TokenMetadata.j**s and **TokenWallet.j**s:

Create the file **./app/src/Admin.js** to represent the Administrator account which is the only account that can mint tokens. The administrator account (Account 0) needs to be connected to Metamask which will be discussed below. It checks to see if the account is Admin ("0") and if so, the mint() function is listed on the web-page:

```jsx
import React, { useState, useEffect } from "react";

import { drizzleReactHooks } from "@drizzle/react-plugin";

import { newContextComponents } from "@drizzle/react-components";

const { useDrizzle, useDrizzleState } = drizzleReactHooks;

const { ContractForm } = newContextComponents;

export default () => {

    const [isAdmin, setIsAdmin] = useState(false);

    const { drizzle } = useDrizzle();

    const state = useDrizzleState(state => state);

    useEffect(() => {

        const init = async () => {

            const admin = await drizzle.contracts.GameToken.methods.admin().call();

            setIsAdmin(admin.toLowerCase() === state.accounts[0].toLowerCase());

        }

        init();

    });

    if(!isAdmin) {

        return null;

    }

    return (

        <div className="App">*

            <div>

                <h2>Mint</h2>

                <ContractForm

                    drizzle={drizzle}

                    contract="GameToken"

                    method="mint"

                />

            </div>

        </div>

    );

};
```

**Create ./app/src/TokenMetadata.js -** this file implements the meta-data functionality which prints out the **account id of the Administrator**, the **Owner of a token**. They are more meta-data functionality that can be implemented as well, but for this example, we are keeping it simple.

```jsx
import React, { useState } from "react";

import { drizzleReactHooks } from "@drizzle/react-plugin";

import { newContextComponents } from "@drizzle/react-components";

const { useDrizzle, useDrizzleState } = drizzleReactHooks;

const { ContractData } = newContextComponents;

export default () => {

    const [ownerOfArg, setOwnerOfArg] = useState(undefined);

    const [isApprovedForAllArgs] = useState(undefined);

    const { drizzle } = useDrizzle();

    const state = useDrizzleState((state) => state);

    const handleSubmitOwnerOf = (e) => {

        e.preventDefault();

        setOwnerOfArg(e.target.elements[0].value);

        };

    return (

        <div className="App">

            <div>

                <h2>Admin</h2>

                <ContractData

                    drizzle={drizzle}

                    drizzleState={state}

                    contract="GameToken"

                    method="admin"

                />

            </div>

            <div>

                <h2>Owner of token</h2>

                <form onSubmit={handleSubmitOwnerOf}>

                    <input type="text"></input>

                    <button>Submit</button>

                </form>

                {ownerOfArg && (

                    <ContractData

                        drizzle={drizzle}

                        drizzleState={state}

                        contract="GameToken"

                        method="ownerOf"

                        methodArgs={[ownerOfArg]}

                    />

                )}

            </div>

        </div>

    );

};
```

**Create ./app/src/TokenWallet.js** manages the functionality associated with the wallet. In this example, the **Balance** and **Transfer** functions are implemented:

```jsx
import React from "react";

import { drizzleReactHooks } from "@drizzle/react-plugin";

import { newContextComponents } from "@drizzle/react-components";

const { useDrizzle, useDrizzleState } = drizzleReactHooks;

const { ContractData, ContractForm } = newContextComponents;

export default () => {

    const { drizzle } = useDrizzle();

    const state = useDrizzleState((state) => state);

    return (

        <div className="App">

            <div>

                <h2>Balance</h2>

                <ContractData

                    drizzle={drizzle}

                    drizzleState={state}

                    contract="GameToken"

                    method="balanceOf"

                    methodArgs={[state.accounts[0]]}

                />

            </div>

            <div>

                <h2>Transfer <h2>

                <ContractForm

                    drizzle={drizzle}

                    contract="GameToken"

                    method="transferFrom"

                />

            </div>

        </div>

    );

};
```

**Replace ./app/src/App.js** with the below instructions which executes the GameToken user interface to include **Admin**, **TokenMetadata** and **TokenWallet**:

```jsx
import React from "react";

import { Drizzle } from "@drizzle/store";

import { drizzleReactHooks } from "@drizzle/react-plugin";

import drizzleOptions from "./drizzleOptions";

import LoadingContainer from "./LoadingContainer.js";

import TokenMetadata from "./TokenMetadata.js";

import TokenWallet from "./TokenWallet.js";

import Admin from "./Admin.js";

const drizzle = new Drizzle(drizzleOptions);

const { DrizzleProvider } = drizzleReactHooks;

function App() {

    return (

        <div>

            <div className="container">

                <center>

                    <h1>Game Token</h1>

                    <DrizzleProvider drizzle={drizzle}>

                        <LoadingContainer>

                            <Admin />

                            <TokenMetadata />

                            <TokenWallet />

                        </LoadingContainer>

                    </DrizzleProvider>

                </center>

            </div>

        </div>

    );

}

export default App;
```

**Replace the code in ./app/src/LoadingContainer.js:**

```jsx
import React from "react";

import { drizzleReactHooks } from "@drizzle/react-plugin";

const { useDrizzleState } = drizzleReactHooks;

function LoadingContainer({ children }) {

    const drizzleStatus = useDrizzleState((state) => state.drizzleStatus);

    if (drizzleStatus.initialized === false) {

        return "Loading ...";

    }

    return <>{children}</>;

}

export default LoadingContainer;
```

Compiling, migrating and running the Tutorial
---------------------------------------------

Open a terminal window in VS Code and start up the Ganache client (by typing ganache-cli):

-   Ganache-cli

The output will look similar to the below image. Ganache sets up 10 accounts. Account (0) is the Game Administrator. ![](Images\image31.png)

From a second terminal window, run the following:

-   truffle compile

-   truffle migrate \--network develop

The output will look like this:

![](Images\image32.png)

Starting and Running the server:
--------------------------------

Open another terminal window in VS Code, cd to the app folder and run **npm install** then **npm run start** to start the server. This will bring up the server on localhost:3000.

In another terminal window, **cd ./app** and start the server using the commands:

-   cd app

-   npm install

-   npm run start

Don't worry if there are some warnings. These lines are just additional ERC721 functionality that isn't being used in this example:

![](Images\image33.png)
Initially, it will say GameToken Loading because the MetaMask accounts have not yet been connected.

Setting up the Accounts in MetaMask
-----------------------------------

Open your MetaMask browser and import the Administrator Account by copying the private key for Account (0). Open MetaMask and choose the network that ganache-cli is using: **Localhost 8545.** Then import an account for the Game Administrator on account (0) into Metamask using account (0)'s private key. In practice, you would not share this private key with anyone!

First, connect Metamask Account 1 to Localhost:3000.

![](Images\image34.png)

Import Account (0) from the **ganache-cli** into **Metamask** using the private key for that account then connect Account 2 to localhost 3000.

In this example, it will be imported into MetaMask Account 2:

![](Images\image35.png)

![](Images\image36.png)

When you have everything connected, select the account connected to the **ganache-cli account (0), refresh the browser window** and you will see:

![](Images\image38.png)

Minting and Transferring Tokens
-------------------------------

Now that the server is running on localhost:3000, mint and transfer tokens using the Administrator Account which has been imported into Metamask Account 2:

![](Images\image39.png)

Using the Admin Account id: 0xe4F6962dC983d69953fF16dF43650Be5c7e7cD02 mint Token \#1. Notice, the balance has been increased to 1 and when inspecting Metamask, token has been minted.

![](Images\image40.png)

Conclusion
----------

Continue to work with the GameItem to extend the functionality for developing other properties, minting additional tokens and transferring them between users. Import another account from ganache-cli to Metamask, connect it to the localhost:3000 network. Transfer a token from Account 2 to the new MetaMask account. Spend some time playing with the simple commands then try extending the example implementing new functionality of the ERC721 token.

This project demonstrated creating a non-fungible token, minting and transferring the token. There are many other functions which are available to non-fungible tokens which support the other options defined by the ERC-721 standard.
