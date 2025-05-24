"""
练习: 函数定义与参数

描述：
创建一个计算面积的函数。
如果提供两个参数，计算长方形面积；
如果只提供一个参数，计算正方形面积。

请补全下面的函数，实现计算面积的功能。
"""
def calculate_area(length, width=None):
    """
    计算面积

    参数:
    - length: 长度
    - width: 宽度(可选)，如果不提供则计算正方形面积

    返回:
    - 计算得到的面积
    """
    if width is None:
        # 只提供一个参数，计算正方形面积
        return length * length
    else:
        # 提供两个参数，计算长方形面积
        return length * width
