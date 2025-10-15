# 代码生成时间: 2025-10-16 02:16:17
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# 配置数据库连接信息
DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname'

# 创建数据库连接引擎
def create_db_engine(uri):
    return create_engine(uri)

# 执行SQL查询并返回结果
def execute_query(engine, query):
    with engine.connect() as connection:
        result = pd.read_sql_query(query, connection)
    return result

# 主函数，用于Streamlit应用
def main():
    st.title('Database Performance Tuning App')

    # 用户输入数据库性能调优相关的参数
    query = st.text_area('Enter SQL Query', height=200)
    if st.button('Execute Query'):
        try:
            # 创建数据库连接
            db_engine = create_db_engine(DATABASE_URI)
            # 执行查询
            df = execute_query(db_engine, query)
            # 展示结果
            st.write(df)
        except Exception as e:
            # 错误处理
            st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()