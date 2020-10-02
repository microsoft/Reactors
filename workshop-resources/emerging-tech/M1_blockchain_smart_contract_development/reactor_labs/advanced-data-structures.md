# Content
- [Advanced uses of data structures](#Advanced-uses-of-data-structures)



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
