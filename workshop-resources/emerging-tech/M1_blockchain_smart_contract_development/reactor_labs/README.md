# Content
* [Advanced uses of data structures](#Advanced-uses-of-data-structures)
* [What is Remix?](#What-is-Remix?)
* [Get started with Remix](#Get-started-with-Remix)
* [What is MetaMask Plug-in?](#What-is-MetaMask-Plug-in?)
* [Download MetaMask](#Download-MetaMask)
* [Add MetaMask](#Add-MetaMask)
* [Get Started with MetaMask](#Get-Started-with-MetaMask)
* [Create a Wallet](#Create-a-Wallet)
* [Secret Backup Phrase](#Secret-Backup-Phrase)
* [Why do Testnets Exist](#Why-do-Testnets-Exist)
* [What is a faucet and how to use the Kovan faucet](#What-is-a-faucet-and-how-to-use-the-Kovan-faucet)
* [Introduction to Oracles](#Introduction-to-Oracles)
     * [What are Oracles](What-are-Oracles)
     * [Why do they exist](Why-do-they-exist)
     * [Main Challenges](Main-Challenges)
     * [Current Oracle Solutions](Current-Oracle-Solutions)
     * [Example: contract w oracles](Example-contract-w-oracles)
* [Request Kovan Ether](#Request-Kovan-Ether)
* [MetaMask deploy using injected Web3 on Kovan Test Network](#MetaMask-deploy-using-injected-Web3-on-Kovan-Test-Network)
* [ERC 20 Tokens](#ERC-20-Tokens)
     * [Defining Features of ERC20](#Defining-Features-of-ERC20)
     * [Common uses for ERC20](#Common-uses-for-ERC20)
     * [Implement your own ERC20 token contract](#Implement-your-own-ERC20-token-contract)
     * [Example: ERC20 contract](#Example-ERC20-contract)

<br>

# Advanced uses of data structures
Hopefully you've had time to review the basic data strucutures.
Here we review some of the more advance uses of these data structures / how they work together. 
The focus for now is to show you how they work via examples because we will be seeing / using them for subsequent smart contracts.

#### Nested mappings, mapping => structs)
```solidity
pragma solidity ^0.6.0;

contract AdvDataStructures {
    event LogNewAlert(string _msg, string _s);


    // quick review
    mapping(uint256 => uint256) public thisIsAMapping;


    struct innerSTRUCT {
        string f1;

    }


    // ___________now lets have some fun

    // nested mapping

    mapping(string => mapping(uint8 => uint8)) public nestedMapping;

    // nested list_of_structs
    struct STRUCT {
        uint8 field1;
        string field2;
        innerSTRUCT field3;
    }

    // nested array
    string[][] nestedArr = [["one"],["two"]];

    // array of struct pattern
    STRUCT[] list_of_structs;



   function create_nested_mapping() public {
    // no pure assign on contract level... must be in function
    nestedMapping['0'][0] = 2;
    thisIsAMapping[0]=99;

    innerSTRUCT memory tempInnerStruct = innerSTRUCT({
        f1: "inner"
    });


    STRUCT memory tempStruct = STRUCT({ field1: 1,
            field2: "socks",
            field3: tempInnerStruct
    });

    list_of_structs.push(tempStruct);
    // storage get =  list_of_structs[1];

    string storage read = list_of_structs[0].field3.f1;

    emit LogNewAlert("we read from list of struct storage: ", read);
    emit LogNewAlert("we read nestedArr: ", nestedArr[0][1]);

    }

    // try to make 3x nested mapping : )
}
```


# What is Remix?
Remix is an online IDE (Integrated Development Environment) you can use to write smart contracts. You can compile, test and deploy them for free. You can use Remix both online and offline.


# Get started with Remix
1. Go to https://remix.ethereum.org/
2. Create a new file and name it Shipping.sol
3. Copy + paste the code from the Shipping contract (This is available in the Learn Module / Prework)[LINK TO LEARN MODULE](htttps://url_tbd.com)
4. Compile the Shipping contract
5. Choose Environment - JavaScript VM
6. Deploy the Shipping contract

Now you can test the deployed contract and its functions.


# What is MetaMask Plug-in?
Metamask itself is a cryptocurrency wallet. <br>
Metamask also is a plug-in that will bring Ethereum to your browser. Metamask does so by making a window.web3 and window.ethereum object available that helps your browswer communicate with the blockchain. <br>
You can choose to connect to the Main Ethereum Network as well as test networks.<br>
As a user you can use it as a crypto wallet to store ether, and for developers it is mainly used to deploy smart contracts. <br><br>
Let’s see how metamask plugin and remix work together to make smart contract development low barrier to entry and a breeze. <br>
(NOTE: if you use MetaMask as a wallet and as a dev tool, it’ll be more secure to make 2 separate accounts) <br>

<br>

# Download MetaMask
- Download MetaMask [here](https://metamask.io/download.html)
* Add your browser of choice (Firefox or Chrome)

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/install%20metamask.png)

<br>

# Add MetaMask
* You will be redirected to add the extension. <br>
Click on Add to Firefox (or Chrome) <br>

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/add%20to%20firefox.png)

<br><br>

* Click Add extension. <br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/add%20metamask%20add%20extension.png)

<br>

# Get Started with MetaMask
You will see Welcome to MetaMask. Click **Get Started**.
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/welcome_to_metamask.png)

<br>

# Create a Wallet
If you are new to Metamask you will create a wallet and set a new password. Click **Create a Wallet**.
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/create_wallet.jpg)

<br>

# Secret Backup Phrase
* Set a new password. You will now get a Secret Backup Phrase. Important! Make sure to store this Secret Backup Phrase somewhere safe since you can not get a hold of it if you do not save it. <br>

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/backup%20phrase.png)

<br><br>

* Confirm your Secret Backup Phrase. After this step you are done with the set up and connected to the main Ethereum network! <br>

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/confirm_backup_phrase.png)

<br>

# Why do Testnets Exist
When we are learning how to code smart contracts, we have the option to use test nets to do transactions without paying for it. <br>
Test nets run in parallel and are in most cases identical with the main net (the real net) but the tokens used are different (even though they might work the same way i.e. monopoly money vs real money, you can still use it to buy things but not in real life :) <br>

This means we can learn and see how it will work in real production without spending any money. <br>
This also means that we have NO EXCUSE to not test our contracts and audit them carefully. <br><br>

There are different test nets in MetaMask, for this tutorial we will use the **Kovan test Network**.

<br>

# What is a faucet and how to use the Kovan faucet
Faucet makes it possible for you to get test ether to use for a test network. It has no real value and you are not paying anything to use it. When you have set-up MetaMask you can change from **Main Ethereum Network** to **Kovan Test Network**. <br><br>

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/Kovan%20Network.png)

<br>

# Request Kovan Ether
* You can request Kovan Ether through your GitHub or Twitter account
* You will need your address from MetaMask
* You can submit your address here: https://faucet.kovan.network/ using your GitHub account.
* You can also get Kovan Ether through Gitter by using GitLab, Twitter or GitHub as a login. [Here](https://gitter.im/kovan-testnet/faucet) you will paste your address in a chat to request ether
* More information about Kovan Faucet can be found [here](https://github.com/kovan-testnet/faucet/blob/master/README.md) <br><br>

![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/account%20metamask.png)

<br>

# Introduction to Oracles

## What are Oracles
* A connection between a blockchain (on-chain) and the external off-chain world; oracles can interact with external software as well as hardware
     * An oracle is not a store of data, but is a layer on a separate network that queries and verifies external information before relaying it.
* Inbound: relays off-chain data from the external world to the blockchain or smart contract
     * EG: An IOT thermometer monitors heat inside a meat-delivery truck. A safe temperature range is agreed on in advance in the smart contact. The smart contract will automatically execute payment to the delivery service as long as the truck temperature stays within the range for the trip.
     * An inbound oracle communicates directly with the thermometer and the smart contract--only signing the smart contract for approved payment if the thermometer stays in the prespecified range.
* Outbound: relays on-chain data/events from a blockchain or smart contract to the external world
     * EG: After a hotel room’s address receives your payment, a smart contract communicates with an outbound oracle to unlock the door and turn on the electricity in your room.

<br>

## Why do they exist
* Oracles are our connection between the digital world and the physical world.
* Without oracles, smart contracts have much more limited application, especially in interfacing between our current web 2.0 world and the new web 3.0 world.
* Oracles are a large part of the “real-time” data benefit of blockchain applications
* If solved, this becomes a key part of the scalability solution… what can be offchain should be completed offchain, however we cannot do as much of that currently since we cannot guarantee “trust-worthiness” of the results

<br>

## Main Challenges
* “We can trust data from oracles but that requires we trust oracles… can we?”
* Scalability / cost: due to the complexity of operations need to verify or get multiple results (for additional validity) it’s frequently quite costly to use a oracle in production
* Increased risks (of centralization) and attack surface (Blockchain <> Oracles <> Other APIs)

<br>

## Current Oracle Solutions
This being an important piece of the blockchain multiple teams are actively working on possible solutions: <br>
- [Provable](https://provable.xyz/)
- [Chainlink](https://chain.link/)
* [cosmos + band protocol](https://bandprotocol.com/)
* [MSFT coco](https://azure.microsoft.com/en-us/blog/announcing-microsoft-s-coco-framework-for-enterprise-blockchain-networks/) (more permissioned / secure, less decentralization)
* Domain specific: i.e. Augur, Algorand etc... have a oracle component as well.

This technology is considered the cutting edge of the blockchain, while ChainLink is considered the current front runner and the most mature, it is still not super developer or user friendly. For example it’s very hard to debug why a certain oracle transaction failed, but like most things in blockchain, we’ll get there :)  

<br>

## Example contract w oracles


```solidity
pragma solidity ^0.6.0;

import "https://raw.githubusercontent.com/smartcontractkit/chainlink/develop/evm-contracts/src/v0.6/ChainlinkClient.sol";

contract APIConsumer is ChainlinkClient {

    uint256 public ethereumPrice;
    event LogNewAlert(string description);

    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    constructor() public {
        setPublicChainlinkToken();
        oracle = 0x2f90A6D021db21e1B2A077c5a37B3C7E75D15b7e;
        jobId = "29fa9aa13bf1468788b7cc4a500a45b8";
        fee = 0.1 * 10 ** 18; // 0.1 LINK
    }


    function requestEthereumPrice() public returns (bytes32 requestId)
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);

        // Set the URL to perform the GET request on
        // this is just a placeholder API for the purpose of demo
        request.add("get", "https://jsonplaceholder.typicode.com/todos/12");

        // we want to extract the info we want given a JSON response
        request.add("path", "id");

        // Sends the request
        emit LogNewAlert('req sent, waiting for resp');

        return sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * Receive the response in the form of uint256
     */
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId)
    {
        emit LogNewAlert("fulflll called");
        ethereumPrice = _price;
    }
}

```

# MetaMask deploy using injected Web3 on Kovan Test Network
* Copy the `APIConsumer` contract to [Remix](https://remix.ethereum.org/).

<br>

* Compile the code <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/compile%20remix.png)

<br>

* Choose **Injected Web3** as an Environment and click **Deploy** <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/injectedweb3_deploy_remix.png)

<br>

* Your contract should now be deployed with MetaMask!

<br>

* Get the testnet address <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/get%20testnet%20address.png)

<br>

* Go to https://kovan.chain.link/ and paste your testnet address in the field <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/get%20chain%20link.png)

<br>

* Go to MetaMask and click **Add Token** <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/Add%20token.png)

<br>

* Click Custom Token and paste the contract address, then click next. <br>
Contract address:`0xa36085F69e2889c224210F603D836748e7dC0088` <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/Add%20tokens%20next.png)

<br>

* Click **Add Tokens** <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/Add%20tokens%20LINK100.png)

<br>

* You will see 100 LINK. Click **SEND** <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/100_link.png)

<br>

* Add your deployed contract address to the field and choose amount of 10 LINK <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/send%20tokens%20add%20address.png)

<br>

* Confirm and then wait until status is not pending.
* Go to Remix. Click **ethereumPrice** which should be 0. Now click **requestEthereumPrice** and Confirm in MetaMask. <br><br>
![](https://github.com/Prtfw/MSFT_BC_M1/blob/helena/Labs/Images/request%20etherum%20remix.png)

<br>

* Afterwards click **ethereumPrice**, it should now be 12!

<br>

# ERC 20 Tokens

## Tokens
Tokens are like ether (ETH) but may have different design decisions, purposes and help operate different DAPPs and facilitate crypot-economics of different Blockchain ecosystems. For example Augur is a network that functions as a prediction market (you can think of it as a betting platform), and Augur has its own token (also ERC20) called REP. This is no different than you using tokens perhaps to take public transport. We have fiat/local currency, for example CAD (sometimes also comes in coins) and also TTC (Toronto Transit Commission) tokens and each TTC token allows you to take 1 subway ride. You can purchase TTC tokens using CAD (just like you can purchase REP using ETH) but they are not the same thing. TTC tokens are specifically for the eco-system of Toronto Transit. 
There are many different types of tokens but today we will focus on the ERC20 standard. 
(Even within ERC20 there are many different tokens for different Blockchain ecosystems. In fact the ERC20 token standard was highly correlated with the ICO craze you may remeber from ~2016-2017.)

## Defining Features of ERC20
ERC20 standardized the commonalities of many common fungible tokens and allows other tokens to operate in a more inter-operable manner on the Ethereum chain. (ERC20 tokens are the vast majority of the ICO tokens.) <br>
Fungible means,  there is no difference between one token vs. another. You can think of this as coins in your daily life. Each 1$ is just like any other $1 but they are not physically the same thing (you can hold 1 in left hand and 1 in the right hand). <br>
ERC20 tokens defines mostly a interface (6 functions to be implemented by you) and also the key fields like token name. 
For more information about ERC20 tokens please see the [EIP](https://eips.ethereum.org/EIPS/eip-20.)

<br>

## Common uses for ERC20
Because of the features defined by ERC20 standards: <br>
They are commonly and well suited for:
* medium of exchange, acts like currency i.e. similar to bitcoins
* represents rights / shares i.e. Augur, if USPS were to implement a blockchain voting system ERC20 standards would be a good choice

<br>

## Implement your own ERC20 token contract
We will be using OpenZepplin for our implementation because:
- saves time
- prevents bugs


## Example ERC20 contract
After you deploy the contract: 
- verify that you can reward the miner
- verify that you can transfer (notice that we are using the default transfer function proivded by OpenZepplin)
- If you get a error related to "allowance" or "approval" (a very common error for those new to working ERC20 tokens), can you figure out why by revewing the [EIP](https://eips.ethereum.org/EIPS/eip-20)? or searching on google?

```solidity

pragma solidity ^0.6.0;

import "https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/master/contracts/token/ERC20/ERC20.sol";

contract Token20 is ERC20 {

    event LogNewAlert(string description, address indexed _from, uint256 _n);

    constructor() ERC20("T20", "T20") public {
        _mint(msg.sender, 1000);
    }

    function _reward() public {
        emit LogNewAlert('_rewarded', block.coinbase, block.number);
        _mint(block.coinbase, 20);
    }


    // Fallback function
    fallback() external payable {}


}
```
