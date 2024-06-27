
import time

flight_time = input("Enter your flight time (in hours and minutes): ")

time_zone_difference = input("Enter time zone difference (in hours and minutes): ")

origin = input("Enter origin (city which flight departed from): ")

destination = input("Enter destination (city which flight is going to): ")

local_time = (time.ctime(time.time())[:16])

t = local_time[11:]

hour = int(t[:2])
minute = int(t[3:])

if hour < 12:
    print("The local time is: {:02d}:{:02d} AM".format(hour,minute))
else:
    hour -= 12
    print("The local time is: {:02d}:{:02d} PM".format(hour,minute))
    hour += 12

if time_zone_difference[0] == "-":
    hour -= int(time_zone_difference[1:3])
    minute -= int(time_zone_difference[4:])
else:
    hour += int(time_zone_difference[:2])
    minute += int(time_zone_difference[3:])

if minute > 59:
    hour += 1
    minute -= 60

if hour > 23:
    hour -= 24

if hour < 12:
    print("Time at destination: {:02d}:{:02d} AM".format(hour,minute))
else:
    hour -= 12
    print("Time at destination: {:02d}:{:02d} PM".format(hour,minute))
    hour += 12

hour += int(flight_time[:2])
minute += int(flight_time[3:])

if hour > 23:
    hour -= 24

if minute > 59:
    minute -= 60
    hour += 1

if hour < 12:
    est_arrival =("Estimated Time of Arrival: {:02d}:{:02d} AM".format(hour,minute))
else:
    hour -= 12
    est_arrival =("Estimated Time of Arrival: {:02d}:{:02d} PM".format(hour,minute))
    hour += 12

hour_time_left = int(flight_time[:2])
minute_time_left = int(flight_time[3:])

minute_time_left -= 1
if minute_time_left < 0:
        minute_time_left += 60
        hour_time_left -= 1

import turtle as t

import math

t.goto (((720*2/math.pi)-200),0)

t.goto(-200,0)

t.write(origin)

t.lt(90)

for count in range(360):
    t.fd(2)
    t.rt(0.5)

t.write(destination)

t.goto(-200,0)

t.lt(180)

c = 0
local_time = (time.ctime(time.time())[:16])
ta = local_time[11:]
hour = int(ta[:2])
minute = int(ta[3:])
flag = True
a = "1"
while(flag == True):
    import turtle as t
    t.fd(2)
    t.rt(0.5)
    c += 1

    if c/360 == c//360:
        t.goto(((720/math.pi)-200),0)
        t.clear()
        t.write("Time left: {:} hours and {:} minutes".format(hour_time_left,minute_time_left))            
        t.goto(-200,0)
        t.goto(-200,0)
        t.write(origin)
        t.lt(180)

        for count in range(20):
            t.fd(2)
            t.rt(0.5)

        if a == "1":
            ta = (time.ctime(time.time())[11:16])
            hour_c = int(ta[:2])
            minute_c = int(ta[3:])
            if hour_c < 12:
                t.write("Time at Origin: {:02d}:{:02d} AM".format(hour_c,minute_c))
            else:
                hour_c -= 12
                t.write("Time at Origin: {:02d}:{:02d} PM".format(hour_c,minute_c))
                hour_c += 12
            a = "2"


        else:
            if time_zone_difference[0] == "-":
                hour_d = hour - int(time_zone_difference[1:3])
                minute_d = minute - int(time_zone_difference[4:])
            else:
                hour_d = hour + int(time_zone_difference[:2])
                minute_d = minute + int(time_zone_difference[3:])
                
            if minute_d > 59:
                hour_d += 1
                minute_d -= 60

            if hour_d > 23:
                hour_d -= 24
            elif hour_d < 0:
                hour_d += 24
            if hour_d < 12:
                t.write("Time at Destination: {:02d}:{:02d} AM".format(hour_d,minute_d))
            else:
                hour_d -= 12
                t.write("Time at Destination: {:02d}:{:02d} PM".format(hour_d,minute_d))
                hour_d += 12
            a = "1"
        for count in range(160):
            t.fd(2)
            t.rt(0.5)
        t.write(est_arrival)
        for count in range(180):
            t.fd(2)
            t.rt(0.5)
        t.write(destination)
        t.goto(-200,0)
        t.lt(180)

        ta = (time.ctime(time.time())[11:16])

        if hour != int(ta[:2]) and minute != int(ta[3:]):
            hour = int(ta[:2])
            minute = int(ta[3:])
            hour_time_left -= 1
           
        elif minute != int(ta[3:]):
            minute = int(ta[3:])
            minute_time_left -= 1

    if hour_time_left == 0 and minute_time_left == 0:
        flag = False
        t.clear()
        t.write("Arrived!")
    else:
        continue