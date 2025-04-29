import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        return (
            f"Block Index    : {self.index}\n"
            f"Timestamp      : {time.ctime(self.timestamp)}\n"
            f"Previous Hash  : {self.previous_hash}\n"
            f"Hash           : {self.hash}\n"
            f"Data           : {self.data}\n"
            f"Nonce          : {self.nonce}\n"
            f"{'-'*41}"
        )


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def __str__(self):
        return "\n".join(str(block) for block in self.chain)


blockchain = Blockchain()

while True:
    data = input("Enter transaction data for the new block (or 'q' to quit): ")

    if data.lower() == "q":
        break

    blockchain.add_block(data)
    print("\nBlock added successfully!")

print("\nFinal Blockchain:")
print(blockchain)

print("\nBlockchain is valid:", blockchain.is_chain_valid())
