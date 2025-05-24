def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作

    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数

    返回:
    - 根据操作返回不同结果
    """
    # 添加操作：需要提供姓名和成绩
    if operation == "add":
        name, score = args
        students_dict[name] = score
        return students_dict
    
    # 删除操作：需要提供姓名
    elif operation == "remove":
        name = args[0]
        if name in students_dict:
            del students_dict[name]
        return students_dict
    
    # 更新操作：需要提供姓名和新成绩
    elif operation == "update":
        name, new_score = args
        if name in students_dict:
            students_dict[name] = new_score
        return students_dict
    
    # 查询操作：需要提供姓名
    elif operation == "get":
        name = args[0]
        return students_dict.get(name, None)
    
    # 不支持的操作
    else:
        raise ValueError("Unsupported operation: {}".format(operation))
