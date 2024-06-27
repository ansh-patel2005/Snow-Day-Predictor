# Snow Day Predictor
# Can be used for any location

# Timeline

# Version 5 - Another bug fix with improvements in calculations.
# Date: March 4, 2023

# Version 4 - Bug Fix as well as updates to have better calculations.
# Date: March 2, 2023

# Version 3 - Integration of SnowForecastAnalyzer into the Snow Day Predictor to predict more in advance about the possibility of a snow day (although
# highest accuracy comes when the hourly forecast is available). Also added option to user of hyper-accurate forecasts but requires user to input more
# information.
# Date: February 20, 2023

# Version 2 - Improvements in calibration for any city rather than just the Greater Toronto Area and fixed an error
# Date: December 19, 2022

# Version 1 - Snow Day Predictor created
# Date: December 16, 2022

ask = input("Is hourly forecast available currently for the day preceding the storm leading up to the morning of the anticipated snow day(yes/no)? ")

accuracy = input("Do you want a hyper-accurate forecast even though it may take a long time to input all the information required (yes/no)? ")

print("Note: Ice amounts in mm should be multiplied by 10 and included in snow")

if(ask == "yes" and accuracy == "yes"):
    for count in range(3):
        print()
        if count == 0:
            print("Input Forecast using Weather Underground or Weather Channel")
            snow_10pm_wu = eval(input("Enter snow at 10 pm hour (in cm): "))
            snow_11pm_wu = eval(input("Enter snow at 11 pm hour (in cm): "))
            snow_12am_wu = eval(input("Enter snow at 12 am hour (in cm): "))
            snow_1am_wu = eval(input("Enter snow at 1 am hour (in cm): "))
            snow_2am_wu = eval(input("Enter snow at 2 am hour (in cm): "))
            snow_3am_wu = eval(input("Enter snow at 3 am hour (in cm): "))
            snow_4am_wu = eval(input("Enter snow at 4 am hour (in cm): "))
            snow_5am_wu = eval(input("Enter snow at 5 am hour (in cm): "))
            snow_6am_wu = eval(input("Enter snow at 6 am hour (in cm): "))
            snow_7am_wu = eval(input("Enter snow at 7 am hour (in cm): "))
            snow_8am_wu = eval(input("Enter snow at 8 am hour (in cm): "))
            snow_9am_wu = eval(input("Enter snow at 9 am hour (in cm): "))
        elif count == 1:
            print()
            print("Input Forecast using Weather Network")
            snow_10pm_wn = eval(input("Enter snow at 10 pm hour (in cm): "))
            snow_11pm_wn = eval(input("Enter snow at 11 pm hour (in cm): "))
            snow_12am_wn = eval(input("Enter snow at 12 am hour (in cm): "))
            snow_1am_wn = eval(input("Enter snow at 1 am hour (in cm): "))
            snow_2am_wn = eval(input("Enter snow at 2 am hour (in cm): "))
            snow_3am_wn = eval(input("Enter snow at 3 am hour (in cm): "))
            snow_4am_wn = eval(input("Enter snow at 4 am hour (in cm): "))
            snow_5am_wn = eval(input("Enter snow at 5 am hour (in cm): "))
            snow_6am_wn = eval(input("Enter snow at 6 am hour (in cm): "))
            snow_7am_wn = eval(input("Enter snow at 7 am hour (in cm): "))
            snow_8am_wn = eval(input("Enter snow at 8 am hour (in cm): "))
            snow_9am_wn = eval(input("Enter snow at 9 am hour (in cm): "))
        elif count == 2:
            print()
            print("Input Forecast using Accuweather")
            snow_10pm_a = eval(input("Enter snow at 10 pm hour (in cm): "))
            snow_11pm_a = eval(input("Enter snow at 11 pm hour (in cm): "))
            snow_12am_a = eval(input("Enter snow at 12 am hour (in cm): "))
            snow_1am_a = eval(input("Enter snow at 1 am hour (in cm): "))
            snow_2am_a = eval(input("Enter snow at 2 am hour (in cm): "))
            snow_3am_a = eval(input("Enter snow at 3 am hour (in cm): "))
            snow_4am_a = eval(input("Enter snow at 4 am hour (in cm): "))
            snow_5am_a = eval(input("Enter snow at 5 am hour (in cm): "))
            snow_6am_a = eval(input("Enter snow at 6 am hour (in cm): "))
            snow_7am_a = eval(input("Enter snow at 7 am hour (in cm): "))
            snow_8am_a = eval(input("Enter snow at 8 am hour (in cm): "))
            snow_9am_a = eval(input("Enter snow at 9 am hour (in cm): "))

    s = [[snow_10pm_wu, snow_10pm_wn, snow_10pm_a],[snow_11pm_wu, snow_11pm_wn, snow_11pm_a],[snow_12am_wu, snow_12am_wn, snow_12am_a],[snow_1am_wu, snow_1am_wn, snow_1am_a],[snow_2am_wu, snow_2am_wn, snow_2am_a],[snow_3am_wu, snow_3am_wn, snow_3am_a],[snow_4am_wu, snow_4am_wn, snow_4am_a],[snow_5am_wu, snow_5am_wn, snow_5am_a], [snow_6am_wu, snow_6am_wn, snow_6am_a], [snow_7am_wu, snow_7am_wn, snow_7am_a], [snow_8am_wu, snow_8am_wn, snow_8am_a], [snow_9am_wu, snow_9am_wn, snow_9am_a]]

    total_snow = 0
    actual_snow = 0

    for count in range(12):
        a = []
        for count_2 in range(3):
            a.append(s[count][count_2])

        a.sort()

        d_1 = a[1] - a[0]

        d_2 = a[2] - a[1]

        if(d_1 == 0):
            d_1 = 0.01
        if(d_2 == 0):
            d_2 = 0.01

        if (d_1 > d_2):
            factor = d_1/d_2
            avg = (a[2] + a[1] + a[0]*(1/factor**2))/(2 + 1/factor**2)

        elif (d_2 > d_1):
            factor = d_2/d_1
            avg = (a[0] + a[1] + a[2]*(1/factor**2))/(2 + 1/factor**2)

        else:
            avg = (a[0] + a[1] + a[2]/3)

        if count == 11:
            total_snow += avg*(1.2**9)
        else:
            total_snow += avg*(1.2**count)
        actual_snow += avg
        if count == 11:
            if avg < 0.5:
                total_snow -= 1.0
            elif avg < 1.0:
                total_snow -= 0.5

        if count == 10:
            if avg < 0.5:
                total_snow -= 1.0
            elif avg < 1.0:
                total_snow -= 0.5

        if count == 9:
            if avg < 0.5:
                total_snow -= 1.0
            elif avg < 1.0:
                total_snow -= 0.5

        if count == 8:
            if avg < 0.5:
                total_snow -= 1.0
            elif avg < 1.0:
                total_snow -= 0.5

        if snow_6am_wu < snow_5am_wu < snow_4am_wu < snow_3am_wu:
            total_snow -= 2.0

    print()

    ten_cm_days = eval(input("Enter number of days when it snows 10 cm or more in your city: "))

    if(ten_cm_days == 0):
        ten_cm_days = 0.01

    adjustment = 2.7/ten_cm_days

    x = actual_snow - 15

    if(x > 0):
        multiplier = (actual_snow*x**(5/9)/15)*adjustment
        total_snow *= multiplier
    else:
        total_snow*=adjustment

    if(total_snow == 0 and actual_snow > 0):
        if(annual_snow < 1):
            if(annual_snow == 0):
                total_snow = 0.99*actual_snow
            else:
                total_snow = (1-annual_snow)*actual_snow

    annual_snow = eval(input("Enter annual snowfall in your city (in cm): "))
    print()
    if(annual_snow == 0):
        annual_snow = 0.01
    percent_snow_day = total_snow*(100/annual_snow)
    if percent_snow_day < 0:
        percent_snow_day = 0
    if percent_snow_day > 100:
        percent_snow_day = 100
    ask_user = input("Do you want to know exact probability of a snow day or no? (Yes/No): ")
    if ask_user == "Yes":
        print(round(percent_snow_day,2),"%")
    if percent_snow_day < 20:
        print("Good luck with your snow day!")
    elif percent_snow_day < 40:
        print("Although not likely, there is a possibility of a snow day!")
    elif percent_snow_day < 60:
        print("Moderate likelihood of a snow day!")
    elif percent_snow_day < 80:
        print("Snow day quite likely!")
    else:
        print("Snow day for sure!")

