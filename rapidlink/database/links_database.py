from rapidlink.database.sqlite import Database


class LinksDatabase:
    def __init__(self) -> None:
        self.db = Database("links.db")
        self.db.execute(
            sql="""CREATE TABLE IF NOT EXISTS links
                (id INTEGER PRIMARY KEY,
                 linkid TEXT not null unique DEFAULT (hex(randomblob(16))), 
                 type TEXT DEFAULT "phone",
                 value TEXT,
                 status TEXT DEFAULT "active",
                 created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                 updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )""",
        )

    def insert(self, linkid, type, value):
        self.db.execute(
            sql="""INSERT INTO links (linkid, type, value, status, created_at, updated_at)
                VALUES (?, ?, ?, "active", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)""",
            params=(linkid, type, value),
        )
        return self.get(linkid=linkid)

    def get(self, linkid=None):
        if linkid:
            self.db.execute(
                sql="""SELECT * FROM links WHERE linkid = ?""",
                params=(linkid,),
            )
        return self.db.cur.fetchone()

    def update(self, linkid, type, value):
        self.db.execute(
            sql="""UPDATE links SET type = ?, value = ? WHERE linkid = ?""",
            params=(
                type,
                value,
                linkid,
            ),
        )
        return self.get(linkid=linkid)

    def delete(self, linkid):
        self.db.execute(
            sql="""DELETE FROM links WHERE linkid = ?""",
            params=(linkid,),
        )
        return self.get(linkid=linkid)

    def list(self):
        self.db.execute(
            sql="""SELECT * FROM links""",
        )
        return self.db.cur.fetchall()


links_db = LinksDatabase()
