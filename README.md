<<<<<<< HEAD
# .xlsx-to-.ics_MSU-BIT-
我们smbu官网（https://ehall.smbu.edu.cn）里面提供的课表只能以.xlsx(Excel)格式导出，我们要把课表导入日历软件的话就很麻烦了。现今我用Python创建一个项目，缓解这个问题。
=======
# Excel to iCalendar Converter

This project allows you to convert an Excel class schedule into an iCalendar (.ics) file that can be imported into Outlook, Google Calendar, or other calendar apps.
But the author has only tested it in Outlook.
The author is not responsible for any errors in the generated iCalendar file.

## How to Use

1. **Setup**: Make sure you have Python 3 installed.
2. **Install dependencies**: Install the required packages using:
    ```
    pip install pandas icalendar
    ```
3. **Prepare the Excel file**
4. **Check the offical rules of the class schedule now**:\
   News: https://ehall--ps-smbu-edu-cn-s.webvpn.smbu.edu.cn:8118/psfw/sys/tzggapp/*default/index.do?ggdm=d12ecd3a-8096-4dde-926a-ab579a6ad44f#/ggll
   **Note**: What date is the first day of the semester?
4. **Check the details**: Check the details of the class schedule in:
    - `Course Code`/`课程号`
    - `Course Name`/`课程名`
    - `Section`/`课序号`
    - `开课单位`
    - `学分`
    - `...`
4. **Check the time slots again**: Check the time slots in:
    - `上课周次`
    - `开始节次`
    - `结束节次`
    - `...`
3. **Run the Script**:
    ```
    python main.py path/to/your/我的课表.xlsx --config_file path/to/conf_classTime.json --output_file path/to/我的课表.ics --semester_start_date YYYY-MM-DD
    ```
5. **Result**: The generated `class_schedule.ics` file will be in the project directory.

## Configuration

Modify `conf_classTime.json` to customize the time slots.


>>>>>>> 676e5fc (Initial commit)
