from .entities.User import User

class ModelUser():
    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, mail, password, fullname FROM user WHERE mail = %s"""
            cursor.execute(sql, (user.mail,))
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, mail, password, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            if row is not None:
                logged_user = User(row[0], row[1], None, row[3])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)