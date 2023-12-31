import ntplib
import datetime
from ctypes             import Structure, windll, pointer
from ctypes.wintypes    import WORD
 
class SYSTEMTIME(Structure):
  _fields_ = [
      ( 'wYear',            WORD ),
      ( 'wMonth',           WORD ),
      ( 'wDayOfWeek',       WORD ),
      ( 'wDay',             WORD ),
      ( 'wHour',            WORD ),
      ( 'wMinute',          WORD ),
      ( 'wSecond',          WORD ),
      ( 'wMilliseconds',    WORD ),
    ]
SetLocalTime = windll.kernel32.SetLocalTime
 
c = ntplib.NTPClient()
response = c.request('ntp.nict.jp', version=3)
dt_ = datetime.datetime.fromtimestamp( response.tx_time )
print( 'Got time as', dt_.strftime( '%d-%m-%Y %H:%M:%S'), 'from NTP Server' )
 
dt_tuple = dt_.timetuple()
st = SYSTEMTIME()
st.wYear            = dt_tuple.tm_year
st.wMonth           = dt_tuple.tm_mon
st.wDayOfWeek       = ( dt_tuple.tm_wday + 1 ) % 7
st.wDay             = dt_tuple.tm_mday
st.wHour            = dt_tuple.tm_hour
st.wMinute          = dt_tuple.tm_min
st.wSecond          = dt_tuple.tm_sec
st.wMilliseconds    = 0
 
ret = SetLocalTime( pointer( st ) )
print (ret)
if ret == 0:
    print( 'Setting failed. Try as administrator.' )
else:
    print( 'Successfully set the systemtime as above.' )
