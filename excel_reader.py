import pandas as pd


def read_class_info(file_path):
    df = pd.read_excel(file_path)

    # Filter and rename columns as required
    class_info = df[['上课周次', '上课星期', '开始节次', '结束节次', '上课教师', '教室名称', '课程名']]

    return class_info
