pragma solidity >=0.5.0 <0.7.0;

contract AssetManager {
    address public manager;

    struct Asset {
        address owner;
        string name;
        uint price;
        bool owned;
        bool exists;
    }

    mapping (uint => Asset) public assets;

    event AssetAdded(address sender, string name, string assetType);
    event AssetTransfer(address sender, address from, address to, string name, string assetType);

    // Constructor code is only run when the contract
    // is created
    constructor() public {
        manager = msg.sender;
    }

    function addAsset(string memory _name, string memory _assetType, uint _price, address _owner) public {
        require(msg.sender == manager, "Only the Asset Manager can add assets");
        uint assetId = uint(keccak256(abi.encodePacked(_name, _assetType)));
        require(!assets[assetId].exists, "Asset name and type already added");

        Asset memory a = Asset({
            owner: _owner,
            name: _name,
            owned: false,
            price: _price,
            exists: true
          }
        );

        assets[assetId] = a;
        emit AssetAdded(msg.sender, _name, _assetType);
    }

    function isAvailable(string memory _name, string memory _assetType) public view returns (bool) {
        uint assetId = uint(keccak256(abi.encodePacked(_name, _assetType)));
        Asset memory a = assets[assetId];
        return a.exists && !a.owned;
    }

    function getOwner(string memory _name, string memory _assetType) public view returns (address) {
        uint assetId = uint(keccak256(abi.encodePacked(_name, _assetType)));
        Asset memory a = assets[assetId];
        require(a.exists, "Asset does not exist");
        return a.owner;
    }

    function getPrice(string memory _name, string memory _assetType) public view returns (uint) {
        uint assetId = uint(keccak256(abi.encodePacked(_name, _assetType)));
        Asset memory a = assets[assetId];
        require(a.exists, "Asset does not exist");
        return a.price;
    }


    function getManager() public view returns (address) {
        return manager;
    }

    function transferAsset(address from, address to, string memory _name, string memory _assetType) public {
        require(msg.sender == manager, "Only the AssetManager can transfer assets");
        uint assetId = uint(keccak256(abi.encodePacked(_name, _assetType)));
        Asset memory a = assets[assetId];

        require(a.exists, "Asset must exist");
        require(a.owner == from, "Asset must be owned by from address");

        a.owner = to;
        assets[assetId] = a;

        emit AssetTransfer(msg.sender, from, to, _name, _assetType);
    }
}