import jwt
from datetime import datetime, timedelta

print("===================Encoding===================")

#Reading private key
read_private_key = open("private_key.pem", 'rb')
private_key = read_private_key.read()

payload = {
    "name" : "Desouza and Associates Inc.",
    "iss" : "D+A India",
    "iat" : datetime.now(),
    "exp" : int((datetime.now() + timedelta(minutes=15)).timestamp())
}

#Encoding payload data with private key
encoded = jwt.encode(payload, private_key, algorithm="RS256")
print(encoded)

read_private_key.close()

print("\n ===================Decoding===================")

#Reading public key
read_public_key = open("public_key.pem", 'rb')
public_key = read_public_key.read()

#Decoding JWT token with public key
decoded = jwt.decode(encoded, public_key, algorithms="RS256")
print(decoded)

read_private_key.close()
