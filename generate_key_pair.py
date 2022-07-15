from Crypto.PublicKey import RSA

key = RSA.generate(2048)

public_key = key.public_key().export_key("PEM")
private_key = key.export_key("PEM")

with open("public_key.pem", 'wb') as pri_key:
    pri_key.write(public_key)

with open("private_key.pem", 'wb') as pub_key:
    pub_key.write(private_key)