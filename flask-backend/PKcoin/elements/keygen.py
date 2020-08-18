from ecdsa import SigningKey, SECP256k1

sk = SigningKey.generate(curve=SECP256k1)

f = open('./flask-backend/PKcoin/keys/private_key.pem', 'wb')
pem = sk.to_pem()
f.write(pem)
f.close()

f = open('./flask-backend/PKcoin/keys/public_key.pem', 'wb')
pem = sk.get_verifying_key().to_pem()
f.write(pem)
f.close()