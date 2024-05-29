from werkzeug.security import check_password_hash, generate_password_hash
# entities/User.py

import bcrypt

class User:
    def __init__(self, id, mail, password, fullname="") -> None:
        self.id = id
        self.mail = mail
        self.password = password
        self.fullname = fullname

    @staticmethod
    def check_password(hashed_password, user_password):
        # Asegúrate de que hashed_password y user_password estén en el formato correcto
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))


