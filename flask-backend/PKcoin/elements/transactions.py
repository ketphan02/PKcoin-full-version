import hashlib
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import randrange_from_seed__trytryagain
import binascii

class Transactions:
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount

    def hashFunc(self):
        hashData = str(self.fromAddress) + str(self.toAddress) + str(self.amount)
        hashData = hashData.encode()
        hashData = hashlib.sha256(hashData).digest()
        return hashData

    def signTransactions(self, signKey):
        if signKey.get_verifying_key() != self.fromAddress:
            raise Exception("You cannot sign transactions for other wallets !")

        transactionsHash = self.hashFunc()
        self.signature = signKey.sign(transactionsHash)

    def isValid(self):
        if self.fromAddress == None:
            return True
        if self.signature == b'':
            raise Exception("No signature found !")

        publicKey = self.fromAddress
        return publicKey.verify(self.signature, self.hashFunc())