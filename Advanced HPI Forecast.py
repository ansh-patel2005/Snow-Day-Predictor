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

    solar_wind = input("Enter solar wind speed(d or u): ")
    
    if solar_wind == "d":
        if hpi_end > 40:
            est_calc_diff -= 1
        elif 30 <= hpi_end <= 40:
            est_calc_diff -= 0.66
        else:
            est_calc_diff -= 0.33
    elif solar_wind == "":
            est_calc_diff = est_calc_diff
    else:
        est_calc_diff += 1
        
    density = input("Enter density(d or u): ")
    
    if density == "d":
        if hpi_end > 40:
            est_calc_diff -= 1
        elif 30 <= hpi_end <= 40:
            est_calc_diff -= 0.66
        else:
            est_calc_diff -= 0.33
    elif density == "":
            est_calc_diff = est_calc_diff
    else:
        est_calc_diff += 1
        
    bt = input("Enter Bt(d or u): ")
    
    if bt == "d":
        if hpi_end > 40:
            est_calc_diff -= 1
        elif 30 <= hpi_end <= 40:
            est_calc_diff -= 0.66
        else:
            est_calc_diff -= 0.33
    elif bt == "":
            est_calc_diff = est_calc_diff
    else:
        est_calc_diff += 2
        
    bz = input("Enter Bz(d or u): ")
    
    if bz == "d":
        if hpi_end > 40:
            est_calc_diff -= 1
        elif 30 <= hpi_end <= 40:
            est_calc_diff -= 0.66
        else:
            est_calc_diff -= 0.33
    elif bz == "":
            est_calc_diff = est_calc_diff
    else:
        est_calc_diff += 3


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


