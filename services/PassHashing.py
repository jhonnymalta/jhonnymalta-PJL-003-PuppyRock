from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def hashing_pass(mypass) -> str:
    hashed_password = bcrypt.generate_password_hash(password=mypass)
    return hashed_password