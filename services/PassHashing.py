from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def hashing_pass(mypass) -> str:
    hashed_password = bcrypt.generate_password_hash(mypass,10)
    return hashed_password

def check_pass(hash,mypass) ->bool:
    return  bcrypt.check_password_hash(hash,mypass)