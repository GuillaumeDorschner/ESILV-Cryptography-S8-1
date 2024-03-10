import tink
from argon2 import PasswordHasher
from flask_login import login_user
from tink import daead

from .models import User


def _init_tink():
    try:
        daead.register()
        keyset_handle = tink.new_keyset_handle(
            daead.deterministic_aead_key_templates.AES256_SIV
        )
        return keyset_handle
    except Exception as e:
        return None


class AuthManager:
    def __init__(self, db):
        try:
            self.db = db
            self.password_hasher = PasswordHasher()
            self.tink_keyset_handle = _init_tink()
        except Exception as e:
            pass

    def hash_password(self, password):
        """
        Hash a password using a salt, using the argon2.
        args:
            password: str
        """
        # No need to store the salt in DB, it is already included in the hash
        try:
            return self.password_hasher.hash(password)
        except Exception as e:
            return None

    def encrypt_password(self, hashed_password):
        """
        Encrypt a hashed password
        args:
            hashed_password: str
        """
        try:
            daead_primitive = self.tink_keyset_handle.primitive(
                daead.DeterministicAead
            )
            encrypted_hash = daead_primitive.encrypt_deterministically(
                hashed_password.encode(), b""
            )
            return encrypted_hash
        except Exception as e:
            return None

    def register(self, email, password):
        """
        Register a new user
        args:
            email: str
            password: str
        return:
            bool
        """
        try:
            hashed_password = self.hash_password(password)
            encrypted_hash = self.encrypt_password(hashed_password)
            self.db.add_user(email, encrypted_hash)
            user = User(
                email=email,
                password=encrypted_hash,
            )
            self.db.session.add(user)
            self.db.session.commit()
            print("User added")
            return True
        except Exception as e:
            return False

    def decrypt_password(self, encrypted_hash):
        """
        Decrypt an encrypted password
        args:
            encrypted_hash: str
        """
        try:
            daead_primitive = self.tink_keyset_handle.primitive(
                daead.DeterministicAead
            )
            decrypted_hash = daead_primitive.decrypt_deterministically(
                encrypted_hash, b""
            )
            return decrypted_hash.decode()
        except Exception as e:
            # Handle the exception here
            return None

    def login(self, email, password):
        """
        Login a user
        args:
            email: str
            password: str
        return:
            User object on success, None otherwise.
        """
        try:
            user = self.db.query.filter_by(email=email).first()
            if user:
                decrypted_hash = self.decrypt_password(user.password)
                if self.password_hasher.verify(decrypted_hash, password):
                    login_user(user)
                    print("User logged in")
                    return user
                else:
                    return None
            return None
        except Exception as e:
            return None
