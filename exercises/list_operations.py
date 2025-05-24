"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""
def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作

    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数

    返回:
    - 操作后的学生列表
    """
    # 添加学生：需要提供要添加的学生姓名
    if operation == "add":
        student_name = args[0]
        students.append(student_name)
    
    # 删除学生：需要提供要删除的学生姓名
    elif operation == "remove":
        student_name = args[0]
        if student_name in students:
            students.remove(student_name)
    
    # 更新学生：需要提供索引和新的学生姓名
    elif operation == "update":
        index, new_name = args
        if 0 <= index < len(students):
            students[index] = new_name
    
    # 如果操作不支持，可以抛出异常或忽略
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
    return students
