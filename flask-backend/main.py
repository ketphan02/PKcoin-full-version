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

PKcoin = flask.json.dumps(PKcoin, default=lambda o: o.__dict__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/get_blockchain/")
def get_blockchain():
    return PKcoin

if __name__ == "__main__":   
    app.run(debug=True)