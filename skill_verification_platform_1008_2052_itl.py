# 代码生成时间: 2025-10-08 20:52:43
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from typing import List, Dict

"""
技能认证平台 Streamlit 应用。
"""

# 模拟的认证信息数据库
CERTIFICATIONS = {
    "John": ["Python", "Data Analysis"],
    "Alice": ["Machine Learning", "Deep Learning"],
    "Bob": ["Web Development"]
}

# 错误消息
ERROR_MSG = "

认证信息加载失败，请稍后再试。"""

# 主函数，用于初始化 Streamlit 应用
def main():
    st.title('技能认证平台')

    # 显示认证信息表格
    show_certifications_table()

    # 显示用户输入和认证结果
    show_user_input()

# 显示认证信息表格
def show_certifications_table():
    # 构建表格数据
    certifications_data = {
        "Name": list(CERTIFICATIONS.keys()),
        "Certifications": [str(certifications) for certifications in CERTIFICATIONS.values()]
    }

    # 将数据转换为 DataFrame
    df = pd.DataFrame(certifications_data)

    # 配置表格选项
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_grid_options(
        pagination=True,
        paginationPageSize=5,
        showToolPanel=True
    )

    # 显示表格
    AgGrid(df, grid_options=gb.build())

# 显示用户输入和认证结果
def show_user_input():
    # 用户输入
    user_name = st.text_input('输入用户名:', '')

    # 显示认证信息
    if st.button('验证技能'):
        try:
            # 获取用户认证信息
            user_certifications = CERTIFICATIONS.get(user_name, [])
            if user_certifications:
                st.write(f"{user_name} 的技能认证包括: {user_certifications}")
            else:
                st.error(f"{user_name} 的认证信息不存在。")
        except Exception as e:
            st.error(ERROR_MSG)
            # 日志记录异常（可根据需要添加日志记录）
            # logging.error(f"{ERROR_MSG} - {str(e)}")

# 运行主函数
if __name__ == '__main__':
    main()