import sqlalchemy as sqla
import database

CONNECTION_STRING = "mysql+pymysql://is61-3:agt2ge8r@192.168.3.111/aaa"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connaction = self.engine.connect()

    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())    
        return result
    
    def get_patients(self):
        query = sqla.text("SELECT * FROM patients")
        result_raw = self.connaction.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def insert_patient(self, name, department, registrar):
        self.cursor.execute('''
            INSERT INTO patients (name, department, doctor)
            VALUES (?, ?, ?)
        ''', (name, department, registrar))
        self.connection.commit()

    def fetch_patients(self):
        self.cursor.execute('SELECT patients, department, doctor FROM napravlenies')
        return self.cursor.fetchall()
    


    if __name__ == "__main__":
        db = database.Database()
        print("спс")