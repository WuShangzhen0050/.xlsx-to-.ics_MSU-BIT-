# .xlsx-to-.ics_MSU-BIT-2025

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.en.md)
[![zh-cn](https://img.shields.io/badge/lang-zh--cn-red.svg)](https://github.com/WuShangzhen0050/.xlsx-to-.ics_MSU-BIT-/blob/main/README.md)



## Project Introduction
The SMBU official website (https://ehall.smbu.edu.cn) only provides course schedules in .xlsx (Excel) format, making it inconvenient to import the schedule into calendar applications. To address this issue, I have created a Python-based project.

-**Automated Conversion**: This project allows you to convert an Excel course schedule into an iCalendar (.ics) file.
-**High Compatibility**: The generated .ics file can be imported into Outlook, Google Calendar, or other calendar applications.
-**Customization Support**: Users can modify conf_classTime.json to adjust class time slots.

However, the author has only tested it in Outlook. The author is a Chinese student majoring in undergraduate mathematics and applied mathematics (edited in February 2025). The course schedules for non-undergraduate and other majors may be different. Relevant personnel can operate or refer to them according to the specific situation.

At the time of editing, the author has checked the situation of adjusting the language to Русский язык and English on the school's official website and then downloading the Excel course schedule. The result is that the downloaded course schedule is in Chinese, so there is no solution for these two languages here.

The author is not responsible for any errors in the generated iCalendar file.

This project serves as a basic implementation, and feedback, suggestions, and improvements are welcome. Some features from the two reference projects below are not yet implemented in this project. Interested users and developers can explore and contribute.

This project refers to the following GitHub open-source projects:
- [wenchenwan/ClasstableToIcalforNUAA](https://github.com/wenchenwan/ClasstableToIcalforNUAA)
- [miaotony/NUAA_ClassSchedule](https://github.com/miaotony/NUAA_ClassSchedule)

Thanks to the contributors of the above projects!

---

## Usage
Before you begin, please read this README carefully! Consider whether this project needs to be deployed in a specific container or environment. The reference projects above provide some deployment options, but this project does not require deployment on Vercel, virtual machines, or other complex containers.

1. **Setup**: Make sure Python 3 is installed.
2. **Install Dependencies**: Install the required packages with the following command:
    ```
    pip install pandas icalendar
    ```
   (Conda users can also install them via Conda.)
3. **Prepare the Excel Course Schedule**
   Ensure that your Excel spreadsheet includes the following columns:
   - `Course name`/`课程名称`
   - `Weeks of class`/`上课周次`
   - `Class time`/`上课时间`
   - `Classroom`/`教室`
   - `Lecturer`/`主讲教师`
   - `Number of students`/`选课人数`
   
   These column names are simply translated from Chinese.

   The old version of the course schedule (2024) follows the format of the included sample file `我的课表.xlsx` ("MySchedule.xlsx"). The old version of this project only supports this format, meaning little to no adjustment is needed.

   However, the new course schedule (2025) follows a more standard format, which requires some adjustments. These adjustments can only be made by me (although I am graduating soon) or by other contributors via issues or push requests upon my approval.

   This update specifically addresses the format change in the course schedule.

   Please refer to the sample file `adjusted202502.xlsx`.
4. **Check the Official Course Schedule Rules Immediately**:\
   News: https://ehall--ps-smbu-edu-cn-s.webvpn.smbu.edu.cn:8118/psfw/sys/tzggapp/*default/index.do?ggdm=d12ecd3a-8096-4dde-926a-ab579a6ad44f#/ggll
   **Pay attention!**: What date is the first day of the semester?
5. **Check Course Details (Step of the Old Version)**: Verify the detailed course information:
    - `Course Code`/`课程号`
    - `Course Name`/`课程名`
    - `Section`/`课序号`
    - `Offering Department`/`开课单位`
    - `Credits`/`学分`
    - `...`

   (If any) 

   These column names are simply translated from Chinese.

   Many of these details are missing in the new course schedule, but that does not matter. My script only processes the most essential columns. Information like "Number of Students" is not included. If you need additional features, feel free to modify the code.
6. **Double-Check Important Information:**:
    - `Weeks of class`/`上课周次`
    - `Start class`/`开始节次`
    - `End class`/`结束节次`
    - `...`
7. **Run the script**:
    ```
    python main.py your_timetable.xlsx --config_file conf_classTime.json --output_file your_timetable.ics --semester_start_date YYYY-MM-DD
    ```
    (This is just a template—adjust the parameters according to your needs.)
8. **Export the File**: The generated ***.ics file (with the name you specified in Step 7) will be saved in the project directory.

## Configuration

   Modify conf_classTime.json to customize class time slots.
