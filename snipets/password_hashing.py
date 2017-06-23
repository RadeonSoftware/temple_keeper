from passlib.hash import pbkdf2_sha256

# encryption
hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)
print(hash)

# verification
hash = pbkdf2_sha256.verify("password", hash)
print('hash status:', hash)

password_register_cache = input()
password_register_recall_cache = input()
password_register = pbkdf2_sha256.encrypt(password_register_cache, rounds=200000, salt_size=16)
valid = pbkdf2_sha256.verify(password_register_recall_cache, password_register)
print(valid)