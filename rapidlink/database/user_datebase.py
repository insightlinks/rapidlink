from rapidlink.database.sqlite import Database


class UserDatabase:
    def __init__(self) -> None:
        self.db = Database("user.db")
        self.db.execute(
            sql="""CREATE TABLE IF NOT EXISTS user
                (id INTEGER PRIMARY KEY,
                 userid TEXT not null unique DEFAULT (hex(randomblob(16))), 
                 username TEXT not null unique,
                 password TEXT,
                 status TEXT DEFAULT "active",
                 created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                 updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )""",
        )

    def insert(self, userid, username, password):
        self.db.execute(
            sql="""INSERT INTO user (userid, username, password, status, created_at, updated_at)
                VALUES (?, ?, ?, "active", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)""",
            params=(userid, username, password),
        )
        return self.get(username)

    def get(self, username=None, userid=None):
        if username:
            self.db.execute(
                sql="""SELECT * FROM user WHERE username = ?""",
                params=(username,),
            )
        elif userid:
            self.db.execute(
                sql="""SELECT * FROM user WHERE userid = ?""",
                params=(userid,),
            )
        return self.db.cur.fetchone()

    # 注销
    def deactivate(self, userid):
        self.db.execute(
            sql="""UPDATE user SET status = "inactive" WHERE userid = ?""",
            params=(userid,),
        )
        return self.get(userid)

    # 激活
    def activate(self, userid):
        self.db.execute(
            sql="""UPDATE user SET status = "active" WHERE userid = ?""",
            params=(userid,),
        )
        return self.get(userid)


user_db = UserDatabase()
