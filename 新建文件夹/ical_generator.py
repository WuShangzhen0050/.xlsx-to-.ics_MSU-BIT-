from icalendar import Calendar, Event
from datetime import datetime, timedelta
import json
import pytz


def generate_ical(df, semester_start_date, json_file_path, output_file):
    with open(json_file_path, 'r') as f:
        time_mapping = json.load(f)

    cal = Calendar()
    weekday_mapping = {"星期一": 0, "星期二": 1, "星期三": 2, "星期四": 3, "星期五": 4, "星期六": 5, "星期日": 6}

    for _, row in df.iterrows():
        start_time = time_mapping[row["开始节次"].split()[0]]['start']
        end_time = time_mapping[row["结束节次"].split()[0]]['end']

        for week_range in row["上课周次"].split(","):
            weeks = week_range.split("-")
            start_week = int(weeks[0])
            end_week = int(weeks[-1]) if len(weeks) > 1 else start_week

            for week in range(start_week, end_week + 1):
                event = Event()
                event.add("summary", row["课程名"])
                event.add("location", row["教室名称"])
                event.add("description", row["上课教师"])

                event_start = semester_start_date + timedelta(days=weekday_mapping[row["上课星期"]], weeks=week - 1)
                event_end = event_start
                start_datetime = datetime.combine(event_start.date(), datetime.strptime(start_time, "%H:%M").time())
                end_datetime = datetime.combine(event_end.date(), datetime.strptime(end_time, "%H:%M").time())

                event.add("dtstart", start_datetime)
                event.add("dtend", end_datetime)
                event.add("dtstamp", datetime.now(pytz.utc))

                cal.add_component(event)

    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())

