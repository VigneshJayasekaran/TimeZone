import pytz
from datetime import datetime
def get_time_for_location(location):
    try:
        timezone = pytz.timezone(location)
        utc_now = datetime.now(pytz.utc)
        local_time = utc_now.astimezone(timezone)
        print(f"Current time in {location}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except pytz.UnknownTimeZoneError:
        print(f"Error: '{location}' is not a valid timezone.")
if __name__ == "__main__":
    location = input("Enter a timezone (e.g., 'America/New_York' or 'Europe/London'): ")
    get_time_for_location(location)
