"""
练习: 使用math模块

描述：
使用math模块计算平方根。

请补全下面的函数，使用math模块的sqrt函数计算平方根。
"""
import math

def calculate_square_root(number):
    """
    计算数字的平方根

    参数:
    - number: 非负数

    返回:
    - 数字的平方根
    """
    if number < 0:
        raise ValueError("不能计算负数的平方根")
    
    return math.sqrt(number)
