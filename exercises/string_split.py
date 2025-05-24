"""
练习: 字符串分割

描述：
使用split()方法分割字符串，提取关键信息。

请补全下面的函数，使用split()方法分割字符串并提取所需信息。
"""
def extract_keywords(text):
    """
    从文本中提取关键词

    参数:
    - text: 包含关键词的文本字符串，关键词之间用空格分隔

    返回:
    - 提取出的关键词列表
    """
    return text.split()

def parse_csv_line(csv_line):
    """
    解析CSV格式的一行数据

    参数:
    - csv_line: CSV格式的字符串，字段之间用逗号分隔

    返回:
    - 包含各字段的列表
    """
    return csv_line.split(',')

def extract_name_and_domain(email):
    """
    从电子邮件地址中提取用户名和域名

    参数:
    - email: 电子邮件地址字符串，格式为username@domain.com

    返回:
    - 包含用户名和域名的元组 (username, domain)
    """
    parts = email.split('@')
    if len(parts) == 2:
        return (parts[0], parts[1])
    else:
        raise ValueError("无效的电子邮件地址")
