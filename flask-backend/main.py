import flask
import binascii 

from PKcoin.elements.block import Block
from PKcoin.elements.chain import BlockChain
from PKcoin.elements.transactions import Transactions

from ecdsa import SigningKey, VerifyingKey

app = flask.Flask("__main__")

with open('./PKcoin/keys/private_key.pem') as f:
    private_key = SigningKey.from_pem(f.read())

with open('./PKcoin/keys/public_key.pem') as f:
    public_key = VerifyingKey.from_pem(f.read())

PKcoin = BlockChain()

@app.route("/")
def home():
    return flask.render_template("index.html", PKcoin = PKcoin.chain)

app.run(debug=True)