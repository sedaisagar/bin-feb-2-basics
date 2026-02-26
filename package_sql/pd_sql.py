import pandas as pd
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker

class SQLUtils:
    DB_NAME = "ok_test"
    DB_USER = "postgres"
    DB_PASS = "root"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    def __init__(self):
        self.url=f"""postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"""
    
    def get_seed_data(self):
        data = [
            {
                "title": f"Title #{i}", 
                "description" : f"Description for #{i}"
            } for i in range(5000)]

        return pd.DataFrame(data)

    def insert(self, data, table_name):
        session = None
        try:
            # table_name="dummy_table_1"
            engine = create_engine(url=self.url) 
            # Creates a connection to the database
            Session = sessionmaker(bind=engine)
            session = Session()
            data.to_sql(
                name=table_name, con=engine, 
                if_exists='append',index=False
            ) # if table exists, overwrite the table.
            print('Dummy Data Inserted Successfully!')
            session.commit()
        except Exception as e:
            if session:
                session.rollback()
            print(f'Error occurred during loading to database: {str(e)}')
        finally:
            if session:
                session.close()


    def read_data(self):
        engine = create_engine(self.url)

        query = """
                SELECT * from dummy_table_1;
            """

        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result

instance = SQLUtils()

instance.insert(instance.get_seed_data(), "dummy_table_1")
data = instance.read_data()

for i in data:
    title, description = i
    print(f"Title :: >> {title}, Description :: >> {description}\n", "-"*50)

# pip install pandas sqlalchemy
