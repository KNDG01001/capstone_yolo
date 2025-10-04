import pymysql

class ResidentInfo :
    def __init__(self, user, passwd, host, db) :
        try :
            self.conn = pymysql.connect(
                user = user,
                passwd = passwd,
                host = host,
                db = db,
                charset = 'utf8'
            )

            self.cur = self.conn.cursor()

        except Exception as e :
            print(f'Can\'t connect  db : {e}')

    def get_query(self, list_of_ids) :        
        format_strings = ','.join(['%s'] * len(list_of_ids))
        query = "SELECT floor FROM floors WHERE name in (%s)" % format_strings
        return query
    
    def execute(self, *args) :
        try :
            query = args[0]
            list_of_ids = args[1]
            self.cur.execute(query, tuple(list_of_ids))
        except IndexError :
            self.cur.execute(query)

    def fetchone(self) :
        try :
            return self.cur.fetchone()
        except Exception as e :
            print(f'{e}')
        
    def commit(self) :
        self.conn.commit()

    def close(self) :
        self.conn.close()

if __name__ == "__main__" :
    list_of_ids = ['홍길동']
    db = ResidentInfo(user = 'root', passwd='12345', host='localhost', db='resident')
    q = db.get_query(list_of_ids)
    # q = "SELECT floor FROM floors WHERE name = 'Warning'"
    db.execute(q, list_of_ids)
    print(db.fetchone())


















