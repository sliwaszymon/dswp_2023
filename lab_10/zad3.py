import datetime
from zoneinfo import ZoneInfo


while True:
    time = input("Podaj czas w formacie HH:MM:SS: ")
    time = datetime.datetime.strptime(time, "%H:%M:%S").time()
    dt = datetime.datetime.combine(datetime.datetime.today().date(), time)

    print(f"Tokyo: {dt.astimezone(tz=ZoneInfo('Asia/Tokyo')).strftime('%H:%M:%S')}")
    print(f"Londyn: {dt.astimezone(tz=ZoneInfo('Europe/London')).strftime('%H:%M:%S')}")
    print(f"Sydney: {dt.astimezone(tz=ZoneInfo('Australia/Sydney')).strftime('%H:%M:%S')}")
    print(f"Waszyngton: {dt.astimezone(tz=ZoneInfo('Etc/GMT+4')).strftime('%H:%M:%S')}")
