from datetime import datetime

today = datetime.now()
day = today.day
month = today.month
year = today.year
print ("hoje ", today, " dia ", day, "/", month, "/", year)
print ("hora ", today.hour, "| min ", today.minute, "| seg ", today.second)