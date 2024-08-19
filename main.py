import json
import argparse
from excel_reader import read_class_info
from ical_generator import generate_ics
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Convert Excel class schedule to iCalendar (.ics) file.")
    parser.add_argument('class_info_file', type=str, help="Path to the Excel file containing the class schedule.")
    parser.add_argument('--config_file', type=str, default='conf_classTime.json',
                        help="Path to the JSON configuration file.")
    parser.add_argument('--output_file', type=str, default='class_schedule.ics', help="Output .ics file name.")
    parser.add_argument('--semester_start_date', type=str, default='2024-09-02',
                        help="Semester start date (YYYY-MM-DD).")

    args = parser.parse_args()

    class_info_file = args.class_info_file
    config_file = args.config_file
    output_file = args.output_file
    semester_start_date = datetime.strptime(args.semester_start_date, '%Y-%m-%d')

    class_info = read_class_info(class_info_file)

    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    generate_ics(class_info, config, output_file, semester_start_date)
    print(f"ICS file generated: {output_file}")


if __name__ == "__main__":
    main()
