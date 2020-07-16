pragma solidity >=0.5.0 <0.7.0;

import "./Bank.sol";
import "./AssetManager.sol";

contract Banker {
    // The keyword "public" makes variables
    // accessible from other contracts
    address public banker;

    Bank public bank;

    AssetManager public assetManager;

    enum Piece {Unassigned, Bitcoin, Ethereum, Monero, ZCash, YCash, Stellar}

    struct  Player {
        address addr;
        string name;
        bool taken;
        Piece piece;
    }

    mapping(string => bool) public names;
    mapping(address => Player) public addrPlayerMapping;

    Player[] public players;

    event GameStarted();
    event GameStopped();

    event PlayerJoined(address player, string name);

    bool public started;
    bool public ended;

    // Constructor code is only run when the contract
    // is created
    constructor() public {
        banker = msg.sender;
        bank = new Bank();
        bank.mint(banker, 100000);

        assetManager = new AssetManager();
        publishProperties();
    }

    function publishProperties() private {
        assetManager.addAsset("Redmond Reactor", "Property", 100, banker);
        assetManager.addAsset("Seattle Reactor", "Property", 100, banker);
        assetManager.addAsset("San Francisco Reactor", "Property", 100, banker);
        assetManager.addAsset("New York Reactor", "Property", 100, banker);
        assetManager.addAsset("Toronto Reactor", "Property", 100, banker);
        assetManager.addAsset("London Reactor", "Property", 100, banker);
        assetManager.addAsset("Sao Paulo Reactor", "Property", 100, banker);
        assetManager.addAsset("Tel Aviv Reactor", "Property", 100, banker);
        assetManager.addAsset("Stockholm Reactor", "Property", 100, banker);
        assetManager.addAsset("Abu Dhabi Reactor", "Property", 100, banker);
        assetManager.addAsset("Sydney Reactor", "Property", 100, banker);
        assetManager.addAsset("Shanghai Reactor", "Property", 100, banker);
        assetManager.addAsset("Bangalore Reactor", "Property", 100, banker);
    }

    function startGame() public {
        require(msg.sender == banker, "Only the Banker can start the game");
        require(!started, "Game already started");

        uint length = players.length;
        require(length >= 2, "Need at least two players");

        for(uint i = 0; i < length; i++) {
            Player memory p = players[i];
            bank.mint(p.addr, 1000);
        }

        started = true;

        emit GameStarted();
    }

    function stopGame() public {
        require(msg.sender == banker, "Only the Banker can stop the game");
        require(started, "Can't stop an unstarted game");
        require(!ended, "Game already ended");
        started = false;
        ended = true;
        emit GameStopped();
    }

    function joinGame(string memory _name) public {
        require(players.length < 6, "Game is full");
        require(!names[_name], "Name is already taken");
        require(!isPlayerInGame(msg.sender), "Same address is not already joined");

        Player memory p = Player({
            addr: msg.sender,
            name: _name,
            taken: true,
            piece: Piece.Unassigned
          }
        );
        players.push(p);
        names[_name] = true;
        addrPlayerMapping[msg.sender] = p;

        emit PlayerJoined(msg.sender, _name);
    }

    function getBalance(address account) public view returns (uint) {
        require(msg.sender == account || msg.sender == banker,
           "You cannot get a balance on someone else's account");
        return bank.getBalance(account);
    }

    function isPropertyAvailable(string memory _name) public view returns (bool) {
        return assetManager.isAvailable(_name, "Property");
    }

    function getPropertyOwner(string memory _name) public view returns (address) {
        return assetManager.getOwner(_name, "Property");
    }

    function getPropertyManager() public view returns (address) {
        return assetManager.getManager();
    }

    function getNumberOfPlayers() public view returns (uint) {
        return players.length;
    }

    function isPlayerInGame(address _addr) public view returns (bool) {
       Player memory p = addrPlayerMapping[_addr];
       return p.taken;
    }

    function buyProperty(string memory _name) public {
        require(isPropertyAvailable(_name), "Property is available");
        require(started, "Game is started");
        Player memory p = addrPlayerMapping[msg.sender];
        require(p.taken, "Address is in game");

        address owner = assetManager.getOwner(_name, "Property");
        uint price = assetManager.getPrice(_name, "Property");

        require(owner != msg.sender, "Player can't already own the property");
        require(bank.getBalance(msg.sender) >= price, "Player can afford property");

        bank.sendMoney(owner, msg.sender, price);
        assetManager.transferAsset(owner, msg.sender, _name, "Property");
    }
}