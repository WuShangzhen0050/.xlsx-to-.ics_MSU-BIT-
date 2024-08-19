from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz


def time_to_minutes(time_str):
    """Converts HH:MM time format to minutes since midnight."""
    h, m = map(int, time_str.split(':'))
    return h * 60 + m


def minutes_to_time(minutes):
    """Converts minutes since midnight to HH:MM time format."""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02}:{m:02}"


def generate_ics(class_info, config, output_file, semester_start_date):
    cal = Calendar()

    weekday_mapping = {
        "星期一": "MO",
        "星期二": "TU",
        "星期三": "WE",
        "星期四": "TH",
        "星期五": "FR",
        "星期六": "SA",
        "星期日": "SU",
    }

    for _, row in class_info.iterrows():
        start_key = row["开始节次"].split()[0]
        end_key = row["结束节次"].split()[0]

        # If numeric key is greater than 14, skip the event
        if start_key.isdigit() and int(start_key) > 14 or end_key.isdigit() and int(end_key) > 14:
            continue

        if start_key not in config["time_slots"]:
            raise KeyError(f"Time slot key '{start_key}' not found in configuration.")

        # Handle case where end_key is "14" to create the union of time slots
        if end_key == "14":
            start_time_minutes = min(time_to_minutes(config["time_slots"][start_key]["start"]),
                                     time_to_minutes(config["time_slots"][end_key]["start"]))
            end_time_minutes = max(time_to_minutes(config["time_slots"][start_key]["end"]),
                                   time_to_minutes(config["time_slots"][end_key]["end"]))
        else:
            if end_key not in config["time_slots"]:
                raise KeyError(f"Time slot key '{end_key}' not found in configuration.")

            # Create the union of the time intervals
            start_time_minutes = min(time_to_minutes(config["time_slots"][start_key]["start"]),
                                     time_to_minutes(config["time_slots"][end_key]["start"]))
            end_time_minutes = max(time_to_minutes(config["time_slots"][start_key]["end"]),
                                   time_to_minutes(config["time_slots"][end_key]["end"]))

        start_time = datetime.strptime(minutes_to_time(start_time_minutes), "%H:%M").time()
        end_time = datetime.strptime(minutes_to_time(end_time_minutes), "%H:%M").time()

        # Process week ranges and create events accordingly
        week_ranges = row["上课周次"].split(",")
        for week_range in week_ranges:
            week_range = week_range.strip("周")

            if '-' in week_range:
                start_week, end_week = map(int, week_range.split("-"))
            else:
                start_week = end_week = int(week_range)

            event_start_date = semester_start_date + timedelta(weeks=start_week - 1,
                                                               days=list(weekday_mapping.keys()).index(row["上课星期"]))
            event_end_date = semester_start_date + timedelta(weeks=end_week - 1,
                                                             days=list(weekday_mapping.keys()).index(row["上课星期"]))

            event = Event()
            event.add("summary", row["课程名"])
            event.add("location", row["教室名称"])
            event.add("description", row["上课教师"])
            event.add("dtstart", datetime.combine(event_start_date, start_time))
            event.add("dtend", datetime.combine(event_start_date, end_time))
            event.add("dtstamp", datetime.now(pytz.utc))

            # Add recurrence rule for the specific week range
            until_date = datetime.combine(event_end_date, end_time)
            rrule = {
                "FREQ": "WEEKLY",
                "UNTIL": until_date,
                "BYDAY": weekday_mapping[row["上课星期"]],
                "INTERVAL": 1
            }
            event.add("rrule", rrule)

            cal.add_component(event)

    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())
