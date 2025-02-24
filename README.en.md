# .xlsx-to-.ics_MSU-BIT-2025

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/imBlanker/.xlsx-to-.ics_MSU-BIT-2025/blob/master/README.en.md)
[![pt-br](https://img.shields.io/badge/lang-zh--cn-red.svg)](https://github.com/imBlanker/.xlsx-to-.ics_MSU-BIT-2025/blob/master/README.md)



## Project Introduction
The timetable provided in our SMBU official website (https://ehall.smbu.edu.cn) can only be exported in .xlsx (Excel) format. It is very troublesome for us to import the timetable into the calendar software. Now I create a project in Python to alleviate this problem.

**Supports**: Converts Excel schedules into .ics (iCalendar) files.
-**Compatibility**: The generated .ics file can be imported into Outlook, Google Calendar, Apple Calendar, etc.
-**Customizable**: Modify conf_classTime.json to adjust time slots.
But the author has only tested it in Outlook.
The author is not responsible for any errors in the generated iCalendar file.

This project refers to the following GitHub open source projects:
- [wenchenwan/ClasstableToIcalforNUAA](https://github.com/wenchenwan/ClasstableToIcalforNUAA)
- [miaotony/NUAA_ClassSchedule](https://github.com/miaotony/NUAA_ClassSchedule)

Thanks to the contributors of the above projects!

---

## Usage
1. **Setup**: Make sure Python 3 is installed.
2. **Install dependencies**: Install the required packages with the following command:
    ```
    pip install pandas icalendar
    ```
3. **Prepare Excel timetable**
   Make sure your Excel file meets the following format:
   Course name
   Weeks of class
   Class time
   Classroom
   Lecturer
   Number of students

   For example, please refer to classInfo.xlsx.
4. **Check the official rules of the timetable immediately**:\
   News: https://ehall--ps-smbu-edu-cn-s.webvpn.smbu.edu.cn:8118/psfw/sys/tzggapp/*default/index.do?ggdm=d12ecd3a-8096-4dde-926a-ab579a6ad44f#/ggll
   **Note**: What date is the first day of the semester?
5. **View details**: View detailed information of the timetable:
    - `Course Code`/`课程号`
    - `Course Name`/`课程名`
    - `Section`/`课序号`
    - `开课单位`
    - `学分`
    - `...`
   (if any)
6. **Check the time slots again**: Check the time slots:
    - `Weeks of class`
    - `Start class`
    - `End class`
    - `...`
7. **Run the script**:
    ```
    python main.py your_timetable.xlsx --config_file conf_classTime.json --output_file your_timetable.ics --semester_start_date YYYY-MM-DD
    ```
    This is a pattern of the command. Please replace the parameters with your own.
8. **Result**: The generated `class_schedule.ics` file will be in the project directory.

## Configuration

   conf_classTime.json