elif(ask == "yes"):

    snow_10pm = eval(input("Enter snow at 10 pm hour (in cm): "))
    snow_11pm = eval(input("Enter snow at 11 pm hour (in cm): "))
    snow_12am = eval(input("Enter snow at 12 am hour (in cm): "))
    snow_1am = eval(input("Enter snow at 1 am hour (in cm): "))
    snow_2am = eval(input("Enter snow at 2 am hour (in cm): "))
    snow_3am = eval(input("Enter snow at 3 am hour (in cm): "))
    snow_4am = eval(input("Enter snow at 4 am hour (in cm): "))
    snow_5am = eval(input("Enter snow at 5 am hour (in cm): "))
    snow_6am = eval(input("Enter snow at 6 am hour (in cm): "))
    snow_7am = eval(input("Enter snow at 7 am hour (in cm): "))
    snow_8am = eval(input("Enter snow at 8 am hour (in cm): "))
    snow_9am = eval(input("Enter snow at 9 am hour (in cm): "))

    ## Adjusting Factors ##

    total_snow = snow_10pm + snow_11pm*1.2 + snow_12am*1.2**2 + snow_1am*1.2**3 + snow_2am*1.2**4 + snow_3am*1.2**5 + snow_4am*1.2**6 + snow_5am*1.2**7 + snow_6am*1.2**8 + snow_7am*1.2**9 + snow_8am*1.2**10 + snow_9am*1.2**9
    actual_total = snow_10pm + snow_11pm + snow_12am + snow_1am + snow_2am + snow_3am + snow_4am + snow_5am + snow_6am + snow_7am + snow_8am + snow_9am

    ten_cm_days = eval(input("Enter number of days when it snows 10 cm or more in your city: "))

    if(ten_cm_days == 0):
        ten_cm_days = 0.01

    if snow_9am < 0.5:
        total_snow -= 1.0
    elif snow_9am < 1.0:
        total_snow -= 0.5

    if snow_8am < 0.5:
        total_snow -= 1.0
    elif snow_8am < 1.0:
        total_snow -= 0.5

    if snow_7am < 0.5:
        total_snow -= 1.0
    elif snow_9am < 1.0:
        total_snow -= 0.5

    if snow_6am < 0.5:
        total_snow -= 1.0
    elif snow_6am < 1.0:
        total_snow -= 0.5

    if snow_6am < snow_5am < snow_4am < snow_3am:
        total_snow -= 2.0

    adjustment = 2.7/ten_cm_days

    x = actual_total - 15

    if(x > 0):
        multiplier = (actual_total*x**(5/9)/15)*adjustment
        total_snow *= multiplier
    else:
        total_snow*=adjustment

    if(total_snow == 0 and actual_total > 0):
        if(annual_snow < 1):
            if(annual_snow == 0):
                total_snow = 0.99*actual_total
            else:
                total_snow = (1-annual_snow)*actual_total

    if(total_snow < 0):
        total_snow = 0

    annual_snow = eval(input("Enter annual snowfall in your city (in cm): "))
    print()
    if(annual_snow == 0):
        annual_snow = 0.01
    percent_snow_day = total_snow*(100/annual_snow)
    if percent_snow_day > 100:
        percent_snow_day = 100
    ask_user = input("Do you want to know exact probability of a snow day or no? (Yes/No): ")
    if ask_user == "Yes":
        print(round(percent_snow_day,2),"%")
    if percent_snow_day < 20:
        print("Good luck with your snow day!")
    elif percent_snow_day < 40:
        print("Although not likely, there is a possibility of a snow day!")
    elif percent_snow_day < 60:
        print("Moderate likelihood of a snow day!")
    elif percent_snow_day < 80:
        print("Snow day quite likely!")
    else:
        print("Snow day for sure!")

