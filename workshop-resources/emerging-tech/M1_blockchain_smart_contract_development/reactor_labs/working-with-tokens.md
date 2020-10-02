# Content


- [ERC 20 Tokens](#ERC-20-Tokens)
     - [Defining Features of ERC20](#Defining-Features-of-ERC20)
     - [Common uses for ERC20](#Common-uses-for-ERC20)
     - [Implement your own ERC20 token contract](#Implement-your-own-ERC20-token-contract)
     - [Example: ERC20 contract](#Example-ERC20-contract)


# ERC 20 Tokens

## Tokens
Tokens are like ether (ETH) but may have different design decisions, purposes and help operate different DAPPs and facilitate crypot-economics of different Blockchain ecosystems. For example Augur is a network that functions as a prediction market (you can think of it as a betting platform), and Augur has its own token (also ERC20) called REP. This is no different than you using tokens perhaps to take public transport. We have fiat/local currency, for example CAD (sometimes also comes in coins) and also TTC (Toronto Transit Commission) tokens and each TTC token allows you to take 1 subway ride. You can purchase TTC tokens using CAD (just like you can purchase REP using ETH) but they are not the same thing. TTC tokens are specifically for the eco-system of Toronto Transit.
There are many different types of tokens but today we will focus on the ERC20 standard.
(Even within ERC20 there are many different tokens for different Blockchain ecosystems. In fact the ERC20 token standard was highly correlated with the ICO craze you may remeber from ~2016-2017.)

## Defining Features of ERC20
ERC20 standardized the commonalities of many common fungible tokens and allows other tokens to operate in a more inter-operable manner on the Ethereum chain. (ERC20 tokens are the vast majority of the ICO tokens.)
Fungible means,  there is no difference between one token vs. another. You can think of this as coins in your daily life. Each 1$ is just like any other $1 but they are not physically the same thing (you can hold 1 in left hand and 1 in the right hand).
ERC20 tokens defines mostly a interface (6 functions to be implemented by you) and also the key fields like token name.
For more information about ERC20 tokens please see the [EIP](https://eips.ethereum.org/EIPS/eip-20.)



## Common uses for ERC20
Because of the features defined by ERC20 standards:
They are commonly and well suited for:
- medium of exchange, acts like currency i.e. similar to bitcoins
- represents rights / shares i.e. Augur, if USPS were to implement a blockchain voting system ERC20 standards would be a good choice



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
