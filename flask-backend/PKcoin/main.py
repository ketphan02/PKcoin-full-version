from elements.chain import BlockChain 
from elements.block import Block
from elements.transactions import Transactions
from ecdsa import SigningKey, VerifyingKey
from hashlib import sha256
import binascii

with open('./keys/private_key.pem') as f:
    private_key = SigningKey.from_pem(f.read())

with open('./keys/public_key.pem') as f:
    public_key = VerifyingKey.from_pem(f.read())

PKcoin = BlockChain()

PKcoin.minePendingTransactions(public_key)
print(PKcoin.getBalance(public_key))

newTransaction = Transactions(public_key, 'someaddress', 10)
newTransaction.signTransactions(private_key)
PKcoin.addTransactions(newTransaction)


PKcoin.minePendingTransactions(public_key)
print(PKcoin.getBalance(public_key))