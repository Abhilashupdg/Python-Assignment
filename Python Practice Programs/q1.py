import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(filename='sql_query.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def create_server_connection(host_name, user_name, user_password, database):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database
        )
        logging.info("Succesful in establishing the connection to the database")
    except Error as err:
        logging.info(f"Error: '{err}'")
    return connection


connection = create_server_connection("localhost", "root", "password@14322", "classicmodels")
logging.info(connection)


def get_query_result(connection, query):
    cursor = connection.cursor()
    result= None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        logging.info(f"Error: '{err}'")




query = """SELECT * FROM employees WHERE firstName = 'Leslie'"""
results = get_query_result(connection, query)
logging.info(results)



def get_one_result(results):
    try:
        for result in results:
            yield result
    except Error as err:
        logging.info(f"Error: '{err}'")


res = get_one_result(results)
logging.info(next(res))


