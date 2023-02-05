from passlib.context import CryptContext

pwd_hash = CryptContext(schemes="bcrypt", deprecated="auto")


class Hash:
    # it will hash the password
    def bcrypt(password: str):
        return pwd_hash.hash(password)

    # it will verify the password
    def verify(hash_password, plain_password):
        return pwd_hash.verify(plain_password, hash_password)
