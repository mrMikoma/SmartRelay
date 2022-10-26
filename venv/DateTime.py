
import datetime

def getCurrentDayDate():
    current_date = datetime.datetime.utcnow()
    output_date = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return(output_date)


def getNextDayDate():
    current_date = datetime.datetime.utcnow()
    current_date += datetime.timedelta(days=1)
    output_date = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return(output_date)

# eof