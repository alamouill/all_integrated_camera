from gps import *
session = gps()

def init_gps():
    global session
    session= gps ()
    session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)

def gps_current_value ():
    report = session.next()
    if report.keys()[0] == 'epx' :
        lat = float(report['lat'])
        lon = float(report['lon'])
        print("lat=%f\tlon=%f\ttime=%s" % (lat, lon, report['time']))
        return str(lat)+str(lon)
    else :
        print("gps not fixed")
        return ("gps not fixed")

if __name__ == '__main__':
    init_gps()
    gps_current_value ()
