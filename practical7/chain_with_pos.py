import hashlib
import time
import random


class Block:
    def __init__(self, index, previous_hash, data, validator, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.validator = validator
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.validator}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        return (
            f"Block Index    : {self.index}\n"
            f"Timestamp      : {time.ctime(self.timestamp)}\n"
            f"Previous Hash  : {self.previous_hash}\n"
            f"Hash           : {self.hash}\n"
            f"Data           : {self.data}\n"
            f"Validator      : {self.validator}\n"
            f"Nonce          : {self.nonce}\n"
            f"{'-'*41}"
        )


class Validator:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = []  # List of validators

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", "None")

    def get_latest_block(self):
        return self.chain[-1]

    def add_validator(self, name, stake):
        validator = Validator(name, stake)
        self.validators.append(validator)

    def choose_validator(self):
        total_stake = sum(v.stake for v in self.validators)
        chosen_value = random.uniform(0, total_stake)
        cumulative_stake = 0
        for validator in self.validators:
            cumulative_stake += validator.stake
            if cumulative_stake >= chosen_value:
                return validator.name

    def add_block(self, data):
        latest_block = self.get_latest_block()
        chosen_validator = self.choose_validator()
        new_block = Block(len(self.chain), latest_block.hash, data, chosen_validator)
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


# Initialize the blockchain
blockchain = Blockchain()

# Adding some validators with different stakes
blockchain.add_validator("Validator1", 10)  # Validator with 10 units of stake
blockchain.add_validator("Validator2", 20)  # Validator with 20 units of stake
blockchain.add_validator("Validator3", 5)  # Validator with 5 units of stake

while True:
    data = input("Enter transaction data for the new block (or 'q' to quit): ")

    if data.lower() == "q":
        break

    blockchain.add_block(data)
    print("\nBlock added successfully!")

print("\nFinal Blockchain:")
print(blockchain)

print("\nBlockchain is valid:", blockchain.is_chain_valid())
