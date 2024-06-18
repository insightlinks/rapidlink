import sqlite3


def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data


class Database:
    def __init__(self, db):
        # 临时允许跨线程访问
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.conn.row_factory = row_to_dict
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def execute(self, sql, params=()):
        self.cur.execute(sql, params)
        self.conn.commit()
