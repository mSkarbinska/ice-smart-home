import SmartHome
from client import Client
import datetime


class MonitoringCameraClient(Client):
    def get_stub(self, base):
        return SmartHome.MonitoringCameraPrx.checkedCast(base)


@MonitoringCameraClient.command
def save_recording(self):
    from_date = input("From date [format: %d/%m/%Y %H:%M]: ")
    from_date_time = get_datetime_from_string(from_date)

    to_date = input("To date [format: %d/%m/%Y %H:%M]: ")
    to_date_time = get_datetime_from_string(to_date)

    from_date_parsed = parse_date(from_date_time)
    from_date_obj = create_datetime_obj(from_date_parsed)
    to_date_parsed = parse_date(to_date_time)
    tp_date_obj = create_datetime_obj(to_date_parsed)

    try:
        self._stub.saveRecording(from_date_obj, tp_date_obj)
    except SmartHome.InvalidDateException | SmartHome.IvalidTimeBlockAException:
        print("Invalid date or time block")


@MonitoringCameraClient.command
def get_last_recording(self):
    from_date = self._stub.getLastRecording().fromDate
    to_date = self._stub.getLastRecording().toDate

    print("Recording from date: " + stringify_date(from_date) + " to date: " + stringify_date(to_date))


def get_datetime_from_string(date_string):
    try:
        return datetime.datetime.strptime(date_string, '%d/%m/%Y %H:%M')
    except ValueError:
        print("Invalid date format. Please enter date in the format 'dd/mm/yyyy hh:mm'.")


def parse_date(date):
    # Extract day, month, year, hour, and minute as integers
    day = date.day
    month = date.month
    year = date.year
    hour = date.hour
    minute = date.minute

    return [day, month, year, hour, minute]


def create_datetime_obj(date):
    date_time = SmartHome.DateTime()
    date_time.day = date[0]
    date_time.month = date[1]
    date_time.year = date[2]
    date_time.hour = date[3]
    date_time.minute = date[4]

    return date_time


def stringify_date(date):
    return f"{date.day}/{date.month}/{date.year} {date.hour}:{date.minute}"
