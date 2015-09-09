__all__ = ["pdict"]

import sqlite3

class pdict(object):
    def __init__(self, filename, *, journal_mode="DELETE"): 
        schema = "(key BLOB PRIMARY KEY, value BLOB)"
        self.connection = sqlite3.connect(filename)
        self.connection.execute("PRAGMA journal_mode = %s" % journal_mode)
        self.connection.execute("CREATE TABLE IF NOT EXISTS dict " + schema)
        self.connection.commit()

    def select_one(self, query, arg=None):
        try: return next(iter(self.connection.execute(query, arg)))
        except StopIteration:
            return None

    def commit(self):
        if self.connection is not None:
            self.connection.commit()

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.commit()
        self.close()

    def __contains__(self, key):
        query = "SELECT 1 from dict where key = ?"
        return self.select_one(query, (key,))

    def __getitem__(self, key):
        query = "SELECT value FROM dict WHERE key = ?"
        item = self.select_one(query, (key,))
        if item is None:
            raise KeyError(key)
        return item[0]

    def get(self, key, default=None):
        try: return self[key]
        except KeyError:
            return default

    def __setitem__(self, key, value):
        query = "REPLACE INTO dict (key, value) VALUES (?, ?)"
        self.connection.execute(query, (key, value))

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        query = "DELETE FROM dict WHERE key = ?"
        self.connection.execute(query, (key,))

    def keys(self):
        query = "SELECT key FROM dict ORDER BY rowid"
        return [key[0] for key in self.connection.execute(query)]

    def values(self):
        query = "SELECT value FROM dict ORDER BY rowid"
        return [value[0] for value in self.connection.execute(query)]

    def items(self):
        query = "SELECT key, value FROM dict ORDER BY rowid"
        return [(item[0], item[1]) for item in self.connection.execute(query)]
