// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransferEther {
    event Transfer(address indexed from, address indexed to, uint256 amount);

    function sendEther(address payable _to) public payable {
        require(msg.value > 0, "You need to send some ether");
        require(_to != address(0), "Invalid address");

        _to.transfer(msg.value);

        emit Transfer(msg.sender, _to, msg.value);
    }

    receive() external payable {}
}
