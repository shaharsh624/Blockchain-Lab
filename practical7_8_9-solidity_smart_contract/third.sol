// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyBlockchain {

    struct Block {
        uint index;
        uint timestamp;
        string data;
        string previousHash;
    }

    Block[] public chain;

    constructor() {
        createGenesisBlock();
    }

    function createGenesisBlock() private {
        chain.push(Block({
            index: 0,
            timestamp: block.timestamp,
            data: "Block - CrowdFunding Records",
            previousHash: "0"
        }));
    }

    function addBlock(string memory data) public {
        Block memory latestBlock = chain[chain.length - 1];
        uint newIndex = latestBlock.index + 1;
        uint newTimestamp = block.timestamp;
        string memory previousHash = latestBlock.previousHash;

        chain.push(Block({
            index: newIndex,
            timestamp: newTimestamp,
            data: data,
            previousHash: previousHash
        }));
    }
    
    function getBlock(uint index) public view returns (Block memory) {
        require(index < chain.length, "Block does not exist.");
        return chain[index];
    }

    function getChainLength() public view returns (uint) {
        return chain.length;
    }
}