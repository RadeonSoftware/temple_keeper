from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

# encryption
def aesEncrypt(plaintext, password, header = 'unnamed data'):
    plaintext = plaintext.encode()
    header = header.encode()
    key = hashlib.sha256(password.encode('utf-8')).digest()
    nonce = get_random_bytes(13)
    cipher = AES.new(key, AES.MODE_CCM, nonce)
    cipher.update(header)
    data = header, cipher.encrypt(plaintext), cipher.nonce, cipher.digest()
    return data

# decryption
def aesDecrypt(data, password):
    header, encrypted, nonce, mac = data
    key = hashlib.sha256(password.encode('utf-8')).digest()
    cipher = AES.new(key, AES.MODE_CCM, nonce)
    cipher.update(header)
    plaintext = cipher.decrypt(encrypted)
    try:
         cipher.verify(mac)
         print("The message is authentic: header=%s, pt=%s" % (header, plaintext))
    except ValueError:
         print("Key incorrect or message corrupted")

# key = hashlib.sha256(password.encode('utf-8')).digest() wird direkt nach erfolgreichem login ausgeführt und sollte
# danach nicht mehr aufgerufen werden sodass das benutzerpasswort nicht mehr im klartext in irgend einer variable
# vorliegt. demnach sollte das argument passwort durch key ersetzt werden und die variable mit klartextpasswort muss
# gelöscht werden
