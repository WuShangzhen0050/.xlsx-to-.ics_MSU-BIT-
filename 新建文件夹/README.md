

# Excel to iCalendar Converter

## Overview

This project is designed to convert a class schedule from an Excel file into an iCalendar (`.ics`) file. The generated calendar can be easily imported into applications like Outlook, Google Calendar, or any other calendar app that supports the `.ics` format.

### Why Convert Excel Schedules to iCalendar?

- **Convenience**: Easily manage and customize your class schedule within your preferred calendar application.
- **Reminders**: Set reminders to avoid missing classes.
- **Cross-Platform Syncing**: Sync your class schedule across devices using apps like Google Calendar or Outlook.
- **Efficient Management**: Handle schedule changes and adjustments efficiently.

## Features

- Converts an Excel-based class schedule to an `.ics` calendar file.
- Supports custom configurations for class timings.
- Automatically handles multi-week schedules and complex class timings.

## Project Structure

- **`excel_reader.py`**: Handles reading and processing of the Excel file containing the class schedule.
- **`conf_classTime.json`**: A JSON configuration file mapping class periods to their respective start and end times.
- **`ical_generator.py`**: Generates the `.ics` iCalendar file using the data extracted from the Excel sheet.
- **`main.py`**: The main script that orchestrates the entire process of reading the Excel file and generating the `.ics` file.
- **`LICENSE`**: The licensing terms under which this project is distributed.

## Setup and Usage

### Prerequisites

- Python 3.x installed on your system.
- Necessary Python libraries:
  - `pandas`
  - `icalendar`
  - `pytz`

You can install the required libraries using pip:

```bash
pip install pandas icalendar pytz
```

### Steps to Use

1. **Clone the Repository**: Download or clone this repository to your local machine.

2. **Prepare Your Excel File**: Ensure your class schedule is formatted similarly to the sample provided in `classInfo.xlsx`. The relevant columns should include:
   - `上课周次` (Weeks)
   - `上课星期` (Day of the Week)
   - `开始节次` (Start Period)
   - `结束节次` (End Period)
   - `上课教师` (Instructor)
   - `教室名称` (Classroom)
   - `课程名` (Course Name)

3. **Edit the Configuration File**: Modify `conf_classTime.json` if your class times differ from the default settings provided.

4. **Run the Script**:
   - Place your Excel file in the project directory.
   - Edit the `main.py` script to point to your Excel file path.
   - Run the script:
   ```bash
   python main.py
   ```

5. **Import the Calendar File**:
   - The script will generate an `我的课表.ics` file in the project directory.
   - Import this file into your calendar application of choice.

### Example

To run the conversion process, use the following command:

```bash
python main.py
```

### License

This project is licensed under the [Your Chosen License]. See the `LICENSE` file for more details.

## Contributions

Contributions to improve the project are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## Acknowledgments

This project is inspired by the [ClasstableToIcalforNUAA](https://github.com/Xm798/ClasstableToIcalforNUAA) project. Special thanks to the original authors for their contributions.

