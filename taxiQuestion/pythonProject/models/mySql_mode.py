from models.my_sql_driver import MySqlDriver

class MySqlMode(object):

    def __init__(self):
        self.mysql_driver = MySqlDriver()
        self.engine, self.session = self.mysql_driver.connect_mysql()

    def mysql_repeat(self, _engine, _session):
        engine, session = self.mysql_driver.mysql_repeat(_engine, _session)
        return engine, session