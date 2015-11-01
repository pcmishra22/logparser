import MySQLdb

class MyDB(object):
     
     _db_connection = None
     _db_cur = None

     def __init__(self,host,user,password,database):
          self._db_connection = MySQLdb.connect(host, user, password, database)
          self._db_cur = self._db_connection.cursor()

     def query(self, query, params):
          
          self._db_cur.execute(query, params)
          self._db_connection.commit()

     def __del__(self):
          self._db_connection.close()
