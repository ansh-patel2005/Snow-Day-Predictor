import statistics

import time

while True:
    live = eval(input("Enter previous 5 HPI in a list: "))

    hpi_average = statistics.mean(live)

    hpi_start = live[0]
    
    hpi_starters = statistics.mean(live[0:1])

    hpi_enders = statistics.mean(live[3:])

    hpi_end = live[4]

    hpi_middle = live[2]

    est_calc_diff = (hpi_end - hpi_start + hpi_enders - hpi_starters + hpi_end - hpi_middle + hpi_enders - hpi_middle)/4


    act_diff = est_calc_diff/3

    time = input("Enter forecast time: ")

    hour = int(time[:2])
    minute = int(time[3:])

    forecast_lead_time = eval(input("Enter forecast lead time (in minutes): "))

    minute += forecast_lead_time
    if minute >= 60:
        minute-= 60
        hour += 1
    if hour >= 24:
        hour -= 24

    current_hpi = hpi_end

    print("{:02d}:{:02d} HPI: {:} GW".format(hour, minute, round(current_hpi,1)))

    for count in range(4):
        updated_hpi = current_hpi + act_diff
        minute += 5
        if minute >= 60:
            minute -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        print("{:02d}:{:02d} HPI: {:} GW".format(hour, minute, round(updated_hpi,1)))
        current_hpi = updated_hpi

    print()


