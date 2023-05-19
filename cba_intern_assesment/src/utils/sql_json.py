import json
import pandas as pd
from sqlalchemy import create_engine

#Database credentials
user='root'
password='F00tb@11z'
host= 'localhost'
database = 'lou'


class DataMethods:

    def get_transactional_data_date(transaction_date):
        engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}")

        #Now we are quering the database with pandas
        #Query is just the string to filter
        query = f"SELECT * FROM transactional_data WHERE transaction_date <= '{transaction_date}'"
        # this takes filter and the engine to connect it
        re = pd.read_sql_query(query,engine)

        #Converts to dictionary.
        data= re.to_dict(orient='records')

        #Convert to json
        json_convert =json.dumps(data)

        return json_convert
    

