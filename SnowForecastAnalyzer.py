# Snow Forecast Analyzer

a = []

snow_1 = eval(input("Enter Weather Underground estimated snowfall (in cm): "))
snow_2 = eval(input("Enter Weather Network estimated snowfall (in cm): "))
snow_3 = eval(input("Enter Accuweather estimated snowfall (in cm): "))

canada = input("Is Environment Canada forecast available (yes/no)? ")
if canada == "no":
    snow_4 = eval(input("Enter Weather Channel estimated snowfall (in cm): "))
else:
    snow_4 = eval(input("Enter Environment Canada estimated snowfall (in cm): "))

a.append(snow_1)
a.append(snow_2)
a.append(snow_3)
a.append(snow_4)

a.sort()

d_1 = a[1] - a[0]

d_2 = a[2] - a[1]

d_3 = a[3] - a[2]


if(d_1 != 0 and d_2 != 0 and d_3 != 0):

    if (d_1 > d_2 > d_3):
        factor = d_1/d_2
        factor_2 = d_1/d_3
        avg = (a[2] + a[3] + a[1]*(1/factor**2) + a[0]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

    elif (d_1 > d_3 > d_2):
        factor = d_1/d_3
        factor_2 = d_1/d_2
        avg = (a[2] + a[1] + a[3]*(1/factor**2) + a[0]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

    elif (d_2 > d_1 > d_3):
        factor = d_2/d_1
        factor_2 = d_2/d_3
        avg = (a[0] + a[3] + a[2]*(1/factor**2) + a[1]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

    elif (d_2 > d_3 > d_1):
        factor = d_2/d_3
        factor_2 = d_2/d_1
        avg = (a[0] + a[3] + a[1]*(1/factor**2) + a[2]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

    elif (d_3 > d_1 > d_2):
        factor = d_3/d_1
        factor_2 = d_3/d_2
        avg = (a[2] + a[1] + a[0]*(1/factor**2) + a[3]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

    elif (d_3 > d_2 > d_1):
        factor = d_3/d_2
        factor_2 = d_3/d_1
        avg = (a[0] + a[1] + a[2]*(1/factor**2) + a[3]*(1/factor_2**2))/(2 + 1/factor**2 + 1/factor_2**2)

else:
    avg = (a[0] + a[1] + a[2] + a[3])/4

print()

print("Estimated Snowfall Combined Forecast:", round(avg,1), "cm or", round((avg/2.54),1), "inches")
