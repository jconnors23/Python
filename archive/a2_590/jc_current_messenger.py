import os
import pickle
import string
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import PublicFormat, Encoding, load_der_public_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Certificate:
    def __init__(self, name, pk):
        self.name = name
        self.pk = pk


class MessengerServer:
    def __init__(self, server_signing_key, server_decryption_key):
        self.server_signing_key = server_signing_key
        self.server_decryption_key = server_decryption_key

    # def decryptReport(self, ct):
    #     ss = self.server_decryption_key.exchange(ec.ECDH(), ct[0])
    #     pt = ct[1] / ss
    #     return pt

    def decryptReport(self, ct):
        k_pub, k_priv = generateKeys()
        shared_secret = k_priv.exchange(ec.ECDH(), self.server_decryption_key)
        # key from hashing 
        digest = hashes.Hash(hashes.SHA256())
        digest.update(self.server_decryption_key) 
        digest.update(shared_secret) 
        key = digest.finalize()
        # pt from symmetric decryption  
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        pt = decryptor.update(ct) + decryptor.finalize()
        return pt


    def signCert(self, cert):
        pk_bytes = cert["pk"].public_bytes(
            Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
        name = cert["name"]
        cert2 = {
            "name": name,
            "pk": pk_bytes
        }
        data = pickle.dumps(cert2)
        signature = self.server_signing_key.sign(
            data, ec.ECDSA(hashes.SHA256()))
        return signature


def generateKeys():
    private_key = ec.generate_private_key(ec.SECP256R1)
    public_key = private_key.public_key()

    return public_key, private_key


def ratchetHKDF(key, input):
    result_key = HKDF(
        algorithm=hashes.SHA256(),
        length=64,
        salt=key,
        info=None
    ).derive(input)
    first_half = result_key[:32]
    second_half = result_key[32:]
    return first_half, second_half


class MessengerClient:

    def __init__(self, name, server_signing_pk, server_encryption_pk):
        self.name = name
        self.server_signing_pk = server_signing_pk
        self.server_encryption_pk = server_encryption_pk
        # conns = { "Bob" : { "prev_pk": prev_pk,
        #                     "rk": rk,
        #                     "ck_sending: ck_sending",
        #                     "ck_receiving": ck_receiving,
        #                     "sent_prev_msg": true or false}}
        self.conns = {}
        # certs = { "Bob" : { "name" : "Bob"
        #                     "pk" : pk }}
        self.certs = {}

    def generateCertificate(self):
        pub_key, priv_key = generateKeys()
        self.curr_priv_key = priv_key
        self.curr_pub_key = pub_key
        self.init_priv_key = priv_key
        self.init_pub_key = pub_key
        cert = {
            "name": self.name,
            "pk": pub_key
        }
        return cert

    def receiveCertificate(self, certificate, signature):
        pk_bytes = certificate["pk"].public_bytes(
            Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
        name = certificate["name"]
        cert2 = {
            "name": name,
            "pk": pk_bytes
        }
        data = pickle.dumps(cert2)

        self.server_signing_pk.verify(
            signature, data, ec.ECDSA(hashes.SHA256()))

        self.certs[name] = certificate
        self.nonce = b"nonce"

    def sendMessage(self, name, message):
        if not name in self.conns.keys():
            # Establish Initial Root Key
            self.curr_priv_key = self.init_priv_key
            self.curr_pub_key = self.init_pub_key
            name_pk = self.certs[name]["pk"]
            self.rk = self.curr_priv_key.exchange(ec.ECDH(), name_pk)
            # print("initial root key")
            # print(self.rk)
            self.rk, self.ck_sending = ratchetHKDF(self.rk, b"root")
            # print("ck_sending")
            # print(self.ck_sending)

            # Derive Message Key through sending chain
            self.ck_sending, self.msg_key = ratchetHKDF(
                self.ck_sending, b"constant")

            # print("msg key")
            # print(self.msg_key)

            header = self.curr_pub_key

            keys = {"prev_pk": name_pk, "rk": self.rk, "ck_sending": self.ck_sending,
                    "ck_receiving": None, "sent_prev_msg": True}
            self.conns[name] = keys

        else:
            print("inside send else")
            self.rk = self.conns[name]["rk"]
            self.ck_sending = self.conns[name]["ck_sending"]

            if not self.conns[name]["sent_prev_msg"]:
                self.curr_pub_key, self.curr_priv_key = generateKeys()
                header = self.curr_pub_key
                self.shared_secret = self.curr_priv_key.exchange(ec.ECDH(),
                                                                 self.conns[name]["prev_pk"])
                self.rk, self.ck_sending = ratchetHKDF(
                    self.rk, self.shared_secret)
                self.ck_sending, self.msg_key = ratchetHKDF(
                    self.ck_sending, b"constant")
            else:
                self.ck_sending, self.msg_key = ratchetHKDF(
                    self.ck_sending, b"constant")
                header = self.curr_pub_key

            self.conns[name]["rk"] = self.rk
            self.conns[name]["ck_sending"] = self.ck_sending
            self.conns[name]["sent_prev_msg"] = True

        aesgcm = AESGCM(key=self.msg_key)
        enc_msg = aesgcm.encrypt(self.nonce, bytes(
            message, 'ascii'), header.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo))

        return header, enc_msg

    def receiveMessage(self, name, header, ciphertext):

        if not name in self.conns.keys():
            # Establish Initial Root Key
            self.curr_pub_key = self.init_pub_key
            self.curr_priv_key = self.init_priv_key
            name_pk = self.certs[name]["pk"]
            self.rk = self.curr_priv_key.exchange(ec.ECDH(), name_pk)
            # print("receive initial rk")
            # print(self.rk)
            self.rk, self.ck_receiving = ratchetHKDF(self.rk, b"root")
            # print("ck_receiving")
            # print(self.ck_receiving)

            # Derive Message Key through sending chain
            self.ck_receiving, self.msg_key = ratchetHKDF(
                self.ck_receiving, b"constant")

            # print("receiving msg key")
            # print(self.msg_key)
            keys = {"prev_pk": name_pk, "rk": self.rk, "ck_sending": None,
                    "ck_receiving": self.ck_receiving, "sent_prev_msg": False}
            self.conns[name] = keys

        else:

            self.rk = self.conns[name]["rk"]
            self.ck_receiving = self.conns[name]["ck_receiving"]

            if self.conns[name]["sent_prev_msg"]:

                print("inside receive else")
                shared_secret = self.curr_priv_key.exchange(ec.ECDH(), header)
                # self.ck_receiving = self.conns[name]["ck_receiving"]
                self.rk, self.ck_receiving = ratchetHKDF(
                    self.rk, shared_secret)
                self.ck_receiving, self.msg_key = ratchetHKDF(
                    self.ck_receiving, b"constant")

            else:

                self.ck_receiving, self.msg_key = ratchetHKDF(
                    self.ck_receiving, b"constant")

            self.conns[name]["prev_pk"] = header
            self.conns[name]["rk"] = self.rk
            self.conns[name]["ck_receiving"] = self.ck_receiving
            self.conns[name]["sent_prev_msg"] = False

        aesgcm = AESGCM(key=self.msg_key)
        try:
            dec_msg = aesgcm.decrypt(self.nonce, ciphertext, header.public_bytes(
                Encoding.DER, PublicFormat.SubjectPublicKeyInfo))
        except:
            return None

        return dec_msg.decode('ascii')

    # def report(self, name, message):
    #     k_pub, k_priv = generateKeys()
    #     s = k_priv.exchange(ec.ECDH(), self.server_encryption_pk)
    #     m_1 = name + message
    #     m_bytes = bytes(m_1, 'ascii')
    #     m_times_s = m_bytes * s
    #     ct = [k_pub, m_times_s]
    #     return m_1, ct

    def report(self, name, message):
        k_pub, k_priv = generateKeys()
        shared_secret = k_priv.exchange(ec.ECDH(), self.server_encryption_pk)
        # bytes_array = [server_encryption_pk, shared_secret]

        # hashing - https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
        digest = hashes.Hash(hashes.SHA256())
        digest.update(self.server_encryption_pk) 
        digest.update(shared_secret) 
        key = digest.finalize()

        # symmetric encryption - https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        m_1 = name + message 
        m_bytes = bytes(m_1, 'ascii') # convert to bytes beforee .update
        ct = encryptor.update(m_bytes) + encryptor.finalize()

        return ct 
        # Questions: 
        # which pk to use here? key = H(pk, shared secret) is it the server pk or k_pub that is generated on line 237 
        # can we calculate digest of both in steps like this or do we have to digest all the bytes at once? aka the whole bytes array at once
    