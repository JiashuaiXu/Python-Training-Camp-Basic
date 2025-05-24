"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""
def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作

    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")

    返回:
    - 集合操作的结果
    """
    if operation == "union":
        # 并集：包含在 set1 或 set2 中的所有学生
        return set1.union(set2)
    
    elif operation == "intersection":
        # 交集：同时出现在 set1 和 set2 中的学生
        return set1.intersection(set2)
    
    elif operation == "difference":
        # 差集：出现在 set1 但不在 set2 中的学生
        return set1.difference(set2)
    
    else:
        # 不支持的操作
        raise ValueError("Unsupported operation: " + operation)
