from excel_reader import read_excel
from ical_generator import generate_ical
from datetime import datetime

if __name__ == "__main__":
    # Define the input and output paths
    excel_file_path = '你的课表文件路径.xlsx'
    json_file_path = 'conf_classTime.json'
    output_ical_path = '我的课表.ics'

    # Define the semester start date
    semester_start_date = datetime(2024, 2, 26)

    # Read the Excel file
    df = read_excel(excel_file_path)

    # Generate the iCalendar file
    generate_ical(df, semester_start_date, json_file_path, output_ical_path)

    print(f"Calendar file generated successfully: {output_ical_path}")
