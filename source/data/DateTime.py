
import datetime

def getCurrentDayDate():
    current_date = datetime.datetime.utcnow()
    output_date = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return output_date


def getNextDayDate():
    current_date = datetime.datetime.utcnow()
    current_date += datetime.timedelta(days=1)
    output_date = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return output_date

# datatime class -> %Y-%m-%dT%H:%M:%SZ
def dateDateString(wrongDate):
    return datetime.datetime.strftime(wrongDate, "%Y-%m-%dT%H:%M:%SZ")

# %Y-%m-%dT%H:%M:%SZ -> datatime class
def dateStringDate(wrongDate):
    return datetime.datetime.strptime(wrongDate, "%Y-%m-%dT%H:%M:%SZ")

def getHoursFrom(date, hours):
    curr_date = dateStringDate(date)
    curr_date = curr_date.replace(minute=0, second=0)
    curr_date += datetime.timedelta(hours=hours)
    return datetime.datetime.strftime(curr_date, "%Y-%m-%dT%H:%M:%SZ")

def getTimeString(wrongDate):
    date = dateStringDate(wrongDate)
    return datetime.datetime.strftime(date, "%H:%M")

# eof