import flask
import binascii

from PKcoin.elements.block import Block
from PKcoin.elements.chain import BlockChain
from PKcoin.elements.transactions import Transactions

from ecdsa import SigningKey, VerifyingKey
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
CORS(app)

with open('./PKcoin/keys/private_key.pem') as f:
    private_key = SigningKey.from_pem(f.read())

with open('./PKcoin/keys/public_key.pem') as f:
    public_key = VerifyingKey.from_pem(f.read())

PKcoin = BlockChain()

data = PKcoin.pendingTransactions
del PKcoin.pendingTransactions
PKcoin_json = flask.json.dumps(PKcoin, default=lambda o: o.__dict__)
PKcoin.readd(data)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/get_blockchain/")
def get_blockchain():
    return PKcoin_json

@app.route("/mine_blockchain/")
def mine_blockchain():
    PKcoin.minePendingTransactions(public_key)

    big_data = PKcoin.pendingTransactions
    del PKcoin.pendingTransactions
    
    data = []
    for i in range(len(PKcoin.chain)):
        data.append(PKcoin.chain[i].transactions)
        del PKcoin.chain[i].transactions
    PKcoin_json = flask.json.dumps(PKcoin, default=lambda o: o.__dict__)
    for i in range(len(PKcoin.chain)):
        PKcoin.chain[i].readd(data[i])
    PKcoin.readd(big_data)
    print(PKcoin.getBalance(public_key))
    # print(big_data)   
    return PKcoin_json

if __name__ == "__main__":   
    app.run(debug=True)