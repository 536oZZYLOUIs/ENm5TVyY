# 代码生成时间: 2025-09-23 19:39:09
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

"""
A Streamlit app that demonstrates SQL injection protection.
This app connects to a database and allows users to input queries.
It uses SQLAlchemy to prevent SQL injection.
"""

# Database credentials
DB_USERNAME = 'username'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'database_name'

# Create a database engine
engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def query_database(query, params=None):
    """
    Execute a query on the database with parameterized statements to prevent SQL injection.
    :param query: The SQL query as a string
    :param params: A dictionary of parameters for the query
    :return: The result of the query
    """
    with engine.connect() as conn:
        try:
            if params:
                result = conn.execute(text(query), **params)
            else:
                result = conn.execute(text(query))
            return result.fetchall()
        except SQLAlchemyError as e:
            st.error(f"An error occurred: {e}")
            return None

# Streamlit layout
st.title('SQL Injection Protection Demo')

# Add a text box for the user to input a query
query = st.text_input('Enter your SQL query', 'SELECT * FROM users;')

# Execute the query button
if st.button('Execute Query'):
    results = query_database(query)
    if results is not None:
        st.write(results)
    else:
        st.write('No results were returned.')
