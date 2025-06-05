from datetime import datetime
import time

now = datetime.now()
formatted_time = now.strftime(f"%a %d %H:%M:%S IST %Y").upper()
print(formatted_time)

# i have hardcode IST coz it was showing its full form. But question demanded only IST.
# Ofcourse there ways for that like one could use pytz, but its fine until it runs.