// SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

contract File1 {
    // Variables
    string public myString = "My string";
    bool public myBool = true;
    uint public myUint = 1;
    int public myInt = 2;
    address public myAddress = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    string name = "";

    //Global Variables
    /*
        msg - data, gas, sender, sig, value
        tx - gas, origin
        block - number, timstamp, chainid, etc
    */


    // Functions
    function setMyName(string memory _name) public {
        name = _name;
    }

    function getMyName() public view returns(string memory) {
        return name;
    }

    function resetMyName() public {
        name = "";
    }


    // constructor
    constructor(string memory _name1) {
        name1 = _name1;
    }


    // Visibility
    /*
        public - accesible from anywhere (inside and outside)
        external - accesible only from outside unless specified using this [functions only]
        private - accesible within contract but not in derived contract    
        internal - accesible within contract and also in derived contract

        [default] - function: public
        [default] - variable: internal
    */
    string name1 = "name1";
    string public name2 = "name2";
    string private name3 = "name3";
    string internal name4 = "name4";


    // Modifiers: used to enforce certain conditions
    // view - can read but does not modify the blockchain (no gas cost)
    function getName() public view returns(string memory) {
        return name;
    }

    // pure - cannot read and modify (no gas cost) : mostly for calculations
    function add(uint a, uint b) public pure returns (uint) {
        return a+b;
    }

    // payable - recieve payment (gas cost)
    uint public balance = 0;
    function pay() public payable {
        balance += msg.value;
    }

    // Custom Modifiers
    address private owner = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    modifier onlyOwner {
        require(msg.sender == owner, 'caller must be owner');
        _;
    }
    function setNameByOwner(string memory _name) onlyOwner public {
        name = _name;
    }


    // operators - same as cpp
    // if else - same as cpp
    // loops - same as cpp


    // Array
    uint[] public array1 = [1, 2, 3];
    uint[] public array2;
    string[] public array3 = ["apple", "banana", "orange"];
    string[10] public array4;

    function getArrayIndex(uint i) public view returns (uint) {
        return array2[i];
    }

    function getArrayLength() public view returns (uint) {
        return array2.length;
    }

    function pushArray(uint i) public {
        array2.push(i);
    }

    function popArray() public {
        array2.pop();
    }

    function deleteArray(uint index) public {
        delete array2[index];
    }

    function getArray() public {
        for (uint i=0 ; i<array3.length ; i++) {
            printMessage(array3[i]);
        }
    }


    // Mappings - Dictionary
    mapping(uint => string) public names;
    mapping(uint => mapping(uint => uint)) public factors;

    function getNameMap(uint _id) public view returns(string memory) {
        return names[_id];
    }

    function setNameMap(uint _id, string memory _name) public {
        names[_id] = _name;
    }

    function removeNameMap(uint _id) public {
        delete names[_id];
    }


    // struct
    struct Book {
        string title;
        string author;
        bool completed;
    }

    mapping(uint => Book) public myBooks;

    function addBook(uint _index, string memory _title, string memory _author) public {
        myBooks[_index] = Book(_title, _author, false);
    }

    function getBook(uint _index) public view returns (Book memory) {
        Book storage book = myBooks[_index];
        return book;
    }

    function completeBook(uint _index) public {
        Book storage book = myBooks[_index];
        book.completed = true;
    }


    // Events - like print()
    /*
        indexed (upto 3) - allows it to be searchable in the logs
    */
    event Log(string indexed message);

    function printMessage(string memory text) public {
        emit Log(text); // Emit the event
    }


    // Ether
    /*
        1 ether = 10^9 gwei = 10^18 wei
    */


    // Fallback
    event FallbackCalled(address sender);

    fallback() external {
        emit FallbackCalled(msg.sender);
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function transfer(address payable _to) public payable {
        (bool sent, ) = _to.call{value: msg.value}("");
        require(sent, "Failed!");
    }


    // revert - reverts if condition is not met
    function example1(uint _value) public {
        if (_value <= 10) {
            revert("must be greater than 10");
        }
        emit Log("success");
    }
}


contract Ownable {
    address owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, 'caller must be owner');
        _;
    }

    function greet() public virtual returns (string memory) {
        return "Hello from Parent!";
    }
}

contract MyContract is Ownable {
    string public name = "Example 1";

    function setName(string memory _name) public onlyOwner {
        name = _name;
    }

    function greet() pure public override returns (string memory) {
        return "Hello from Child!";
    }
}
