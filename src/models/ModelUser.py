from .entities.User import User

class ModelUser:
    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, mail, password, fullname FROM user WHERE mail = %s"""
            cursor.execute(sql, (user.mail,))
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                if User.check_password(row[2], user.password):
                    user = User(row[0], row[1], row[2], row[3])
                    return user
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
