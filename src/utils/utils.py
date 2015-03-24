# -*- coding: iso-8859-15 -*-
import datetime
import math


from oma_tzinfo import UTC_tzinfo, EE_tzinfo

def time2EE(time):
    time = time.replace(tzinfo=UTC_tzinfo())
    return time.astimezone(EE_tzinfo())

def secondsFrom70s(now):
    return (now-datetime.datetime(1970,1,1)).total_seconds()

def getDelta(time):
    return int( math.floor( ( time2EE(datetime.datetime.now()) - time ).total_seconds() ) )

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False