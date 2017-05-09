import hashlib

BUF_SIZE = 65536  # reading 64kb chunks

sha256 = hashlib.sha256()

with open('environment.py', 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        print(data)
        if not data:
            break
        sha256.update(data)

print("SHA256: {0}".format(sha256.hexdigest()))
