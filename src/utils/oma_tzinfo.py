# coding: iso-8859-15
import datetime

class EE_tzinfo(datetime.tzinfo):
    
    def __init__(self): pass
    
    """tzinfo Suomen aikavyöhykkeelle"""
    def utcoffset(self, dt):
        return datetime.timedelta(hours=+2) + self.dst(dt)
    
    def _FirstSunday(self, dt):
        """Ensimmäinen sunnuntai dt:nä tai sen jälkeen"""
        return dt + datetime.timedelta(days=(6 - dt.weekday()))
    
    def dst(self, dt):
        # Maaliskuun viimeinen sunnuntai 01:00 UTC
        dst_start = self._FirstSunday(datetime.datetime(dt.year, 3, 22, 1))
        # Lokakuun viimeinen sunnuntai 01:00 UTC
        dst_end = self._FirstSunday(datetime.datetime(dt.year, 10, 22, 1))
        
        if dst_start <= dt.replace(tzinfo=None) < dst_end:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(hours=0)
        
    def tzname(self, dt):
        if self.dst(dt) == datetime.timedelta(hours=0):
            return "EEST"
        else:
            return "EET"
        
class UTC_tzinfo(datetime.tzinfo):
    
    def __init__(self): pass
    
    def utcoffset(self, dt):
        return datetime.timedelta(hours=0)
    
    def dst(self, dt):
        return datetime.timedelta(hours=0)
        
    def tzname(self, dt):
        return "UTC"