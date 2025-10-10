# 代码生成时间: 2025-10-11 02:02:18
import streamlit as st

# 定义一个函数来显示首页的内容

def main_page():
    st.title('在线学习平台')
    st.write('欢迎来到在线学习平台！')
    with st.expander('课程列表'):
        courses = ['数学', '物理', '化学', '生物']
        st.write(courses)

    # 导航栏
    with st.sidebar:
        st.header('导航')
        choice = st.selectbox('选择操作:', ('首页', '课程详情', '个人中心'))
        if choice == '课程详情':
            course_details()
        elif choice == '个人中心':
            personal_center()

# 定义一个函数来显示课程详情页面

def course_details():
    st.title('课程详情')
    course_name = st.text_input('请输入课程名称：')
    if course_name:
        try:
            # 假设有一个获取课程信息的函数
            course_info = get_course_info(course_name)
            st.write(course_info)
        except Exception as e:
            st.error('无法获取课程信息：' + str(e))

# 定义一个函数来获取课程信息

def get_course_info(course_name):
    # 这里只是一个示例，实际应用中需要根据数据库或其他数据源来获取信息
    return f'{course_name}课程详细介绍'

# 定义一个函数来显示个人中心页面

def personal_center():
    st.title('个人中心')
    st.write('这里可以展示用户的个人信息和学习进度等。')

# 运行主页面
if __name__ == '__main__':
    main_page()