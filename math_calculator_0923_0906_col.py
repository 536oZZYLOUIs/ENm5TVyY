# 代码生成时间: 2025-09-23 09:06:43
import streamlit as st

# 定义数学计算工具集应用
class MathCalculator:
    def __init__(self):
        """初始化数学计算工具集应用"""
        self.operators = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }

    def add(self, a, b):
        """加法运算"""
        return a + b

    def subtract(self, a, b):
        """减法运算"""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a - b

    def multiply(self, a, b):
        """乘法运算"""
        return a * b

    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def calculate(self, operator, a, b):
        """根据操作符执行相应的数学运算"""
        if operator not in self.operators:
            raise ValueError(f"Unsupported operator: {operator}.")
        return self.operators[operator](a, b)

# 初始化数学计算工具集应用
calculator = MathCalculator()

# Streamlit界面布局
def main():
    st.title('Math Calculator')

    # 输入数值
    num1 = st.number_input('Enter first number', min_value=0.0, max_value=100.0)
    num2 = st.number_input('Enter second number', min_value=0.0, max_value=100.0)

    # 选择运算符
    operator = st.selectbox('Choose an operation', list(calculator.operators.keys()))

    # 执行计算并显示结果
    try:
        result = calculator.calculate(operator, num1, num2)
        st.write(f'The result of {operator} is {result}')
    except ValueError as e:
        st.error(f'Error: {e}')

# 运行主函数
if __name__ == '__main__':
    main()