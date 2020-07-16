pragma solidity >=0.5.0 <0.7.0;

contract Bank {
    // The keyword "public" makes variables
    // accessible from other contracts
    address public minter;
    mapping (address => uint) public balances;

    // Events allow clients to react to specific
    // contract changes you declare
    event Sent(address from, address to, uint amount);

    // Constructor code is only run when the contract
    // is created
    constructor() public {
        minter = msg.sender;
    }

    // Sends an amount of newly created coins to an address
    // Can only be called by the contract creator
    function mint(address receiver, uint amount) public {
        require(msg.sender == minter, "Sender == Minter");
        require((amount < 1e60), "Amount isn't too big");

        balances[receiver] += amount;
    }

    // Sends an amount of existing coins
    // from any caller to an address
    function sendMoney(address receiver, address sender, uint amount) public {
        require(msg.sender == minter, "Only the banker can authorize transfers");
        require(amount <= balances[sender], "Insufficient balance.");
        balances[sender] -= amount;
        balances[receiver] += amount;
        emit Sent(sender, receiver, amount);
    }

    function getBalance(address account) public view returns (uint) {
        require(msg.sender == account || msg.sender == minter,
           "You cannot get a balance on someone else's account");
        return balances[account];
    }
}