from flask import Flask, jsonify, request

from datetime import datetime 


from src.utils.csv_sql_class import DataProcessor
data_processor = DataProcessor()
from src.utils.sql_json import DataMethods
Dtm = DataMethods()



app = Flask(__name__)

@app.route('/dataGenerator', methods=['POST']) #DATA generator path a.
def data_Generator():

    file_path = request.args.get('filePath') # path parameter

    data = process_csv(file_path)

    #Actual data response
    return { 'data': data}


def process_csv(file_path):
    data=[]

    with open(file_path, mode='r') as file: #r means it's read mode

        header_skip = file.readline().strip().split(',') #Title header skip

        for line in file:
            values =line.strip().split(',')
            row_data = dict(zip(header_skip, values))
            data.append(row_data)
    return data

# Calling the class to read the csv
csvdata = data_processor.read_data_from_csv("\\C:\\cba_intern_assesment\\src\\data")
# Calling class again to transfer to mySQL
data_processor.store_data_to_mysql(csvdata,database ='lou', table = 'newt')


# b. GET Transactional Data


@app.route('/getTransactionalData', methods = ['GET'])
def get_Transactional_data():
    date = request.args.get('date') #dictionary collection request.args.get
    try:
        new_date = datetime.date(date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'ERROR: Date format is Invalid. Please use YYYY-MM-DD.'}), 400
    
    current_date = datetime.now() #Retreiving current date
    
# Calling our methods class
    new_transactional_data = Dtm.get_transactional_data_date(date) #query_dtbase will be defined later
    
    return jsonify(new_transactional_data)



if __name__ == '__main__':
    app.run()




