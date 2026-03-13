# Datetime module in python
from dateutil import relativedelta



from datetime import datetime, timedelta
import zoneinfo

now_date_time = datetime.now()

# Get the timezone object for Asia Kathmandu
ak_tz = zoneinfo.ZoneInfo("Asia/Kathmandu")
ak_dt = now_date_time.astimezone(ak_tz)

# ny_tz = zoneinfo.ZoneInfo("America/New_York")
# pb_tz = zoneinfo.ZoneInfo("Europe/Paris")

# ny_dt = now_date_time.astimezone(ny_tz)
# pb_dt = now_date_time.astimezone(pb_tz)


# ak_str_dt = now_date_time.strftime("%H:%M:%S %m/%d/%Y")

ak_p_dt = datetime.strptime("07:45:43 03/10/2026", "%H:%M:%S %m/%d/%Y")
ak_p_dt = ak_p_dt.astimezone(ak_tz) - relativedelta.relativedelta(months = 1)


# print(f"Current Device Date Time Is::>> {now_date_time}\n")
# print(f"US New York Date Time Is::>> {ny_dt}\n")
# print(f"Paris Berlin Date Time Is::>> {pb_dt}\n")
# 
# print(f"Asia Kathmandu Date Time Is::>> {ak_str_dt}\n")
print(f"Asia Kathmandu Date Time Is::>> {ak_p_dt}\n")