else:
    import SnowForecastAnalyzer

    from SnowForecastAnalyzer import *

    snow_10pm = avg/12
    snow_11pm = avg/12
    snow_12am = avg/12
    snow_1am = avg/12
    snow_2am = avg/12
    snow_3am = avg/12
    snow_4am = avg/12
    snow_5am = avg/12
    snow_6am = avg/12
    snow_7am = avg/12
    snow_8am = avg/12
    snow_9am = avg/12

    total_snow = snow_10pm + snow_11pm*1.2 + snow_12am*1.2**2 + snow_1am*1.2**3 + snow_2am*1.2**4 + snow_3am*1.2**5 + snow_4am*1.2**6 + snow_5am*1.2**7 + snow_6am*1.2**8 + snow_7am*1.2**9 + snow_8am*1.2**10 + snow_9am*1.2**9

    actual_total = snow_10pm + snow_11pm + snow_12am + snow_1am + snow_2am + snow_3am + snow_4am + snow_5am + snow_6am + snow_7am + snow_8am + snow_9am

    ten_cm_days = eval(input("Enter number of days when it snows 10 cm or more in your city: "))

    if(ten_cm_days == 0):
        ten_cm_days = 0.01

    adjustment = 2.7/ten_cm_days

    x = actual_total - 15

    if(x > 0):
        multiplier = (actual_total*x**(5/9)/15)*adjustment
        total_snow *= multiplier
    else:
        total_snow*=adjustment

    if(total_snow == 0 and actual_total > 0):
        if(annual_snow < 1):
            if(annual_snow == 0):
                total_snow = 0.99*actual_total
            else:
                total_snow = (1-annual_snow)*actual_total

    annual_snow = eval(input("Enter annual snowfall in your city (in cm): "))
    print()
    if(annual_snow == 0):
        annual_snow = 0.01
    percent_snow_day = total_snow*(100/annual_snow)
    if percent_snow_day > 100:
        percent_snow_day = 100
    ask_user = input("Do you want to know exact probability of a snow day or no? (Yes/No): ")
    if ask_user == "Yes":
        print(round(percent_snow_day,2),"%", sep = "")
    if percent_snow_day < 20:
        print("Good luck with your snow day!")
    elif percent_snow_day < 40:
        print("Although not likely, there is a possibility of a snow day!")
    elif percent_snow_day < 60:
        print("Moderate likelihood of a snow day!")
    elif percent_snow_day < 80:
        print("Snow day quite likely!")
    else:
        print("Snow day for sure!")

