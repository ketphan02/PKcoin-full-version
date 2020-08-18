import hashlib

class Block:
    def __init__(self, datetime, transactions, prevHash = ''):
        self.key = 0
        self.datetime = datetime
        self.transactions = transactions
        self.prevHash = prevHash
        self.hash = self.hashFunc()
        
    def hashFunc(self):
        hashData = str(self.datetime) + str(self.transactions) + str(self.prevHash) + str(self.key)
        hashData = hashData.encode()
        hashData = str(hashlib.sha256(hashData).hexdigest())
        return hashData

    def mineBlock(self, diff):
        while self.hash[0:diff] != "0" * diff:
            self.key = self.key + 1
            self.hash = self.hashFunc()

        print(self.hash)

    def hasValidTransactions(self):
        for trans in self.transactions:
            if not trans.isValid():
                return False
        return True
