#Question 7 POST/dataGenerator
import pandas as pd
from sqlalchemy import create_engine



#Database credentials
user='root'
password='F00tb@11z'
host= 'localhost'
database = 'lou'

path = "\\C:\\cba_intern_assesment\\src\\data"
class DataProcessor:
    def __init__(self):
        self.engine = None
    
    #Command where Pandas loads csv
    def read_data_from_csv(self, path ):
        try:
            data = pd.read_csv(path)
            return data
        except FileNotFoundError:
            print(f"Error: {path} not found.")
            return None
    
    def store_data_to_mysql(self, data, database, table, host='localhost', user='root', password='F00tb@11z'):
        try:
            # Creates SQLAlchemy engine
            self.engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
            
            # Store data to MySQL using pandas
            data.to_sql(table, con=self.engine, if_exists='replace', index=False)
            
            print("loaded data successfully")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.engine:
                self.engine.dispose()



