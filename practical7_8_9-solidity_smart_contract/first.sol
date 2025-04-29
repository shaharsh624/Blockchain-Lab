// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWorld {
    string enter;

    function set(string memory value) public {
        enter = value;
    }

    function get() public view returns(string memory) {
        return enter;
    }
}
