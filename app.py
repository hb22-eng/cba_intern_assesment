from flask import Flask, jsonify, request


import csv

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



# b. GET Transactional Data
#Make our Query Database
import datetime

def query_transac_data(start_date, end_date):

    @app.route('/getTransactionalData', methods = ['GET'])

    def get_Transactional_data():
        date = request.args.get('date') #dictionary collection request.args.get
        try:
            new_date = datetime.datetime.strptime(date, '%YYYY-%MM-%DD').date()
        except ValueError:
            return jsonify({'ERROR: Date format is Invalid. Please use YYYY-MM-DD.'}), 400
    
    current_date = datetime.date.today() #Retreiving current date

    new_transactional_data = query_transac_data(new_date, current_date) #query_dtbase will be defined later

    return jsonify(new_transactional_data)




#Question 7 POST/dataGenerator

import mysql.connector
class DataProcessor:
    def read_data_from_csv(self,csv_file_path):
        data=[]
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except IOError:
            print(f"Error: Could not read data from CSV file '{csv_file_path}'")
        return data
   
    def store_into_mysql(self,data):
 #CREATE MYSQL CONNECTION
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password = 'F00tb@11z',
            database = 'your_database')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE/TABLE')
            insert_query = 'Insert DATA'
            cursor.executemany(insert_query,data)
            
            
            conn.commit()
            cursor.close()
            conn.close()



            print("loaded data successfully")





if __name__ == '__main__':
    app.run()



