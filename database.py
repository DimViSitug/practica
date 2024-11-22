import sqlalchemy as sqla
import database

CONNECTION_STRING = "mysql+pymysql://is61-3:agt2ge8r@192.168.3.111/aaa"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()

    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())    
        return result
    
    def get_napravlenies(self):
        query = sqla.text("SELECT * FROM napravlenies")
        result_raw = self.connection.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def insert_napravlenies(self, id_patients,id_wards, doctor):
        self.cursor.execute('''
            INSERT INTO napravlenies (id_patients, id_wards, doctor)
            VALUES (id_patients,id_wards, doctor)
        ''', (id_patients,id_wards, doctor))
        self.connection.commit()

    def fetch_napravlenies(self, id_patients,id_wards,doctor  ):
        query = sqla.text('SELECT id_patients, id_wards, doctor FROM napravlenies')
        query = query.bindparams(sqla.bindparam("id_patients", id_patients))
        query = query.bindparams(sqla.bindparam("id_wards", id_wards))
        query = query.bindparams(sqla.bindparam("doctor", doctor))

        self.connaction.execute(query)
        self.connaction.commit() 
    


    if __name__ == "__main__":
         db = database.Database()
         print(db.get_napravlenies())