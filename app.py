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

if __name__ == '__main__': # Will only run code inside if statement when program is run directly by python interpreter
    app.run()


#Question 7 POST/dataGenerator


import csv
import mysql.connector

class D:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
    
    def read_data_from_csv(self,csv_file_path):
        dt=[]
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    dt.append(row)
        except IOError:
            print(f"Error: Could not read data from CSV file '{csv_file_path}'")
        return dt 
    





if __name__ == '__main__':
    app.run()




